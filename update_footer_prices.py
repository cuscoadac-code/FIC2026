import os

# Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Prices
content = content.replace("Básico ($80 USD)", "Básico (S/ 300)")
content = content.replace("Premium ($150 USD)", "Premium (S/ 560)")
content = content.replace("VIP ($250 USD)", "VIP (S/ 940)")

# 2. Footer Info
# Replace old address "Plaza de Armas, Cusco, Perú" with new address
content = content.replace("Plaza de Armas, Cusco, Perú", "Mz. a Lote 21 Urb. Mariscal Gamarra I Etapa, Cusco")

# Add ayni sport email next to or replacing the old email
content = content.replace("info@cicloviadelmaiz.com", "info@cicloviadelmaiz.com</span>\n</li>\n<li class=\"flex items-start\">\n<div class=\"w-5 h-5 flex items-center justify-center text-gray-400 mt-1 mr-2\">\n<i class=\"ri-mail-line\"></i>\n</div>\n<span class=\"text-gray-400\">aynisporteam@gmail.com")

# Replace old phone "+51 84 123 456" with new WhatsApp
content = content.replace("+51 84 123 456", "+51 993 022 225")

# 3. Facebook link
# The first <a href="#"> enclosing <i class="ri-facebook-fill"></i>
fb_old = '<a href="#" class="text-gray-400 hover:text-white transition-colors">\n<div class="w-8 h-8 flex items-center justify-center">\n<i class="ri-facebook-fill"></i>'
fb_new = '<a href="https://www.facebook.com/profile.php?id=61562076251040&locale=es_LA" target="_blank" class="text-gray-400 hover:text-white transition-colors">\n<div class="w-8 h-8 flex items-center justify-center">\n<i class="ri-facebook-fill"></i>'
content = content.replace(fb_old, fb_new)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)


# Update llms.txt
if os.path.exists("llms.txt"):
    with open("llms.txt", "r", encoding="utf-8") as f:
        llms_content = f.read()
    
    llms_content = llms_content.replace("Básico ($80 USD)", "Básico (S/ 300)")
    llms_content = llms_content.replace("Premium ($150 USD)", "Premium (S/ 560)")
    llms_content = llms_content.replace("VIP ($250 USD)", "VIP (S/ 940)")

    with open("llms.txt", "w", encoding="utf-8") as f:
        f.write(llms_content)

print("Footer, prices and links updated.")
