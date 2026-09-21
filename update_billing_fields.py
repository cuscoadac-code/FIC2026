import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Make email required
content = content.replace('<input type="email" id="email" class="w-full px-4 py-2 border border-gray-300 rounded \nfocus:outline-none focus:border-primary">', 
                          '<input type="email" id="email" required class="w-full px-4 py-2 border border-gray-300 rounded \nfocus:outline-none focus:border-primary">')
content = content.replace('<input type="email" id="email" class="w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:border-primary">', 
                          '<input type="email" id="email" required class="w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:border-primary">')

# Add Billing fields right after Email
billing_fields = """
<div class="mb-6 bg-gray-50 p-4 rounded-lg border border-gray-200">
    <h4 class="font-bold text-gray-800 mb-4">Datos de Facturación (Ayni Sport S.A.C.)</h4>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
        <div>
            <label class="block text-gray-700 mb-2 font-bold" for="tipo_comprobante">Tipo de Comprobante</label>
            <select id="tipo_comprobante" class="w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:border-primary" onchange="toggleFacturaFields()">
                <option value="Boleta">Boleta de Venta</option>
                <option value="Factura">Factura</option>
            </select>
        </div>
        <div>
            <label class="block text-gray-700 mb-2 font-bold" id="label_doc" for="documento">DNI / Pasaporte</label>
            <input type="text" id="documento" required class="w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:border-primary">
        </div>
    </div>
    
    <!-- Campos exclusivos para Factura -->
    <div id="campos_factura" class="hidden grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
            <label class="block text-gray-700 mb-2 font-bold" for="razon_social">Razón Social</label>
            <input type="text" id="razon_social" class="w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:border-primary">
        </div>
        <div>
            <label class="block text-gray-700 mb-2 font-bold" for="direccion_fiscal">Dirección Fiscal</label>
            <input type="text" id="direccion_fiscal" class="w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:border-primary">
        </div>
    </div>
</div>
"""

# Inject before the Country/Age row
country_row = '<div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">\n<div>\n<label class="block text-gray-700 mb-2" for="pais">País</label>'
if 'id="tipo_comprobante"' not in content:
    content = content.replace(country_row, billing_fields + '\n' + country_row)

# Add JS for toggling fields and updating WhatsApp message
js_logic = """
<script>
    function toggleFacturaFields() {
        const tipo = document.getElementById('tipo_comprobante').value;
        const camposFactura = document.getElementById('campos_factura');
        const labelDoc = document.getElementById('label_doc');
        const inputDoc = document.getElementById('documento');
        
        if (tipo === 'Factura') {
            camposFactura.classList.remove('hidden');
            labelDoc.textContent = 'RUC';
            inputDoc.placeholder = 'Ej. 20123456789';
        } else {
            camposFactura.classList.add('hidden');
            labelDoc.textContent = 'DNI / Pasaporte';
            inputDoc.placeholder = '';
        }
    }
</script>
"""
if 'toggleFacturaFields()' not in content:
    content = content.replace('</body>', js_logic + '\n</body>')

# Update submitForm logic to capture billing data
old_js_vars = """        data.edad = document.getElementById('edad').value;"""
new_js_vars = """        data.edad = document.getElementById('edad').value;
        data.tipo_comprobante = document.getElementById('tipo_comprobante').value;
        data.documento = document.getElementById('documento').value;
        data.razon_social = document.getElementById('razon_social').value;
"""
content = content.replace(old_js_vars, new_js_vars)

# Update the WhatsApp message text to include billing info
old_msg = """Método de pago: ${data.metodo_pago}
Operación: ${data.operacion}

*Por favor adjunta aquí la foto/captura de pantalla"""

new_msg = """Método de pago: ${data.metodo_pago}
Operación: ${data.operacion}
Comprobante: ${data.tipo_comprobante} (${data.documento}) ${data.tipo_comprobante === 'Factura' ? ' - ' + data.razon_social : ''}

*Por favor adjunta aquí la foto/captura de pantalla"""
content = content.replace(old_msg, new_msg)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
