import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add "Voluntariado" to nav menu (Gallery was already added in the previous python script, but since it didn't run, I'll add both)
nav_item = '<a href="index.html#galeria" class="hover:text-primary transition-colors">Galería</a>\n<a href="index.html#voluntariado" class="hover:text-primary transition-colors">Voluntariado</a>\n<a href="blog.html"'
content = content.replace('<a href="blog.html"', nav_item)

# 2. HTML for Gallery Section
gallery_html = """
    <!-- Sección de Galería -->
    <section id="galeria" class="py-20 bg-white">
        <div class="container mx-auto px-6">
            <div class="text-center mb-16">
                <h2 class="text-4xl md:text-5xl font-bold text-secondary mb-4">Galería de Eventos Anteriores</h2>
                <div class="w-24 h-1 bg-primary mx-auto mb-6"></div>
                <p class="text-gray-600 max-w-2xl mx-auto text-lg">Revive la emoción, el esfuerzo y los increíbles paisajes de nuestras ediciones pasadas a través de nuestra selección de fotos y videos.</p>
            </div>

            <!-- Videos -->
            <h3 class="text-3xl font-bold text-secondary mb-8 border-b-2 border-primary pb-2 inline-block">Videos Destacados</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-16">
                <div class="relative pb-[56.25%] h-0 rounded-lg overflow-hidden shadow-lg bg-gray-200 flex items-center justify-center">
                    <span class="text-gray-500 absolute inset-0 flex items-center justify-center">Video de YouTube (Reemplazar src)</span>
                    <iframe src="https://www.youtube.com/embed/Ejemplo1" title="Video resumen FIC" class="absolute top-0 left-0 w-full h-full border-0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                </div>
                <div class="relative pb-[56.25%] h-0 rounded-lg overflow-hidden shadow-lg bg-gray-200 flex items-center justify-center">
                    <span class="text-gray-500 absolute inset-0 flex items-center justify-center">Video de YouTube (Reemplazar src)</span>
                    <iframe src="https://www.youtube.com/embed/Ejemplo2" title="Testimonios FIC" class="absolute top-0 left-0 w-full h-full border-0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                </div>
            </div>

            <!-- Fotos -->
            <h3 class="text-3xl font-bold text-secondary mb-8 border-b-2 border-primary pb-2 inline-block">Fotos Históricas</h3>
            <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                <div class="group relative overflow-hidden rounded-lg shadow-md aspect-square bg-gray-200">
                    <img src="https://images.unsplash.com/photo-1544181093-c712c9a1d131?q=80&w=600&auto=format&fit=crop" alt="Ciclismo Cusco" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                </div>
                <div class="group relative overflow-hidden rounded-lg shadow-md aspect-square bg-gray-200">
                    <img src="https://images.unsplash.com/photo-1511994298241-608e28f14fde?q=80&w=600&auto=format&fit=crop" alt="MTB Action" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                </div>
                <div class="group relative overflow-hidden rounded-lg shadow-md aspect-square bg-gray-200">
                    <img src="https://images.unsplash.com/photo-1579224422204-032c3f15c1e5?q=80&w=600&auto=format&fit=crop" alt="MTB Trail" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                </div>
                <div class="group relative overflow-hidden rounded-lg shadow-md aspect-square bg-gray-200">
                    <img src="https://images.unsplash.com/photo-1534777367038-9404f45b869a?q=80&w=600&auto=format&fit=crop" alt="Cycling Group" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                </div>
                <div class="group relative overflow-hidden rounded-lg shadow-md aspect-square bg-gray-200">
                    <img src="https://images.unsplash.com/photo-1507034589631-9433cc6bc453?q=80&w=600&auto=format&fit=crop" alt="Mountain Bike" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                </div>
                <div class="group relative overflow-hidden rounded-lg shadow-md aspect-square bg-gray-200">
                    <img src="https://images.unsplash.com/photo-1521360098595-5ee3a8542da6?q=80&w=600&auto=format&fit=crop" alt="Bike Wheel" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                </div>
                <div class="group relative overflow-hidden rounded-lg shadow-md aspect-square bg-gray-200">
                    <img src="https://images.unsplash.com/photo-1596706939989-d9d1502476d0?q=80&w=600&auto=format&fit=crop" alt="Cyclist Sunset" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                </div>
                <div class="group relative overflow-hidden rounded-lg shadow-md aspect-square bg-gray-200">
                    <img src="https://images.unsplash.com/photo-1541336032412-2048a678540d?q=80&w=600&auto=format&fit=crop" alt="Mountain Path" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                </div>
            </div>
        </div>
    </section>

"""

# 3. HTML for Volunteering Section
voluntariado_html = """
    <!-- Sección de Voluntariado -->
    <section id="voluntariado" class="py-20 bg-gray-50 relative overflow-hidden">
        <div class="absolute inset-0 opacity-10" style="background-image: url('https://www.transparenttextures.com/patterns/cubes.png');"></div>
        <div class="container mx-auto px-6 relative z-10">
            <div class="flex flex-col md:flex-row items-center bg-white rounded-2xl shadow-xl overflow-hidden">
                <div class="w-full md:w-1/2 h-64 md:h-auto relative">
                    <img src="https://images.unsplash.com/photo-1559027615-cd4628902d4a?q=80&w=1000&auto=format&fit=crop" alt="Voluntarios" class="absolute inset-0 w-full h-full object-cover">
                    <div class="absolute inset-0 bg-secondary bg-opacity-30"></div>
                </div>
                <div class="w-full md:w-1/2 p-10 md:p-16">
                    <span class="text-primary font-bold tracking-widest uppercase text-sm mb-2 block">Únete al Equipo</span>
                    <h2 class="text-3xl md:text-4xl font-bold text-secondary mb-6">Sé Voluntario en la FIC 2026</h2>
                    <p class="text-gray-600 mb-6 text-lg">
                        El éxito de la Ciclovía del Maíz depende en gran medida de personas apasionadas como tú. Vive la competencia desde adentro, conoce a ciclistas de todo el mundo y sé parte de la organización del evento deportivo más grande del Valle Sagrado.
                    </p>
                    <ul class="space-y-3 mb-8">
                        <li class="flex items-center text-gray-700">
                            <i class="ri-checkbox-circle-fill text-primary text-xl mr-3"></i> Certificado de participación oficial
                        </li>
                        <li class="flex items-center text-gray-700">
                            <i class="ri-checkbox-circle-fill text-primary text-xl mr-3"></i> Kit exclusivo de staff (Polo y gorra)
                        </li>
                        <li class="flex items-center text-gray-700">
                            <i class="ri-checkbox-circle-fill text-primary text-xl mr-3"></i> Alimentación durante los días del evento
                        </li>
                    </ul>
                    <a href="https://wa.me/51994381708?text=Hola,%20quiero%20ser%20voluntario%20en%20la%20FIC%202026" target="_blank" class="inline-block bg-secondary hover:bg-opacity-90 text-white font-bold py-3 px-8 rounded-full shadow-lg transition-transform transform hover:scale-105">
                        Postular por WhatsApp <i class="ri-whatsapp-line ml-2"></i>
                    </a>
                </div>
            </div>
        </div>
    </section>
"""

# Inject before inscripcion
content = content.replace('<section id="inscripcion"', gallery_html + voluntariado_html + '\n<section id="inscripcion"')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Gallery and Volunteering sections added.")
