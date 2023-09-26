from http.server import HTTPServer,BaseHTTPRequestHandler,SimpleHTTPRequestHandler
from jinja2 import Environment,PackageLoader,select_autoescape
from mas import tranding_mas,riht_content,weak_mas

class CustomHandler(SimpleHTTPRequestHandler):
    env=Environment(
        loader=PackageLoader("main"),
        autoescape=select_autoescape()
    )
    def do_GET(self):
        if self.path.startswith('/media/'):
            super().do_GET()
        elif self.path=='/' or self.path=='/index':
            self.render_index()
        elif self.path=='/categori':
            self.render_categori()
        elif self.path=='/about':
            self.render_about()
        elif self.path=='/latest_news':
            self.render_latest_news()
        elif self.path=='/contact':
            self.render_contact()
        elif self.path=='/elements':
            self.render_elements()
        elif self.path=='/blog':
            self.render_blog()
        elif self.path=='/single-blog':
            self.render_single_blog()
        elif self.path=='/details':
            self.render_details()
    
    def render_index(self):
        self.send_response(200)
        self.send_header("Content-type",'text/html')
        self.end_headers()
        body=self.env.get_template("index.html").render(tranding_mas=tranding_mas,riht_content=riht_content,weak_mas=weak_mas)
        self.wfile.write(body.encode('utf-8'))

    def render_categori(self):
        self.send_response(200)
        self.send_header("Content-type",'text/html')
        self.end_headers()
        body=self.env.get_template("categori.html").render()
        self.wfile.write(body.encode('utf-8'))
    
    def render_about(self):
        self.send_response(200)
        self.send_header("Content-type",'text/html')
        self.end_headers()
        body=self.env.get_template("about.html").render()
        self.wfile.write(body.encode('utf-8'))
    
    def render_latest_news(self):
        self.send_response(200)
        self.send_header("Content-type",'text/html')
        self.end_headers()
        body=self.env.get_template("latest_news.html").render()
        self.wfile.write(body.encode('utf-8'))

    def render_contact(self):
        self.send_response(200)
        self.send_header("Content-type",'text/html')
        self.end_headers()
        body=self.env.get_template("contact.html").render()
        self.wfile.write(body.encode('utf-8'))

    def render_elements(self):
        self.send_response(200)
        self.send_header("Content-type",'text/html')
        self.end_headers()
        body=self.env.get_template("elements.html").render()
        self.wfile.write(body.encode('utf-8'))

    def render_blog(self):
        self.send_response(200)
        self.send_header("Content-type",'text/html')
        self.end_headers()
        body=self.env.get_template("blog.html").render()
        self.wfile.write(body.encode('utf-8'))

    def render_single_blog(self):
        self.send_response(200)
        self.send_header("Content-type",'text/html')
        self.end_headers()
        body=self.env.get_template("single-blog.html").render()
        self.wfile.write(body.encode('utf-8'))

    def render_details(self):
        self.send_response(200)
        self.send_header("Content-type",'text/html')
        self.end_headers()
        body=self.env.get_template("details.html").render()
        self.wfile.write(body.encode('utf-8'))

def run (server_class=HTTPServer,handler_class=BaseHTTPRequestHandler):
    server_address=('',8000)
    httpd=server_class(server_address,handler_class)
    print("[+] Server starting")
    httpd.serve_forever()

if __name__=="__main__":
    run(handler_class=CustomHandler)