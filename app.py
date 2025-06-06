import os
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html_code = """
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <title>Giới thiệu bản thân</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f0f8ff;
                margin: 50px;
                text-align: center;
            }
            .container {
                background: white;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                display: inline-block;
            }
            h1 {
                color: #2c3e50;
            }
            p {
                font-size: 18px;
                color: #34495e;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Xin chào!</h1>
            <p><strong>Tên:</strong> {{ name }}</p>
            <p><strong>MSSV:</strong> {{ student_id }}</p>
            <p>Chào mừng bạn đến với trang web giới thiệu của mình.</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_code, name="Quách Kỳ Hiệp", student_id="22DH111096")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
