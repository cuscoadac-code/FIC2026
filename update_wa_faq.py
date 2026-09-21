import os
import re
import glob

# 1. Update WhatsApp numbers in all relevant files
files_to_update = glob.glob("*.html") + ["llms.txt"]
old_number = "51994381708"
new_number = "51993022225"

old_formatted = "+51 994 381 708"
new_formatted = "+51 993 022 225"

for file_path in files_to_update:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Update wa.me links and JS redirects
    content = content.replace(old_number, new_number)
    # Update text representations
    content = content.replace(old_formatted, new_formatted)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


# 2. Add FAQ section to index.html
with open("index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

faq_html = """
    <!-- Preguntas Frecuentes -->
    <section id="faq" class="py-20 bg-white">
        <div class="container mx-auto px-6 max-w-4xl">
            <div class="text-center mb-16">
                <span class="text-primary font-bold tracking-widest uppercase text-sm mb-2 block">Dudas Comunes</span>
                <h2 class="text-4xl font-bold text-secondary mb-4">Preguntas Frecuentes</h2>
                <div class="w-24 h-1 bg-primary mx-auto mb-6"></div>
                <p class="text-gray-600 text-lg">Todo lo que necesitas saber sobre el evento, las rutas y las inscripciones.</p>
            </div>
            
            <div class="space-y-4">
                <!-- FAQ Item 1 -->
                <div class="border rounded-lg overflow-hidden">
                    <button class="w-full text-left px-6 py-4 bg-gray-50 hover:bg-gray-100 font-bold text-secondary flex justify-between items-center focus:outline-none faq-toggle">
                        <span>¿Es obligatorio tener licencia UCI para participar?</span>
                        <i class="ri-arrow-down-s-line text-xl transition-transform duration-300"></i>
                    </button>
                    <div class="px-6 py-4 text-gray-600 bg-white border-t hidden faq-content">
                        No, la Ciclovía del Maíz es un evento de formato abierto. Tenemos categorías tanto para ciclistas profesionales (Elite) como para aficionados y principiantes. ¡Todos son bienvenidos!
                    </div>
                </div>

                <!-- FAQ Item 2 -->
                <div class="border rounded-lg overflow-hidden">
                    <button class="w-full text-left px-6 py-4 bg-gray-50 hover:bg-gray-100 font-bold text-secondary flex justify-between items-center focus:outline-none faq-toggle">
                        <span>¿Qué incluye el kit de inscripción?</span>
                        <i class="ri-arrow-down-s-line text-xl transition-transform duration-300"></i>
                    </button>
                    <div class="px-6 py-4 text-gray-600 bg-white border-t hidden faq-content">
                        El kit básico incluye: Dorsal oficial, medalla finisher (al completar la carrera), puntos de hidratación y nutrición en ruta, y asistencia médica. Los paquetes Premium y VIP incluyen jerseys oficiales, pases a eventos VIP y más sorpresas.
                    </div>
                </div>

                <!-- FAQ Item 3 -->
                <div class="border rounded-lg overflow-hidden">
                    <button class="w-full text-left px-6 py-4 bg-gray-50 hover:bg-gray-100 font-bold text-secondary flex justify-between items-center focus:outline-none faq-toggle">
                        <span>¿Puedo cambiar de categoría después de inscribirme?</span>
                        <i class="ri-arrow-down-s-line text-xl transition-transform duration-300"></i>
                    </button>
                    <div class="px-6 py-4 text-gray-600 bg-white border-t hidden faq-content">
                        Sí, se permiten cambios de categoría hasta 30 días antes del evento. Deberás comunicarte con soporte vía WhatsApp para realizar la gestión sin costo adicional.
                    </div>
                </div>

                <!-- FAQ Item 4 -->
                <div class="border rounded-lg overflow-hidden">
                    <button class="w-full text-left px-6 py-4 bg-gray-50 hover:bg-gray-100 font-bold text-secondary flex justify-between items-center focus:outline-none faq-toggle">
                        <span>¿Cuáles son las restricciones para la categoría E-Bike?</span>
                        <i class="ri-arrow-down-s-line text-xl transition-transform duration-300"></i>
                    </button>
                    <div class="px-6 py-4 text-gray-600 bg-white border-t hidden faq-content">
                        Las E-Bikes (Bicicletas de pedaleo asistido) solo pueden competir en su propia categoría exclusiva. Está estrictamente prohibido usar E-Bikes en categorías Master o Elite convencionales.
                    </div>
                </div>
            </div>
            
            <div class="text-center mt-10">
                <p class="text-gray-600 mb-4">¿Tienes otra duda?</p>
                <a href="https://wa.me/51993022225" target="_blank" class="inline-flex items-center text-primary font-bold hover:text-secondary transition-colors text-lg">
                    Contáctanos por WhatsApp <i class="ri-whatsapp-line ml-2 text-2xl"></i>
                </a>
            </div>
        </div>
    </section>
"""

# Insert FAQ right before <section id="inscripcion"
if '<section id="faq"' not in index_content:
    index_content = index_content.replace('<section id="inscripcion"', faq_html + '\n<section id="inscripcion"')

# Inject JS for FAQ Accordion logic
js_faq = """
<script>
    // FAQ Accordion
    document.addEventListener('DOMContentLoaded', () => {
        const faqToggles = document.querySelectorAll('.faq-toggle');
        faqToggles.forEach(toggle => {
            toggle.addEventListener('click', () => {
                const content = toggle.nextElementSibling;
                const icon = toggle.querySelector('i');
                
                // Toggle visibility
                content.classList.toggle('hidden');
                
                // Rotate icon
                if (content.classList.contains('hidden')) {
                    icon.style.transform = 'rotate(0deg)';
                } else {
                    icon.style.transform = 'rotate(180deg)';
                }
            });
        });
    });
</script>
"""

if 'const faqToggles' not in index_content:
    index_content = index_content.replace('</body>', js_faq + '\n</body>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_content)

print("WhatsApp numbers updated and FAQ section added.")
