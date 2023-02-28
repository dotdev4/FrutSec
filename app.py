from io import BytesIO
from flask import Flask, render_template, redirect, json, jsonify, request
import traceback
from base import Productos, session, insert, filter, Session
import base

app = Flask(__name__, static_folder='staticFiles', template_folder='templates')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/productos", methods=['GET'])
def productos():
    if request.method == 'GET':
        try:
            return render_template('productos.html')
        except:
            return jsonify({'trace': traceback.format_exc()})

@app.route("/productos/<cat>", methods=['GET'])
def productos_x_cat(cat):
    try:
        if cat is not None:
            cat = cat.lower()
            f = filter(cat=cat)
            return render_template("productos.html", data=f, href = "/productos/" + f"{cat}")
        else:
            pass
    except:
        return render_template('index.html')

@app.route("/productos/todos", methods=['GET'])
def productos_todos():
    try:
        session = Session()
        data = session.query(Productos).all()
        return render_template('productos.html', data=data)
    except:
        return render_template('index.html')
        
@app.route("/abm", methods=['GET'])
def abm():
    if request.method == 'GET':
        return render_template('abm.html')

@app.route("/nuevo", methods=['POST'])
def nuevo():
    if request.method == 'POST':
        n = str(request.form.get('name'))#name
        d = str(request.form.get('description'))#description
        c = str(request.form.get('categoria'))#categoria
        p = request.form.get('price')#price
        insert(n, d, c.lower(), p)

        return render_template('index.html')    

if __name__ == '__main__':
    app.run(debug=True)