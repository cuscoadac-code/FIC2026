import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove "Certificado médico..." and "Comprobante de seguro..." items
# They are typically inside a <li class="flex items-start"> ... </li>
# We can use a regex to match the <li> that contains the text.
pattern_certificado = r'<li class="flex items-start">[^<]*<div[^>]*>.*?<i class="ri-file-list-line"></i>.*?</div>\s*<span[^>]*>Certificado médico.*?</span>\s*</li>'
content = re.sub(pattern_certificado, '', content, flags=re.DOTALL)

pattern_seguro = r'<li class="flex items-start">[^<]*<div[^>]*>.*?<i class="ri-file-list-line"></i>.*?</div>\s*<span[^>]*>Comprobante de seguro.*?</span>\s*</li>'
content = re.sub(pattern_seguro, '', content, flags=re.DOTALL)

# 2. Modify Yape/Plin Instructions & Remove input field
old_yape_block_regex = r'<div id="pago-yape-plin" class="bg-gray-100 p-4 rounded mb-4">.*?</div>'
new_yape_block = """<div id="pago-yape-plin" class="bg-gray-100 p-4 rounded mb-4 border-l-4 border-purple-500">
<p class="text-sm font-bold mb-2 text-purple-700">Instrucciones Yape / Plin:</p>
<p class="text-sm text-gray-700">1. Envía el monto al número: <span class="font-bold text-lg text-gray-900">993 022 225</span> <br><span class="text-xs text-gray-500">(A nombre de Ayni Sport S.A.C.)</span></p>
<p class="text-sm text-gray-700 mt-2">2. Presiona el botón <b>"Inscribirse y Pagar"</b> para abrir WhatsApp.</p>
<p class="text-sm text-gray-700 mt-2">3. <b>Adjunta la captura de pantalla</b> de tu pago directamente en el chat.</p>
<!-- No input for num_operacion needed -->
</div>"""
content = re.sub(old_yape_block_regex, new_yape_block, content, flags=re.DOTALL)

# Also fix the Javascript so it doesn't look for `num_operacion`
js_fix_old = """if (data.metodo_pago === 'Yape' || data.metodo_pago === 'Plin') {
            data.operacion = document.getElementById('num_operacion').value;
        }"""
js_fix_new = """if (data.metodo_pago === 'Yape' || data.metodo_pago === 'Plin') {
            data.operacion = 'Captura enviada por WhatsApp';
        }"""
content = content.replace(js_fix_old, js_fix_new)

# Clean up WhatsApp text to remove "Operación: Captura enviada por WhatsApp" if we want, or leave it. 
# Leaving it is fine: "Operación: Captura enviada por WhatsApp" is clear.

# 3. Payment Icons (Visa/Mastercard -> Yape/Plin)
# Replace the Visa div
visa_pattern = r'<div class="flex items-center bg-white px-3 py-2 rounded">\s*<div class="w-6 h-6 flex items-center justify-center mr-2">\s*<i class="ri-visa-fill text-blue-700"></i>\s*</div>\s*<span class="text-sm">Visa</span>\s*</div>'
yape_div = """<div class="flex items-center bg-white px-3 py-2 rounded border border-gray-200">
<div class="w-6 h-6 flex items-center justify-center mr-2 bg-purple-600 text-white rounded font-bold text-xs">Y</div>
<span class="text-sm font-bold text-purple-600">Yape</span>
</div>"""
content = re.sub(visa_pattern, yape_div, content, flags=re.DOTALL)

# Replace the Mastercard div
mastercard_pattern = r'<div class="flex items-center bg-white px-3 py-2 rounded">\s*<div class="w-6 h-6 flex items-center justify-center mr-2">\s*<i class="ri-mastercard-fill text-red-600"></i>\s*</div>\s*<span class="text-sm">Mastercard</span>\s*</div>'
plin_div = """<div class="flex items-center bg-white px-3 py-2 rounded border border-gray-200">
<div class="w-6 h-6 flex items-center justify-center mr-2 bg-blue-500 text-white rounded font-bold text-xs">P</div>
<span class="text-sm font-bold text-blue-500">Plin</span>
</div>"""
content = re.sub(mastercard_pattern, plin_div, content, flags=re.DOTALL)


# 4. Change "Fotos Históricas" to "Galería de Fotos"
content = content.replace("Fotos Históricas", "Galería de Fotos")
# Just in case there are accents issues
content = content.replace("Fotos Histricas", "Galería de Fotos")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Form updates, gallery title, and icons fixed.")
