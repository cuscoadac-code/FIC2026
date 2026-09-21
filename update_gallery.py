import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add "Galería" to nav menu
nav_item = '<a href="index.html#galeria" class="hover:text-primary transition-colors">Galería</a>\n<a href="blog.html"'
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
                <div class="relative pb-[56.25%] h-0 rounded-lg overflow-hidden shadow-lg">
                    <iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ" title="Video resumen FIC" class="absolute top-0 left-0 w-full h-full border-0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                </div>
                <div class="relative pb-[56.25%] h-0 rounded-lg overflow-hidden shadow-lg">
                    <iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ" title="Testimonios FIC" class="absolute top-0 left-0 w-full h-full border-0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                </div>
            </div>

            <!-- Fotos -->
            <h3 class="text-3xl font-bold text-secondary mb-8 border-b-2 border-primary pb-2 inline-block">Fotos Históricas</h3>
            <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                <div class="group relative overflow-hidden rounded-lg shadow-md aspect-square">
                    <img src="https://images.unsplash.com/photo-1544181093-c712c9a1d131?q=80&w=600&auto=format&fit=crop" alt="Ciclismo Cusco" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                    <div class="absolute inset-0 bg-black bg-opacity-40 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                        <i class="ri-search-eye-line text-white text-3xl"></i>
                    </div>
                </div>
                <div class="group relative overflow-hidden rounded-lg shadow-md aspect-square">
                    <img src="https://images.unsplash.com/photo-1511994298241-608e28f14fde?q=80&w=600&auto=format&fit=crop" alt="MTB Action" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                    <div class="absolute inset-0 bg-black bg-opacity-40 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                        <i class="ri-search-eye-line text-white text-3xl"></i>
                    </div>
                </div>
                <div class="group relative overflow-hidden rounded-lg shadow-md aspect-square">
                    <img src="https://images.unsplash.com/photo-1579224422204-032c3f15c1e5?q=80&w=600&auto=format&fit=crop" alt="MTB Trail" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                    <div class="absolute inset-0 bg-black bg-opacity-40 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                        <i class="ri-search-eye-line text-white text-3xl"></i>
                    </div>
                </div>
                <div class="group relative overflow-hidden rounded-lg shadow-md aspect-square">
                    <img src="https://images.unsplash.com/photo-1534777367038-9404f45b869a?q=80&w=600&auto=format&fit=crop" alt="Cycling Group" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                    <div class="absolute inset-0 bg-black bg-opacity-40 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                        <i class="ri-search-eye-line text-white text-3xl"></i>
                    </div>
                </div>
                <div class="group relative overflow-hidden rounded-lg shadow-md aspect-square">
                    <img src="https://images.unsplash.com/photo-1507034589631-9433cc6bc453?q=80&w=600&auto=format&fit=crop" alt="Mountain Bike" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                    <div class="absolute inset-0 bg-black bg-opacity-40 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                        <i class="ri-search-eye-line text-white text-3xl"></i>
                    </div>
                </div>
                <div class="group relative overflow-hidden rounded-lg shadow-md aspect-square">
                    <img src="https://images.unsplash.com/photo-1521360098595-5ee3a8542da6?q=80&w=600&auto=format&fit=crop" alt="Bike Wheel" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                    <div class="absolute inset-0 bg-black bg-opacity-40 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                        <i class="ri-search-eye-line text-white text-3xl"></i>
                    </div>
                </div>
                <div class="group relative overflow-hidden rounded-lg shadow-md aspect-square">
                    <img src="https://images.unsplash.com/photo-1596706939989-d9d1502476d0?q=80&w=600&auto=format&fit=crop" alt="Cyclist Sunset" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                    <div class="absolute inset-0 bg-black bg-opacity-40 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                        <i class="ri-search-eye-line text-white text-3xl"></i>
                    </div>
                </div>
                <div class="group relative overflow-hidden rounded-lg shadow-md aspect-square">
                    <img src="https://images.unsplash.com/photo-1541336032412-2048a678540d?q=80&w=600&auto=format&fit=crop" alt="Mountain Path" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                    <div class="absolute inset-0 bg-black bg-opacity-40 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                        <i class="ri-search-eye-line text-white text-3xl"></i>
                    </div>
                </div>
            </div>
            
            <div class="text-center mt-12">
                <a href="https://instagram.com" target="_blank" class="inline-flex items-center text-primary font-bold hover:text-secondary transition-colors text-lg">
                    Ver más fotos en nuestro Instagram <i class="ri-instagram-line ml-2 text-2xl"></i>
                </a>
            </div>
        </div>
    </section>

"""

# Inject before inscripcion
content = content.replace('<section id="inscripcion"', gallery_html + '<section id="inscripcion"')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Gallery section added.")
