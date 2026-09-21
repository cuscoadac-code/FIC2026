import glob
import re

cookie_html = """
    <!-- Cookie Banner (Inspirado en Cookiebot) -->
    <div id="cookie-banner" class="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 shadow-2xl z-[100] transform transition-transform duration-500 translate-y-full" style="display: none;">
        <div class="container mx-auto px-4 py-6 max-w-7xl relative">
            <!-- Close Button -->
            <button id="cookie-close" class="absolute top-4 right-4 text-gray-500 hover:text-gray-800 focus:outline-none">
                <i class="ri-close-line text-2xl"></i>
            </button>
            
            <div class="flex flex-col lg:flex-row gap-6 items-center lg:items-start">
                
                <!-- Logos (Opcional, lado izquierdo) -->
                <div class="hidden lg:flex flex-col items-center justify-center w-32 shrink-0 border-r border-gray-200 pr-6">
                    <div class="text-primary font-black text-xl leading-none text-center mb-4">FIC<br>2026</div>
                    <div class="text-[10px] text-gray-400 font-bold tracking-widest uppercase text-center">Privacidad</div>
                </div>

                <!-- Text Content -->
                <div class="flex-1">
                    <h3 class="font-bold text-gray-900 text-lg mb-2">Este sitio web utiliza cookies.</h3>
                    <p class="text-sm text-gray-600 leading-relaxed mb-3">
                        Este sitio web almacena cookies en su ordenador. Estas cookies se utilizan para mejorar el sitio web y ofrecerle servicios más personalizados, tanto en este sitio como a través de otros medios. Para obtener más información sobre las cookies que utilizamos, consulte nuestra <a href="#" class="text-red-500 hover:underline">Política de cookies</a>.
                    </p>
                    <button class="text-red-500 text-sm font-bold flex items-center hover:underline focus:outline-none">
                        Mostrar detalles <i class="ri-arrow-right-s-line ml-1"></i>
                    </button>
                </div>

                <!-- Buttons -->
                <div class="flex flex-col gap-2 w-full lg:w-64 shrink-0 mt-4 lg:mt-0">
                    <button id="cookie-accept-all" class="w-full bg-gray-400 hover:bg-gray-500 text-white font-bold py-2 px-4 text-sm transition-colors">
                        Permitir todas las cookies
                    </button>
                    <button class="w-full bg-white border border-gray-300 hover:bg-gray-50 text-gray-700 font-bold py-2 px-4 text-sm flex justify-between items-center transition-colors">
                        Personalizar <i class="ri-arrow-right-s-line text-gray-400"></i>
                    </button>
                    <button id="cookie-accept-necessary" class="w-full bg-white border border-gray-300 hover:bg-gray-50 text-gray-700 font-bold py-2 px-4 text-sm transition-colors text-center leading-tight">
                        Utilizar únicamente las cookies necesarias.
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- Cookie JS Logic -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const banner = document.getElementById('cookie-banner');
            const acceptAllBtn = document.getElementById('cookie-accept-all');
            const acceptNecBtn = document.getElementById('cookie-accept-necessary');
            const closeBtn = document.getElementById('cookie-close');

            // Check localStorage
            if (!localStorage.getItem('fic_cookies_accepted')) {
                // Show banner after short delay
                banner.style.display = 'block';
                setTimeout(() => {
                    banner.classList.remove('translate-y-full');
                }, 500);
            }

            function hideBanner() {
                banner.classList.add('translate-y-full');
                setTimeout(() => {
                    banner.style.display = 'none';
                }, 500);
            }

            function acceptCookies() {
                localStorage.setItem('fic_cookies_accepted', 'true');
                hideBanner();
            }

            acceptAllBtn.addEventListener('click', acceptCookies);
            acceptNecBtn.addEventListener('click', acceptCookies);
            closeBtn.addEventListener('click', hideBanner);
        });
    </script>
"""

# Apply to all main HTML files
files_to_update = ["index.html", "blog.html", "noticia-ejemplo.html", "resultados.html"]

for file_path in files_to_update:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if already has cookie banner
    if 'id="cookie-banner"' in content:
        continue
        
    # Inject right before </body>
    if '</body>' in content:
        content = content.replace('</body>', cookie_html + '\n</body>')
    else:
        content += cookie_html
        
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Cookie banner injected into all pages.")
