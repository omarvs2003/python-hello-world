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
                <style>
                    body {{
                        background-color: #f7f7f7;
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        justify-content: center;
                        padding: 40px;
                        color: #333;
                    }}
                    h1 {{
                        color: #222;
                        font-size: 2em;
                    }}
                    form {{
                        margin: 20px 0;
                    }}
                    button {{
                        padding: 15px 25px;
                        margin: 10px;
                        font-size: 16px;
                        border: none;
                        border-radius: 8px;
                        cursor: pointer;
                        transition: all 0.2s ease-in-out;
                    }}
                    button:hover {{
                        transform: scale(1.05);
                    }}
                    .vote-btn {{
                        background-color: #4CAF50;
                        color: white;
                    }}
                    .reset-btn {{
                        background-color: #f44336;
                        color: white;
                    }}
                    .card {{
                        background: white;
                        padding: 20px;
                        border-radius: 12px;
                        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                        max-width: 300px;
                        text-align: center;
                    }}
                </style>
            </head>
            <body>
                <h1>¿Qué prefieres?</h1>
                <form method="POST">
                    <button type="submit" name="vote" value="Pizza" class="vote-btn">🍕 Pizza</button>
                    <button type="submit" name="vote" value="Tacos" class="vote-btn">🌮 Tacos</button>
                </form>

                <div class="card">
                    <h2>Resultados</h2>
                    <p>🍕 Pizza: <strong>{votes['Pizza']}</strong> votos</p>
                    <p>🌮 Tacos: <strong>{votes['Tacos']}</strong> votos</p>
                </div>

                <form method="POST">
                    <button type="submit" name="vote" value="reset" class="reset-btn">🔄 Reiniciar conteo</button>
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
