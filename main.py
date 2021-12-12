from flask import Flask, render_template, request, redirect, url_for
from werkzeug.datastructures import ImmutableMultiDict
import time

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/upload', methods=['POST'])
def upload_file():
    data = dict(request.form)
    uploaded_file = data['image']
    uploaded_filename = data['filename']
    time.sleep(2)
    if uploaded_filename != '':
        print(f"UPLOADED FILE {type(uploaded_file)} {uploaded_filename}")
        with open(uploaded_filename, "wb") as binary_file:
            pass
            # binary_file.write(bytes(uploaded_file))
        return 'Success'
    else:
        return 'filename empty'

if __name__ == '__main__':
   app.run(debug = True)