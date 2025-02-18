#!/usr/bin/python3
"""
Set up a simple HTTP server to serve JSON data and handle different endpoints
"""
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    """Handler to process GET requests."""
    
    def do_GET(self):
        """Handle GET requests"""
        response_data = {}  
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode())
        elif self.path == '/data':
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
    """Run the HTTP server."""
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Server running on http://localhost:8000...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
