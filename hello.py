from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import parse_qs

class VotingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Cargar votos actuales
        with open("votes.json", "r") as file:
            votes = json.load(file)

        # HTML con botones de votación y botón para reiniciar
        html = f"""
        <html>
            <head>
                <title>Votaciones</title>
            </head>
            <body>
                <h1>¿Qué prefieres?</h1>
                <form method="POST">
                    <button type="submit" name="vote" value="Pizza">🍕 Pizza</button>
                    <button type="submit" name="vote" value="Tacos">🌮 Tacos</button>
                </form>

                <h2>Resultados:</h2>
                <p>Pizza: {votes['Pizza']} votos</p>
                <p>Tacos: {votes['Tacos']} votos</p>

                <form method="POST" style="margin-top: 30px;">
                    <button type="submit" name="vote" value="reset" style="background-color: red; color: white;">🔄 Reiniciar conteo</button>
                </form>
            </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def do_POST(self):
        length = int(self.headers.get("Content-Length"))
        post_data = self.rfile.read(length).decode("utf-8")
        params = parse_qs(post_data)
        vote = params.get("vote", [None])[0]

        # Cargar votos actuales
        with open("votes.json", "r") as file:
            votes = json.load(file)

        if vote == "Pizza" or vote == "Tacos":
            votes[vote] += 1
        elif vote == "reset":
            votes["Pizza"] = 0
            votes["Tacos"] = 0

        # Guardar cambios
        with open("votes.json", "w") as file:
            json.dump(votes, file)

        # Redireccionar al inicio
        self.send_response(303)
        self.send_header("Location", "/")
        self.end_headers()

if __name__ == "__main__":
    server_address = ("0.0.0.0", 8090)
    httpd = HTTPServer(server_address, VotingHandler)
    print("Servidor corriendo en el puerto 8090...")
    httpd.serve_forever()
