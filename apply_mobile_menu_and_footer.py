import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. MOBILE MENU
# The mobile menu button:
# <button class="text-white focus:outline-none">
# We need to give it an ID and add the mobile menu div right after the <nav> ends.
menu_button_pattern = r'(<button) (class="text-white focus:outline-none">)'
content = re.sub(menu_button_pattern, r'\1 id="mobile-menu-btn" \2', content, count=1)

mobile_menu_html = """
<!-- Mobile Menu -->
<div id="mobile-menu" class="hidden md:hidden bg-gray-900 border-t border-gray-800">
    <div class="flex flex-col px-6 py-4 space-y-4 text-white font-bold">
        <a href="#inicio" class="mobile-link hover:text-primary transition-colors">Inicio</a>
        <a href="#ruta" class="mobile-link hover:text-primary transition-colors">La Ruta</a>
        <a href="#festival" class="mobile-link hover:text-primary transition-colors">El Festival</a>
        <a href="#categorias" class="mobile-link hover:text-primary transition-colors">Categorías</a>
        <a href="#turismo" class="mobile-link hover:text-primary transition-colors">Turismo</a>
        <a href="#galeria" class="mobile-link hover:text-primary transition-colors">Galería</a>
        <a href="#voluntariado" class="mobile-link hover:text-primary transition-colors">Voluntariado</a>
        <a href="#faq" class="mobile-link hover:text-primary transition-colors">FAQ</a>
        <a href="resultados.html" class="hover:text-primary transition-colors">Resultados</a>
        <a href="blog.html" class="hover:text-primary transition-colors">Blog</a>
        <a href="#inscripcion" class="mobile-link text-primary hover:text-white transition-colors">Inscripción</a>
    </div>
</div>
"""

# Insert mobile menu right after </nav>
if 'id="mobile-menu"' not in content:
    content = content.replace("</nav>", "</nav>\n" + mobile_menu_html)

# Add script for mobile menu
mobile_js = """
<script>
    document.addEventListener('DOMContentLoaded', () => {
        const btn = document.getElementById('mobile-menu-btn');
        const menu = document.getElementById('mobile-menu');
        const links = document.querySelectorAll('.mobile-link');
        
        if(btn && menu) {
            btn.addEventListener('click', () => {
                menu.classList.toggle('hidden');
            });
            
            links.forEach(link => {
                link.addEventListener('click', () => {
                    menu.classList.add('hidden');
                });
            });
        }
    });
</script>
"""
if 'mobile-menu-btn' not in content or 'mobile-link' in mobile_menu_html:
    if 'const btn = document.getElementById(\'mobile-menu-btn\');' not in content:
        content = content.replace("</body>", mobile_js + "\n</body>")


# 2. FOOTER LINKS
# Find the Enlaces Rápidos block
enlaces_block = """<ul class="space-y-2">
<li><a href="#inicio" class="text-gray-400 hover:text-white transition-colors">Inicio</a></li>
<li><a href="#ruta" class="text-gray-400 hover:text-white transition-colors">La Ruta</a></li>
<li><a href="#festival" class="text-gray-400 hover:text-white transition-colors">El Festival</a></li>
<li><a href="#categorias" class="text-gray-400 hover:text-white transition-colors">Categorías</a></li>
<li><a href="#turismo" class="text-gray-400 hover:text-white transition-colors">Turismo</a></li>
<li><a href="#inscripcion" class="text-gray-400 hover:text-white transition-colors">Inscripción</a></li>
</ul>"""

new_enlaces_block = """<ul class="space-y-2">
<li><a href="#inicio" class="text-gray-400 hover:text-white transition-colors">Inicio</a></li>
<li><a href="#ruta" class="text-gray-400 hover:text-white transition-colors">La Ruta</a></li>
<li><a href="#festival" class="text-gray-400 hover:text-white transition-colors">El Festival</a></li>
<li><a href="#categorias" class="text-gray-400 hover:text-white transition-colors">Categorías</a></li>
<li><a href="#turismo" class="text-gray-400 hover:text-white transition-colors">Turismo</a></li>
<li><a href="#galeria" class="text-gray-400 hover:text-white transition-colors">Galería</a></li>
<li><a href="#voluntariado" class="text-gray-400 hover:text-white transition-colors">Voluntariado</a></li>
<li><a href="#faq" class="text-gray-400 hover:text-white transition-colors">Preguntas Frecuentes</a></li>
<li><a href="resultados.html" class="text-gray-400 hover:text-white transition-colors">Resultados</a></li>
<li><a href="blog.html" class="text-gray-400 hover:text-white transition-colors">Blog</a></li>
<li><a href="#inscripcion" class="text-primary font-bold hover:text-white transition-colors">Inscripción</a></li>
</ul>"""

# If the block has some corruption, try to regex replace the whole ul inside the "Enlaces Rápidos" section.
ul_pattern = r'<h4 class="font-bold mb-4">Enlaces Rápidos</h4>\s*<ul class="space-y-2">.*?</ul>'
# Fallback for accent corruption
ul_pattern_fallback = r'<h4 class="font-bold mb-4">Enlaces R.*?pidos</h4>\s*<ul class="space-y-2">.*?</ul>'

replacement = '<h4 class="font-bold mb-4">Enlaces Rápidos</h4>\n' + new_enlaces_block

if re.search(ul_pattern, content, flags=re.DOTALL):
    content = re.sub(ul_pattern, replacement, content, flags=re.DOTALL)
else:
    content = re.sub(ul_pattern_fallback, replacement, content, flags=re.DOTALL)


# 3. CIX LAB SIGNATURE
old_copyright = r'<p class="text-gray-400 text-sm mb-4 md:mb-0">&copy; 2026 Ciclov.a del Ma.z\. Todos los derechos reservados\.</p>'
new_copyright = '<p class="text-gray-400 text-sm mb-4 md:mb-0">&copy; 2026 Ciclovía del Maíz. Todos los derechos reservados. Desarrollado por <a href="https://cixlab.site" target="_blank" class="text-primary hover:text-white transition-colors font-bold">Cix Lab</a>.</p>'

content = re.sub(old_copyright, new_copyright, content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Mobile menu, footer links, and Cix Lab signature updated.")
