import os
import shutil
import re

# List of the 8 uploaded files
files = [
    "media_1790099434865.jpg",
    "media_1790099434873.jpg",
    "media_1790099434882.jpg",
    "media_1790099434891.jpg",
    "media_1790099447477.jpg",
    "media_1790099450371.jpg",
    "media_1790099464670.jpg",
    "media_1790099466540.jpg"
]

source_dir = r"C:\Users\ASUS\.gemini\antigravity\brain\85f72ee5-e216-485b-877e-41de4c95a8b5\.user_uploaded"
dest_dir = r"C:\Users\ASUS\.gemini\antigravity\scratch\ciclovia-maiz\images"

for i, filename in enumerate(files):
    src = os.path.join(source_dir, filename)
    dst = os.path.join(dest_dir, f"gallery_{i+1}.jpg")
    try:
        shutil.copy2(src, dst)
        print(f"Copied {filename} to gallery_{i+1}.jpg")
    except Exception as e:
        print(f"Error copying {filename}: {e}")

# Now update the HTML
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Generate new gallery HTML
new_gallery_html = '<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">\n'
for i in range(1, 9):
    new_gallery_html += f"""                <div class="group relative overflow-hidden rounded-lg shadow-md aspect-square bg-gray-200">
                    <img src="images/gallery_{i}.jpg" alt="FIC 2026 Galería" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500 hover:shadow-2xl">
                </div>\n"""
new_gallery_html += '            </div>'

# Regex to replace the old gallery grid
# The old gallery starts with <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
# and ends with the matching </div> before <!-- Sponsors -->
content = re.sub(
    r'<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">[\s\S]*?</div>\s*</div>\s*<!-- Sponsors -->',
    new_gallery_html + '\n\n            <!-- Sponsors -->',
    content
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Gallery updated in HTML.")
