from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Enviar respuesta HTTP 200 (OK)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # Mensaje que quieres mostrar en el navegador
        message = """
        <html>
            <head><title>Hola desde Docker</title></head>
            <body>
                <h1>¡Hola mundo desde Github! Ahora estoy conectado a Jenkins :) gatito!!!! perrito!!!!</h1>
                <p>Ahora vengo de un hook</p>
                <p>PD. Omar V, Edgar R, Ruber T</p>
                <p> test6 desde github </p>
                
            </body>
        </html>
        """
        
        # Escribir la respuesta al navegador
        self.wfile.write(message.encode('utf-8'))

if __name__ == "__main__":
    # Configurar el servidor para que escuche en todas las interfaces (0.0.0.0) y en el puerto 8090
    server_address = ('0.0.0.0', 8090)
    httpd = HTTPServer(server_address, HelloHandler)
    print("Servidor corriendo en el puerto 8090...")
    httpd.serve_forever()
