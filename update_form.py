import os

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update the Yape/Plin phone number in the HTML instructions
content = content.replace("Envía el monto al número: <span class=\"font-bold text-primary\">999 999 999</span>",
                          "Envía el monto al número: <span class=\"font-bold text-primary\">993 022 225</span>")

# 2. Update the WhatsApp message text
old_msg = """const mensaje = encodeURIComponent(`¡Hola! Me he inscrito en la Ciclovía del Maíz 2026.
Nombre: ${data.nombre} ${data.apellido}
Paquete: ${data.paquete}
Método de pago: ${data.metodo_pago}
Operación: ${data.operacion}`);"""

new_msg = """const mensaje = encodeURIComponent(`¡Hola! Me he inscrito en la Ciclovía del Maíz 2026.
Nombre: ${data.nombre} ${data.apellido}
Paquete: ${data.paquete}
Método de pago: ${data.metodo_pago}
Operación: ${data.operacion}

*Por favor adjunta aquí la foto/captura de pantalla de tu voucher o Yape para validar tu inscripción.*`);"""

content = content.replace(old_msg, new_msg)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Form instructions and WhatsApp message updated.")
