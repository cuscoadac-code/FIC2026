from http.server import SimpleHTTPRequestHandler, HTTPServer
import json

class ChatHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            message = data.get('message', '').lower()
            
            # Simple bot logic
            reply = "Gracias por tu mensaje. Hemos recibido tu consulta y un asesor te responderá pronto."
            if "inscrip" in message or "precio" in message:
                reply = "Puedes inscribirte en la sección 'Inscripción'. Tenemos paquetes Básico ($80), Premium ($150) y VIP ($250)."
            elif "ruta" in message or "sector" in message or "distancia" in message:
                reply = "La ruta consta de 3 sectores: San Salvador–Pisac (25km), Taray–Urubamba (30km), y Calca–Urubamba (28km)."
            elif "fecha" in message or "cuando" in message:
                reply = "El festival se llevará a cabo del 15 al 17 de Agosto de 2025 en Cusco, Perú."
            elif "hola" in message or "buenos d" in message or "saludos" in message:
                reply = "¡Hola! Bienvenido al chat de la Ciclovía del Maíz. ¿En qué te puedo orientar?"
                
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'reply': reply}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, ChatHandler)
    print("Servidor chatbot iniciado en el puerto 8080...")
    httpd.serve_forever()
