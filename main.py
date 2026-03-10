from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from socketserver import BaseRequestHandler


FILE_NAME = "test.txt.p7s"
FILE_PATH = Path(__file__).with_name(FILE_NAME)
HOST = "0.0.0.0"
PORT = 8080


class FileHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path != "/file":
            self.send_error(404)
            return

        data = FILE_PATH.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "application/x-p7s")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Content-Disposition", 'attachment; filename="test.txt.p7s"')
        self.end_headers()
        self.wfile.write(data)


def run() -> None:
    def handler(*args: object) -> BaseRequestHandler:
        return FileHandler(*args)

    server = HTTPServer((HOST, PORT), handler)
    print(f"Serving {FILE_NAME} at http://{HOST}:{PORT}/file")
    server.serve_forever()


if __name__ == "__main__":
    run()
