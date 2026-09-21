import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Insert Payment HTML before terms checkbox
payment_html = """
<div class="mb-6">
<label class="block text-gray-700 mb-2">Método de Pago</label>
<div class="space-y-2 mb-4">
<label class="flex items-center">
<input type="radio" name="metodo_pago" value="Yape" class="custom-checkbox" onchange="togglePaymentInfo()" checked>
<span class="ml-2">Yape</span>
</label>
<label class="flex items-center">
<input type="radio" name="metodo_pago" value="Plin" class="custom-checkbox" onchange="togglePaymentInfo()">
<span class="ml-2">Plin</span>
</label>
<label class="flex items-center">
<input type="radio" name="metodo_pago" value="Depósito Bancario" class="custom-checkbox" onchange="togglePaymentInfo()">
<span class="ml-2">Depósito Bancario</span>
</label>
<label class="flex items-center">
<input type="radio" name="metodo_pago" value="PayPal" class="custom-checkbox" onchange="togglePaymentInfo()">
<span class="ml-2">PayPal</span>
</label>
</div>

<div id="pago-yape-plin" class="bg-gray-100 p-4 rounded mb-4">
<p class="text-sm font-bold mb-2">Instrucciones:</p>
<p class="text-sm">Envía el monto al número: <span class="font-bold text-primary">999 999 999</span> (A nombre de Cusco Addac).</p>
<p class="text-sm mt-2">Luego, ingresa tu número de operación/referencia:</p>
<input type="text" id="num_operacion" class="w-full px-4 py-2 mt-2 border border-gray-300 rounded focus:outline-none focus:border-primary" placeholder="Ej. 12345678">
</div>

<div id="pago-deposito" class="bg-gray-100 p-4 rounded mb-4 hidden">
<p class="text-sm font-bold mb-2">Instrucciones (BCP / BBVA / Interbank):</p>
<p class="text-sm">Cuenta BCP Soles: <span class="font-bold">194-0000000-0-00</span></p>
<p class="text-sm">CCI: <span class="font-bold">002-194-0000000000-00</span></p>
<p class="text-sm mt-2">Ingresa tu número de operación bancaria:</p>
<input type="text" id="num_operacion_banco" class="w-full px-4 py-2 mt-2 border border-gray-300 rounded focus:outline-none focus:border-primary" placeholder="Ej. 098765">
</div>

<div id="pago-paypal" class="bg-gray-100 p-4 rounded mb-4 hidden">
<p class="text-sm">Haz clic en el siguiente enlace para pagar mediante PayPal y anota tu código de transacción aquí.</p>
<a href="https://paypal.me/cuscoaddac" target="_blank" class="text-primary font-bold hover:underline">paypal.me/cuscoaddac</a>
<input type="text" id="num_operacion_paypal" class="w-full px-4 py-2 mt-2 border border-gray-300 rounded focus:outline-none focus:border-primary" placeholder="Código de transacción (Ej. 3LX9... )">
</div>
</div>
"""

terms_checkbox = """<div class="mb-6">
<label class="flex items-center">
<input type="checkbox" class="custom-checkbox">
<span class="ml-2 text-sm">Acepto los términos y condiciones del evento</span>
</label>
</div>"""

content = content.replace(terms_checkbox, payment_html + terms_checkbox)

# 2. Add JS toggle togglePaymentInfo()
js_toggle = """
function togglePaymentInfo() {
    const metodo = document.querySelector('input[name="metodo_pago"]:checked').value;
    document.getElementById('pago-yape-plin').classList.add('hidden');
    document.getElementById('pago-deposito').classList.add('hidden');
    document.getElementById('pago-paypal').classList.add('hidden');
    
    if (metodo === 'Yape' || metodo === 'Plin') {
        document.getElementById('pago-yape-plin').classList.remove('hidden');
    } else if (metodo === 'Depósito Bancario') {
        document.getElementById('pago-deposito').classList.remove('hidden');
    } else if (metodo === 'PayPal') {
        document.getElementById('pago-paypal').classList.remove('hidden');
    }
}
"""

content = content.replace("function submitForm", js_toggle + "\nfunction submitForm")

# 3. Add to submitForm data collector
submit_data_js = """
        const pack = document.querySelector('input[name="paquete"]:checked');
        data.paquete = pack ? pack.nextElementSibling.textContent.trim() : '';
        
        const metodo = document.querySelector('input[name="metodo_pago"]:checked');
        data.metodo_pago = metodo ? metodo.value : '';
        if (data.metodo_pago === 'Yape' || data.metodo_pago === 'Plin') {
            data.operacion = document.getElementById('num_operacion').value;
        } else if (data.metodo_pago === 'Depósito Bancario') {
            data.operacion = document.getElementById('num_operacion_banco').value;
        } else if (data.metodo_pago === 'PayPal') {
            data.operacion = document.getElementById('num_operacion_paypal').value;
        }
"""

content = content.replace("""        const pack = document.querySelector('input[name="paquete"]:checked');
        data.paquete = pack ? pack.nextElementSibling.textContent.trim() : '';""", submit_data_js)

# 4. Modify Whatsapp Message
old_wa_msg = 'const mensaje = encodeURIComponent("Black prueba fuck al reservar de forma \nautnklaotca");'
# Wait, the current string in the file had a newline from formatting or something?
# Let's use re to replace it.
content = re.sub(r'const mensaje = encodeURIComponent\("Black prueba.*?\);', 'const mensaje = encodeURIComponent(`¡Hola! Me he inscrito en la Ciclovía del Maíz 2026.\\nNombre: ${data.nombre} ${data.apellido}\\nPaquete: ${data.paquete}\\nMétodo de pago: ${data.metodo_pago}\\nOperación: ${data.operacion}`);', content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Payment methods added.")
