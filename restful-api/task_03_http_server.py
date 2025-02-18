#!/usr/bin/python3
"""
Développer une API simple en utilisant le module `http.server` de Python
"""
import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHandler(BaseHTTPRequestHandler):
    """Gestionnaire pour traiter les requêtes GET."""
    def do_GET(self):
        response_data = {}
        if self.path == '/data':
            response_data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode())
        elif self.path == '/status':
            response_data = {"status": "OK"}
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode())
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            response_data = {"error": "Not Found"}
            self.wfile.write(json.dumps(response_data).encode())


def run(server_class=HTTPServer, handler_class=SimpleHandler):
    """Exécuter le serveur HTTP."""
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Le serveur fonctionne sur http://localhost:8000...")
    httpd.serve_forever()
