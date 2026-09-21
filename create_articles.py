import os
import re

# Template for the articles
article_template = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - FIC 2026 Blog</title>
    <script src="https://cdn.tailwindcss.com/3.4.16"></script>
    <script>
        tailwind.config={{
            theme:{{
                extend:{{
                    colors:{{
                        primary:'#E67E22',
                        secondary:'#2C3E50',
                        accent:'#F39C12'
                    }}
                }}
            }}
        }}
    </script>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/remixicon@4.5.0/fonts/remixicon.css" rel="stylesheet">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🚴</text></svg>">
    <style>
        body {{ font-family: 'Open Sans', sans-serif; }}
        h1, h2, h3, h4, h5, h6, .font-montserrat {{ font-family: 'Montserrat', sans-serif; }}
    </style>
</head>
<body class="bg-gray-50 flex flex-col min-h-screen">

    <!-- Header / Navbar -->
    <header class="bg-gray-900 text-white shadow-md sticky top-0 z-50">
        <nav class="container mx-auto px-6 py-4 flex justify-between items-center">
            <div class="flex items-center">
                <a href="index.html" class="text-white text-2xl font-bold">FIC 2026</a>
            </div>
            <div class="hidden md:flex space-x-8 text-white font-bold">
                <a href="index.html" class="hover:text-primary transition-colors">Inicio</a>
                <a href="blog.html" class="text-primary hover:text-white transition-colors">Volver al Blog</a>
            </div>
            <div class="md:hidden">
                <a href="blog.html" class="text-white hover:text-primary"><i class="ri-arrow-left-line ri-lg mr-1"></i> Blog</a>
            </div>
        </nav>
    </header>

    <!-- Post Content -->
    <main class="flex-grow container mx-auto px-4 py-12 max-w-4xl">
        <!-- Breadcrumb -->
        <div class="text-sm text-gray-500 mb-6 font-bold">
            <a href="index.html" class="hover:text-primary">Inicio</a> <i class="ri-arrow-right-s-line mx-1"></i>
            <a href="blog.html" class="hover:text-primary">Blog</a> <i class="ri-arrow-right-s-line mx-1"></i>
            <span class="text-gray-800">{category}</span>
        </div>

        <!-- Article Header -->
        <header class="mb-10 text-center">
            <span class="text-primary font-bold tracking-widest uppercase text-sm mb-3 block">{category}</span>
            <h1 class="text-4xl md:text-5xl font-extrabold text-secondary mb-6 leading-tight">{title}</h1>
            <div class="flex items-center justify-center text-gray-500 text-sm">
                <i class="ri-calendar-line mr-2"></i> 20 Noviembre, 2026
                <span class="mx-3">|</span>
                <i class="ri-user-line mr-2"></i> Por Equipo Ayni Sport
            </div>
        </header>

        <!-- Featured Image -->
        <div class="rounded-xl overflow-hidden shadow-lg mb-12">
            <img src="{image_url}" alt="Imagen del artculo" class="w-full h-auto max-h-[500px] object-cover">
        </div>

        <!-- Article Body -->
        <article class="prose prose-lg max-w-none text-gray-700 space-y-6 leading-relaxed">
            {content}
        </article>
        
        <!-- Tags -->
        <div class="mt-12 pt-6 border-t border-gray-200 flex flex-wrap gap-2">
            <span class="bg-gray-200 text-gray-700 px-3 py-1 rounded-full text-sm font-bold">Ciclismo</span>
            <span class="bg-gray-200 text-gray-700 px-3 py-1 rounded-full text-sm font-bold">Valle Sagrado</span>
            <span class="bg-gray-200 text-gray-700 px-3 py-1 rounded-full text-sm font-bold">FIC 2026</span>
        </div>

        <!-- Call to action -->
        <div class="mt-12 bg-gray-900 text-white p-8 rounded-xl text-center shadow-xl">
            <h3 class="text-2xl font-bold mb-4">Listo para la aventura?</h3>
            <p class="mb-6 text-gray-300">nete a cientos de ciclistas y vive la experiencia de la Ciclova del Maz.</p>
            <a href="index.html#inscripcion" class="inline-block bg-primary hover:bg-orange-600 text-white font-bold py-3 px-8 rounded-full transition-colors text-lg">
                Inscrbete ahora
            </a>
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white py-8 mt-12">
        <div class="container mx-auto px-6 text-center">
            <p>&copy; 2026 Ciclova del Maz. Todos los derechos reservados.</p>
        </div>
    </footer>
