from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/encrypt" method="post">
            <label>Rotate by: <input name="rot" type="number" value=0 id="rot_input" required></label>
            <textarea name="plaintext" placeholder="Enter message to encrypt here..." required autofocus>{0}</textarea>
            <input type="submit" value="Encrypt plaintext">
        </form>
    </body>
</html>"""


@app.route("/")
def index():
  return form.format("")

@app.route("/encrypt", methods=['POST'])
def encrypt():
  rot = int(request.form['rot'])
  text = str(request.form['plaintext'])
  return form.format(rotate_string(text, rot))

app.run()