from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import os

try:
    from supabase import create_client, Client
    import requests
except ImportError:
    print("Faltan dependencias. Asegúrate de ejecutar: pip install supabase requests")

# ================= CONFIGURACIÓN =================
# REEMPLAZA ESTAS VARIABLES CON TUS CREDENCIALES REALES DE SUPABASE
SUPABASE_URL = os.environ.get("SUPABASE_URL", "TU_SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "TU_SUPABASE_ANON_KEY")

# Configuración de API de WhatsApp (Ejemplo usando UltraMsg, Meta API o GreenAPI)
WHATSAPP_API_URL = "https://api.ultramsg.com/INSTANCE_ID/messages/chat"
WHATSAPP_API_TOKEN = "TU_ULTRAMSG_TOKEN"
WHATSAPP_TARGET_NUMBER = "+51994381708"
# =================================================

supabase = None
if SUPABASE_URL != "TU_SUPABASE_URL" and SUPABASE_KEY != "TU_SUPABASE_ANON_KEY":
    try:
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    except Exception as e:
        print("Error inicializando Supabase:", e)

def send_whatsapp_message():
    """Envía el mensaje de WhatsApp al número especificado."""
    mensaje = "Black prueba fuck al reservar de forma autnklaotca"
    print(f"\n[WhatsApp] Intentando enviar mensaje a {WHATSAPP_TARGET_NUMBER}...")
    
    if WHATSAPP_API_TOKEN == "TU_ULTRAMSG_TOKEN":
        print(f"[WhatsApp - SIMULACIÓN] Mensaje: '{mensaje}'")
        print("[WhatsApp] Para enviar de verdad, configura WHATSAPP_API_TOKEN en server.py")
        return True
        
    payload = {
        "token": WHATSAPP_API_TOKEN,
        "to": WHATSAPP_TARGET_NUMBER,
        "body": mensaje
    }
    try:
        response = requests.post(WHATSAPP_API_URL, data=payload)
        return response.status_code == 200
    except Exception as e:
        print("[WhatsApp] Error enviando WhatsApp:", e)
        return False

class RequestHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        # 1. Endpoint Chatbot
        if self.path == '/api/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            message = data.get('message', '').lower()
            
            reply = "Gracias por tu mensaje. Un asesor te responderá pronto."
            if "inscrip" in message or "precio" in message:
                reply = "Puedes inscribirte en la sección 'Inscripción'. Paquetes: Básico ($80), Premium ($150), VIP ($250)."
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'reply': reply}).encode('utf-8'))
            
        # 2. Endpoint Inscripción / Reservas
        elif self.path == '/api/inscribir':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                
                # A. Guardar en Supabase
                if supabase:
                    try:
                        supabase.table('inscripciones').insert(data).execute()
                        print("[Supabase] Datos guardados exitosamente.")
                    except Exception as e:
                        print("[Supabase] Error al guardar:", e)
                else:
                    print(f"\n[Supabase - SIMULACIÓN] Datos a guardar:\n{json.dumps(data, indent=2)}")
                
                # B. Enviar Mensaje de WhatsApp Automático
                send_whatsapp_message()
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": True}).encode('utf-8'))
                
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
                
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print("========================================")
    print("Servidor backend iniciado (Puerto 8080)")
    print(f"Supabase Conectado: {'SÍ' if supabase else 'NO (Modo Simulación)'}")
    print("========================================")
    httpd.serve_forever()