</body>
</html>
"""

# ARTICLE 1
art1_title = "El impacto ecológico, económico y cultural de la FIC en el Valle Sagrado"
art1_cat = "Comunidad"
art1_img = "https://images.unsplash.com/photo-1544181093-c712c9a1d131?q=80&w=1200&auto=format&fit=crop"
art1_content = """
<p class="text-xl font-semibold text-gray-800">El Festival Internacional de Ciclismo (FIC) "Ciclovía del Maíz" va mucho más allá de ser una simple competencia deportiva. Organizado por <b>Ayni Sport S.A.C.</b>, el festival es un motor de desarrollo sostenible para las comunidades locales del Valle Sagrado de los Incas.</p>

<h2 class="text-2xl font-bold text-secondary mt-8 mb-4">Un impulso a la economía local</h2>
<p>Con cientos de participantes nacionales e internacionales visitando el Cusco y el Valle Sagrado, la FIC 2026 inyecta dinamismo directamente a las economías locales. Desde el nuevo tramo que abarca <b>Taray hasta Ollantaytambo</b>, los ciclistas interactúan con hospedajes comunitarios, restaurantes tradicionales, artesanos y productores de maíz.</p>
<p>El evento promueve un turismo responsable donde cada pedalada se traduce en ingresos directos para las familias andinas. Los alojamientos en Ollantaytambo y Urubamba logran su ocupación máxima, generando oportunidades de trabajo temporal y exposición global.</p>

<h2 class="text-2xl font-bold text-secondary mt-8 mb-4">Revalorizando la cultura del Maíz</h2>
<p>Como su nombre lo indica, la "Ciclovía del Maíz" rinde homenaje al sagrado cultivo inca: el maíz blanco gigante. Durante el festival, los ciclistas y sus acompañantes tienen la oportunidad de probar la gastronomía basada en este insumo ancestral, conocer sus procesos de cultivo, e incluso presenciar ceremonias tradicionales de agradecimiento a la Pachamama (Madre Tierra).</p>
<p>Este intercambio cultural fortalece la identidad de las comunidades, enseñando a los visitantes que el recorrido que están realizando no es solo un circuito de tierra, sino una vía histórica que alimentó a todo un imperio.</p>

<h2 class="text-2xl font-bold text-secondary mt-8 mb-4">Compromiso Ecológico</h2>
<p>La preservación del Valle Sagrado es nuestra máxima prioridad. La organización ha establecido estrictas reglas de "Cero Rastro" para todos los competidores. Además, parte de las inscripciones se destinan a campañas de limpieza y reforestación de la ribera del río Vilcanota, asegurando que el deporte coexista en perfecta armonía con el ecosistema de la región.</p>
"""

# ARTICLE 2
art2_title = "Ruta Taray - Ollantaytambo: Una travesía épica en la FIC 2026"
art2_cat = "La Ruta"
art2_img = "https://images.unsplash.com/photo-1511994298241-608e28f14fde?q=80&w=1200&auto=format&fit=crop"
art2_content = """
<p class="text-xl font-semibold text-gray-800">Para la edición 2026, el Festival Internacional de Ciclismo presenta una ruta renovada, exigente e inigualable. Atrás quedó el circuito anterior; este año, el desafío se extiende por la imponente ruta desde <b>Taray hasta Ollantaytambo</b>.</p>

<h2 class="text-2xl font-bold text-secondary mt-8 mb-4">El nuevo desafío: Taray</h2>
<p>El punto de partida de la competencia se traslada al hermoso y tranquilo distrito de Taray. Famoso por sus impresionantes andenes y su tranquilidad junto al río Vilcanota, Taray servirá como escenario para el calentamiento y la partida oficial. Los corredores experimentarán los primeros kilómetros sobre terrenos mixtos de tierra compacta y ascensos moderados, perfectos para medir fuerzas antes del tramo principal.</p>

<h2 class="text-2xl font-bold text-secondary mt-8 mb-4">Navegando por el Valle Sagrado</h2>
<p>A medida que la ruta avanza hacia Pisac, Calca y Urubamba, el nivel técnico se incrementa. Los competidores de Cross Country Maratón (XCM) deberán enfrentarse a subidas técnicas, descensos rápidos y cruces de pequeños arroyos. Todo esto bajo la mirada de los nevados andinos y las antiguas ruinas que vigilan el valle desde lo alto.</p>

