import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove specific list items manually or with non-greedy tight regex
# Looking for `<li class="flex items-start"> ... <span>Certificado médico...</span> </li>`
# We can just match <li ... to </li> where there are no other <li> inside
pattern_certificado = r'<li class="flex items-start">(?:(?!<li).)*?Certificado m(?:é|)dico.*?(?:</li>)'
content = re.sub(pattern_certificado, '', content, flags=re.DOTALL | re.IGNORECASE)

pattern_seguro = r'<li class="flex items-start">(?:(?!<li).)*?Comprobante de seguro.*?(?:</li>)'
content = re.sub(pattern_seguro, '', content, flags=re.DOTALL | re.IGNORECASE)


# 2. Modify Yape/Plin Instructions & Remove input field
old_yape_block_regex = r'<div id="pago-yape-plin"[^>]*>.*?</div>'
# We have to be careful with .*?</div>. It might stop at the first inner </div> or consume too much if there are nested divs.
# The original block is:
# <div id="pago-yape-plin" class="bg-gray-100 p-4 rounded mb-4">
# <p class="text-sm font-bold mb-2">Instrucciones:</p>
# <p class="text-sm">Envía el monto al número: <span class="font-bold text-primary">993 022 225</span> (A nombre de Cusco Addac).</p>
# <input type="text" id="num_operacion" class="w-full px-4 py-2 mt-2 border border-gray-300 rounded focus:outline-none focus:border-primary" placeholder="Número de operación/referencia">
# </div>

yape_start = content.find('<div id="pago-yape-plin"')
if yape_start != -1:
    yape_end = content.find('</div>', yape_start) + 6
    if content.find('<input', yape_start, yape_end) != -1: # Ensure we didn't miss nested divs. Actually there's no nested div in this block
        new_yape_block = """<div id="pago-yape-plin" class="bg-gray-100 p-4 rounded mb-4 border-l-4 border-purple-500">
<p class="text-sm font-bold mb-2 text-purple-700">Instrucciones Yape / Plin:</p>
<p class="text-sm text-gray-700">1. Envía el monto al número: <span class="font-bold text-lg text-gray-900">993 022 225</span> <br><span class="text-xs text-gray-500">(A nombre de Ayni Sport S.A.C.)</span></p>
<p class="text-sm text-gray-700 mt-2">2. Presiona el botón <b>"Inscribirse y Pagar"</b> para abrir WhatsApp.</p>
<p class="text-sm text-gray-700 mt-2">3. <b>Adjunta la captura de pantalla</b> de tu pago directamente en el chat.</p>
</div>"""
        content = content[:yape_start] + new_yape_block + content[yape_end:]


# Fix JS
js_fix_old = """if (data.metodo_pago === 'Yape' || data.metodo_pago === 'Plin') {
            data.operacion = document.getElementById('num_operacion').value;
        }"""
js_fix_new = """if (data.metodo_pago === 'Yape' || data.metodo_pago === 'Plin') {
            data.operacion = 'Captura enviada por WhatsApp';
        }"""
content = content.replace(js_fix_old, js_fix_new)


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
content = content.replace("Fotos Histricas", "Galería de Fotos") # if corrupted
content = content.replace("Fotos Histricas", "Galería de Fotos")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Form updates, gallery title, and icons fixed.")
