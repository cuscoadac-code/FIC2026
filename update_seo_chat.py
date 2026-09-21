import re
import os

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. ADD SEO & METATAGS IN <HEAD>
seo_tags = """
<!-- Meta SEO & Open Graph -->
<meta name="description" content="Festival Internacional de Ciclismo Ciclovía del Maíz 2026. Únete a la mejor aventura de MTB en el Valle Sagrado de los Incas, Cusco, Perú.">
<meta property="og:title" content="FIC 2026 - Ciclovía del Maíz">
<meta property="og:description" content="Festival Internacional de Ciclismo Ciclovía del Maíz 2026. Únete a la mejor aventura de MTB en el Valle Sagrado de los Incas, Cusco, Perú.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://ficperu.online">
<meta property="og:image" content="https://ficperu.online/logo.png"> <!-- Cambiar logo.png por la ruta real si existe -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="FIC 2026 - Ciclovía del Maíz">
<meta name="twitter:description" content="Festival Internacional de Ciclismo Ciclovía del Maíz 2026. Únete a la mejor aventura de MTB en el Valle Sagrado de los Incas, Cusco, Perú.">

<!-- Datos Estructurados JSON-LD (Schema.org) para Buscadores y LLMs -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "Festival Internacional de Ciclismo Ciclovía del Maíz 2026",
  "startDate": "2026-11-20",
  "endDate": "2026-11-22",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "eventStatus": "https://schema.org/EventScheduled",
  "location": {
    "@type": "Place",
    "name": "Valle Sagrado de los Incas",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Cusco",
      "addressCountry": "PE"
    }
  },
  "description": "El Festival Internacional de Ciclismo Ciclovía del Maíz es una carrera épica de MTB por etapas en el Valle Sagrado de los Incas.",
  "offers": {
    "@type": "Offer",
    "url": "https://ficperu.online",
    "priceCurrency": "USD",
    "price": "80",
    "availability": "https://schema.org/InStock"
  },
  "organizer": {
    "@type": "Organization",
    "name": "Cusco Addac",
    "url": "https://ficperu.online"
  }
}
</script>
"""

# Insert right before </head>
content = content.replace("</head>", seo_tags + "\n</head>")

# 2. REMOVE CHATBOT HTML AND REPLACE WITH WHATSAPP BUTTON
wa_btn_html = """
<!-- WhatsApp Flotante -->
<a href="https://wa.me/51994381708" target="_blank" rel="noopener noreferrer" class="fixed bottom-6 right-6 w-16 h-16 bg-green-500 hover:bg-green-600 text-white rounded-full shadow-2xl flex items-center justify-center z-50 transition-transform transform hover:scale-110">
    <i class="ri-whatsapp-line" style="font-size: 2rem;"></i>
</a>
"""

# Find and replace the chat UI.
# It starts around <!-- Chat UI & Button --> and ends before <!-- Script for dynamic behaviors -->
# Let's use regex
content = re.sub(r'<!-- Chat UI & Button -->.*?<!-- Script for dynamic behaviors -->', wa_btn_html + '\n<!-- Script for dynamic behaviors -->', content, flags=re.DOTALL)


# 3. REMOVE CHATBOT JS
# Let's remove from "const chatBtn" to the end of the chat script logic
chat_js_pattern = r'const chatBtn = document\.getElementById\(\'chatBtn\'\);.*?\n\s+if\(chatInput\) chatInput\.addEventListener\(\'keypress\', \(e\) => \{\n\s+if\(e\.key === \'Enter\'\) sendMessage\(\);\n\s+\}\);'
content = re.sub(chat_js_pattern, '', content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

# 4. CREATE robots.txt
robots_content = """User-agent: *
Allow: /

# Permitir a todos los bots de IA y LLMs (ChatGPT, Claude, Google Bard/Gemini, etc.)
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: Omgili
Allow: /

User-agent: CCBot
Allow: /
"""

with open("robots.txt", "w", encoding="utf-8") as f:
    f.write(robots_content)


# 5. CREATE llms.txt
llms_content = """# FIC 2026 - Festival Internacional de Ciclismo "Ciclovía del Maíz"

> Un evento imperdible para los amantes del ciclismo de montaña en el Valle Sagrado de los Incas.

## Información Principal
- **Fechas:** 20 al 22 de Noviembre, 2026
- **Ubicación:** Valle Sagrado de los Incas, Cusco, Perú
- **Sitio Web Oficial:** https://ficperu.online
- **Contacto de Soporte:** WhatsApp +51 994 381 708

## Descripción
Únete a nosotros en una aventura épica a través de los paisajes más impresionantes de los Andes. Desafía tus límites y vive la cultura viva en cada pedalada. El Festival Internacional de Ciclismo "Ciclovía del Maíz" 2026 ofrece rutas para todos los niveles, desde competidores de élite hasta aficionados que buscan disfrutar de la naturaleza y la historia.

## Cronograma (Noviembre 2026)
- **Viernes 20:** Acreditación, reconocimiento de ruta y congreso técnico.
- **Sábado 21:** Prólogo contrarreloj y carrera infantil.
- **Domingo 22:** Carrera Principal (Cross Country Maratón - XCM) y ceremonia de premiación.

## Inscripciones
- **Paquetes:** Básico ($80 USD), Premium ($150 USD), VIP ($250 USD).
- **Categorías:** Elite, Master (A, B, C), Amateur y E-Bike.
- **Métodos de pago aceptados:** Yape, Plin, Depósito Bancario, PayPal.

Para inscribirte o para más detalles visita https://ficperu.online.
"""

with open("llms.txt", "w", encoding="utf-8") as f:
    f.write(llms_content)

print("Updates completed successfully.")