<h2 class="text-2xl font-bold text-secondary mt-8 mb-4">La gloriosa meta: Ollantaytambo</h2>
<p>El esfuerzo supremo se coronará en la mítica fortaleza de Ollantaytambo, la "Ciudad Inca Viviente". El tramo final exigirá a los ciclistas darlo todo en un sprint a través de senderos empedrados que datan de la época imperial.</p>
<p>Cruzar la meta en Ollantaytambo no solo será un logro físico, sino emocional. Allí los esperará el calor de la comunidad, música tradicional, y por supuesto, el inicio de un festival de cierre que quedará en la memoria de cada participante.</p>

<p class="font-bold text-gray-800 mt-6">¡Prepara tu bicicleta, afina tus pulmones para la altura y prepárate para conquistar la ruta Taray - Ollantaytambo en la FIC 2026!</p>
"""

with open("impacto-cultural-economico.html", "w", encoding="utf-8") as f:
    f.write(article_template.format(title=art1_title, category=art1_cat, image_url=art1_img, content=art1_content))

with open("preparacion-ruta-taray.html", "w", encoding="utf-8") as f:
    f.write(article_template.format(title=art2_title, category=art2_cat, image_url=art2_img, content=art2_content))

# Update blog.html to point to these new articles
with open("blog.html", "r", encoding="utf-8") as f:
    blog_content = f.read()

# Replace Article 1
old_art1 = r'<article[^>]*>.*?<span[^>]*>Noticias</span>.*?<h3[^>]*>.*?Lanzamiento Oficial de la FIC 2026.*?</a></h3>.*?</article>'
new_art1 = """<article class="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition-shadow duration-300">
    <img src="https://images.unsplash.com/photo-1544181093-c712c9a1d131?q=80&w=800&auto=format&fit=crop" alt="Impacto FIC" class="w-full h-48 object-cover">
    <div class="p-6">
        <span class="text-primary font-bold text-sm uppercase tracking-wide">Comunidad</span>
        <h3 class="text-xl font-bold mt-2 mb-3"><a href="impacto-cultural-economico.html" class="hover:text-primary">El impacto ecológico, económico y cultural de la FIC</a></h3>
        <p class="text-gray-600 mb-4 line-clamp-3">El Festival Internacional de Ciclismo va mucho más allá del deporte, impulsando el desarrollo sostenible en todo el Valle Sagrado.</p>
        <a href="impacto-cultural-economico.html" class="text-secondary font-bold hover:text-primary flex items-center">
            Leer más <i class="ri-arrow-right-line ml-2"></i>
        </a>
    </div>
</article>"""
blog_content = re.sub(old_art1, new_art1, blog_content, flags=re.DOTALL)

# Replace Article 2
old_art2 = r'<article[^>]*>.*?<span[^>]*>Entrenamiento</span>.*?<h3[^>]*>.*?Cmo prepararte para la altura del Valle Sagrado.*?</a></h3>.*?</article>'
# Due to encoding issues in regex, we'll just replace the whole section manually by finding the start and end.
# Actually, re.sub with DOTALL is fine if we use wildcards.
old_art2_robust = r'<article[^>]*>.*?<span[^>]*>Entrenamiento</span>.*?<h3[^>]*>.*?Valle Sagrado.*?</a></h3>.*?</article>'
new_art2 = """<article class="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition-shadow duration-300">
    <img src="https://images.unsplash.com/photo-1511994298241-608e28f14fde?q=80&w=800&auto=format&fit=crop" alt="Ruta Taray" class="w-full h-48 object-cover">
    <div class="p-6">
        <span class="text-primary font-bold text-sm uppercase tracking-wide">La Ruta</span>
        <h3 class="text-xl font-bold mt-2 mb-3"><a href="preparacion-ruta-taray.html" class="hover:text-primary">Ruta Taray - Ollantaytambo: Una travesía épica</a></h3>
        <p class="text-gray-600 mb-4 line-clamp-3">Para la edición 2026, presentamos una ruta renovada. Descubre los desafíos desde Taray hasta la gloriosa meta en Ollantaytambo.</p>
        <a href="preparacion-ruta-taray.html" class="text-secondary font-bold hover:text-primary flex items-center">
            Leer más <i class="ri-arrow-right-line ml-2"></i>
        </a>
    </div>
</article>"""
blog_content = re.sub(old_art2_robust, new_art2, blog_content, flags=re.DOTALL)

# Write back
with open("blog.html", "w", encoding="utf-8") as f:
    f.write(blog_content)

print("Blog updated with new articles.")
