from http.server import BaseHTTPRequestHandler
import json
import os

try:
    from supabase import create_client, Client
    import requests
except ImportError:
    pass

SUPABASE_URL = os.environ.get("SUPABASE_URL", "TU_SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "TU_SUPABASE_ANON_KEY")
WHATSAPP_API_URL = os.environ.get("WHATSAPP_API_URL", "https://api.ultramsg.com/INSTANCE_ID/messages/chat")
WHATSAPP_API_TOKEN = os.environ.get("WHATSAPP_API_TOKEN", "TU_ULTRAMSG_TOKEN")
WHATSAPP_TARGET_NUMBER = "+51994381708"

supabase = None
if SUPABASE_URL != "TU_SUPABASE_URL" and SUPABASE_KEY != "TU_SUPABASE_ANON_KEY":
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    except:
        pass

def send_whatsapp_message():
    mensaje = "Black prueba fuck al reservar de forma autnklaotca"
    if WHATSAPP_API_TOKEN == "TU_ULTRAMSG_TOKEN":
        return True
    
    payload = {
        "token": WHATSAPP_API_TOKEN,
        "to": WHATSAPP_TARGET_NUMBER,
        "body": mensaje
    }
    try:
        requests.post(WHATSAPP_API_URL, data=payload)
    except:
        pass

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Vercel quita el trailing slash o lo maneja diferente, pero en Vercel la ruta base del handler
        # depende del nombre del archivo. Usaremos self.path que contiene la URL original.
        if '/api/chat' in self.path:
            content_length = int(self.headers.get('Content-Length', 0))
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
            
        elif '/api/inscribir' in self.path:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                if supabase:
                    try:
                        supabase.table('inscripciones').insert(data).execute()
                    except:
                        pass
                
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
