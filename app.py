from io import BytesIO
from flask import Flask, render_template, redirect, json, jsonify, request
import traceback
from base import Productos, session, insert, filter
import base

app = Flask(__name__, static_folder='staticFiles', template_folder='templates')

@app.route("/")
def index():
    try:
        return render_template('index.html')
    except:
        return jsonify({'trace': traceback.format_exc()})

@app.route("/productos", methods=['GET'])
def productos():
    if request.method == 'GET':
        try:
            return render_template('productos.html')
        except:
            return jsonify({'trace': traceback.format_exc()})

@app.route("/productos/todos", methods=['GET'])
def filt():
    try:
        productos_productos = {base.filter()}

        nueva = []

        for producto in productos_productos:
            nueva.append(producto)

        return jsonify(nueva)

    except:
        return jsonify({'trace': traceback.format_exc()})



@app.route("/abm", methods=['GET'])
def abm():
    if request.method == 'GET':
        return render_template('abm.html')
    #elif request.method == 'POST':
    #    file = request.files['file']
    #    upload = Upload(name=file.filename, data=file.read())
    #    session.add(upload)
    #    session.commit()
    #    return f'Uploaded: {file.filename}

@app.route("/nuevo", methods=['POST'])
def nuevo():
    if request.method == 'POST':
        n = str(request.form.get('name'))#name
        d = str(request.form.get('description'))#description
        c = str(request.form.get('categoria'))#categoria
        p = request.form.get('price')#price
        insert(n, d, c.capitalize(), p)

        return render_template('index.html')    

if __name__ == '__main__':
    app.run(debug=True)