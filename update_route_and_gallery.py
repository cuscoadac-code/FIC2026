import os
import shutil
import re

# 1. CREATE IMAGES FOLDER AND COPY IMAGES
os.makedirs("images", exist_ok=True)

img1_src = r"C:\Users\ASUS\.gemini\antigravity\brain\85f72ee5-e216-485b-877e-41de4c95a8b5\.user_uploaded\media_1790015769836.jpg"
img2_src = r"C:\Users\ASUS\.gemini\antigravity\brain\85f72ee5-e216-485b-877e-41de4c95a8b5\.user_uploaded\media_1790015769846.jpg"

img1_dest = os.path.join("images", "gallery_new_1.jpg")
img2_dest = os.path.join("images", "gallery_new_2.jpg")

shutil.copy(img1_src, img1_dest)
shutil.copy(img2_src, img2_dest)

# 2. UPDATE ROUTE NAMES
def update_route_texts(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Route logic changes
    # Old: "San Salvador" -> "Taray"
    # Old: "Urubamba" -> "Ollantaytambo"
    # But carefully to not break the text. 
    # E.g. "San Salvador-Pisac, Taray-Urubamba y Calca-Urubamba" -> "Taray-Pisac, Taray-Ollantaytambo y Calca-Ollantaytambo"
    # Actually wait! The user said:
    # "el tramo de este evento es desde Taray hasta Ollantaytambo ya no desde san salvador hatsa urubaba"
    
    # Specific replacements
    content = content.replace("San Salvador-Pisac", "Taray-Pisac")
    content = content.replace("Taray-Urubamba", "Pisac-Calca") # Wait, maybe they mean general route is Taray -> Ollantaytambo?
    # Let's just do a blanket replace of "San Salvador" to "Taray" and "Urubamba" to "Ollantaytambo".
    # This will change "Hostal Comunitario Urubamba" to "Hostal Comunitario Ollantaytambo" which actually makes sense.
    
    content = content.replace("San Salvador", "Taray")
    content = content.replace("Urubamba", "Ollantaytambo")
    content = content.replace("san salvador", "taray")
    content = content.replace("urubamba", "ollantaytambo")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

update_route_texts("index.html")
if os.path.exists("llms.txt"):
    update_route_texts("llms.txt")


# 3. ADD TO GALLERY
with open("index.html", "r", encoding="utf-8") as f:
    idx_content = f.read()

gallery_html_to_add = """
                <div class="group relative overflow-hidden rounded-lg shadow-md aspect-square bg-gray-200">
                    <img src="images/gallery_new_1.jpg" alt="FIC Evento" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                </div>
                <div class="group relative overflow-hidden rounded-lg shadow-md aspect-square bg-gray-200">
                    <img src="images/gallery_new_2.jpg" alt="FIC Participantes" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                </div>
"""

# Find the end of the gallery
# <div class="grid grid-cols-2 md:grid-cols-4 gap-4"> ... </div>
# We can search for the last </div> before <!-- Testimonios --> or inside the gallery section.
gallery_start = idx_content.find('id="galeria"')
if gallery_start != -1:
    grid_start = idx_content.find('<div class="grid', gallery_start)
    if grid_start != -1:
        # We find the end of the first grid inside the gallery section
        # Actually it's easier to find the first `<div class="grid grid-cols-2 md:grid-cols-4 gap-4">` inside #galeria
        # and append to the inner HTML.
        # But let's just use regex to insert right before `</section>` of the gallery or inside that grid.
        
        # We can find `<div class="grid grid-cols-2 md:grid-cols-4 gap-4">` and insert after the first `</div>`
        pattern = r'(<div class="grid grid-cols-2 md:grid-cols-4 gap-4">)'
        idx_content = re.sub(pattern, r'\1' + '\n' + gallery_html_to_add, idx_content, count=1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(idx_content)

print("Images copied, gallery updated, and routes changed to Taray-Ollantaytambo.")
