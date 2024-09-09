from http.server import BaseHTTPRequestHandler, HTTPServer

hostname = "localhost"
serverport = 8080


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('contacts.html', 'r', encoding='utf-8') as file:
            data = file.read()
            self.wfile.write(bytes(data, 'utf-8'))

    def do_POST(self):
        content_len = int(self.headers['Content-Length'])
        body = self.rfile.read(content_len)
        print(body)
        self.send_response(200)
        self.end_headers()

        with open('contacts.html', 'r', encoding='utf-8') as file:
            data = file.read()
            self.wfile.write(bytes(data, 'utf-8'))




if __name__ == '__main__':
    server = HTTPServer((hostname, serverport), MyServer)

    print(f"server started http://{hostname}:{serverport}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
