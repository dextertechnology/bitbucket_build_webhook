import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

from call_to_hook import ValidateResponse
from perpetrator import RunScript


HOST = os.getenv("WEBHOOK_HOST", "localhost")
PORT = os.getenv("WEBHOOK_PORT", 8000)
TOKEN=os.getenv("WEBHOOK_TOKEN", "bd3d75978a182fa93598df9731ca0c812c2f76410695a8c935e8823b7584f950")
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SCRIPT_DIR=os.getenv("SCRIPT_DIR", os.path.join(BASE_DIR, "scripts"))

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        print(self.path)

        check_path = f"/webhook/{TOKEN}"

        if self.path == check_path:
            body = self.rfile.read(content_length)
            self.send_response(200)
            self.end_headers()
            response = BytesIO()
            response.write(body)

            response_status = ValidateResponse(str(response.getvalue().decode('UTF-8')))
            valid_status = response_status.is_valid()

            if not valid_status:
                print("Request Invoked however, doing nothing")
            else:
                RunScript(os.path.join(SCRIPT_DIR, "aws_login.sh")).execute()
                RunScript(os.path.join(SCRIPT_DIR, "deploy_docker.sh")).execute()
                print("Deployment Completed")
        else:
            pass


if __name__ == "__main__":
    httpd = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
    print(f"Serving in {HOST}:{PORT}")
    httpd.serve_forever()
