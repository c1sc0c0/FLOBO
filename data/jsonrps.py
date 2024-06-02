from http.server import BaseHTTPRequestHandler, HTTPServer
from jsonrpcserver import method, dispatch
import json

# Define a simple JSON-RPC method
@method
def ping():
    return "pong"

@method
def add(a: int, b: int) -> int:
    return a + b

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Read the length of the incoming request
        content_length = int(self.headers['Content-Length'])
        # Read the request body
        request_body = self.rfile.read(content_length)
        # Dispatch the request to the JSON-RPC server
        response = dispatch(request_body.decode())
        # Send response status code
        self.send_response(200)
        # Send headers
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        # Send the JSON-RPC response
        self.wfile.write(json.dumps(response).encode())

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()