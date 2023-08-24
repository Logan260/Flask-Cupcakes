from flask import Flask, render_template, jsonify, request
from models import db, connect_db, Cupcake

app = Flask(__name__, template_folder="templates")

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "peanutbutter"
connect_db(app)

@app.route("/")
def root():
    "Home page"
    return render_template ("index.html")

@app.route("/api/cupcakes")
def cupcake_list():
    "returns cupcakes in JSON"
    cupcakes = [cupcake._dict() for cupcake in Cupcake.query.all()]
    return jsonify (cupcakes = cupcakes)

@app.route("/api/cupcakes", methods = ["POST"])
def create_cupcake():
    """This will add a cupcake and return data about the new cupcake in JSON"""
    data = request.json
    cupcake = Cupcake(
        flavor=data["flavor"],
        rating= data["rating"],
        size = data["size"],
        image = data["image"] or None
    )
    db.session.add(cupcake)
    db.session.commit()
    return (jsonify(cupcake = cupcake._dict()))

@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """returns info for one cupcake"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake = cupcake._dict())

@app.route("/api/cupcakes/<int:cupcake_id>", methods = ["PATCH"])
def update_cupcake(cupcake_id):
    """Update cupcake"""
    data = request.json
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.flavor = data["flavor"]
    cupcake.rating = data["rating"]
    cupcake.size = data["size"]
    cupcake.image = data["iamge"]
    db.session.add(cupcake)
    db.session.commit()
    return jsonify(cupcake = cupcake._dict())

@app.route("/api/cupcake/<int:cupcake_id>", methods = ["DELETE"])
def delete_cupcake(cupcake_id):
    """This deletes a cupcake and retruns a message"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(messgae = "Cupcake Deleted!")