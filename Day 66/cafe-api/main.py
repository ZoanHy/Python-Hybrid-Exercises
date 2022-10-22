import json
from random import *
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
FOLDER = "C:/Users/ASUS/BK University/5_Self_Study/6_PythonHybrid/db"
API_KEY = "zoanhyhahahaha"

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{FOLDER}/cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def convert_dict(self):
        dict = {}
        for col in self.__table__.columns:
            dict[col.name] = getattr(self, col.name);
        return dict
    
        # return {col.name: getattr(self, col.name) for col in self.__table__.columns}

@app.route("/")
def home():
    return render_template("index.html")

## HTTP GET - Read Record
@app.route('/random', methods=['GET'])
def random_cafe_shop():
    cafes = db.session.query(Cafe).all()
    random_cafe = choice(cafes)
    # return jsonify(cafe = {
    #     # "id" : random_cafe.id,
    #     "name":   random_cafe.name,
    #     "map_url":random_cafe.map_url,
    #     "img_url":random_cafe.img_url,
    #     "location": random_cafe.location,
    #     'amenities':{
    #         "seats": random_cafe.seats,
    #         "has_toilet": random_cafe.has_toilet,
    #         "has_wifi": random_cafe.has_wifi,
    #         "has_sockets":random_cafe.has_sockets,
    #         "can_take_calls": random_cafe.can_take_calls,
    #         "coffee_price":random_cafe.coffee_price,
    #     }
    # })

    return jsonify(cafe = random_cafe.convert_dict())

@app.route('/all', methods=['GET'])
def get_all_cafes():
    list_cafe = []
    cafes = db.session.query(Cafe).all()
    list_cafe = [cafe.convert_dict() for cafe in cafes]        
    return jsonify(cafes=list_cafe)

@app.route('/search')
def search():
    loc = request.args.get("loc")
    cafe_found = db.session.query(Cafe).filter_by(location=loc).first()
    
    if cafe_found:
        return jsonify(cafe=cafe_found.convert_dict())
    else:
        return jsonify(errors={'No occur': "Please check again!"})
    

## HTTP POST - Create Record    
@app.route('/add', methods = ['POST'])
def add_new_cafe():
    cafe = Cafe (
        name = request.form.get('name'),
        map_url = request.form.get('map_url'),
        img_url = request.form.get('img_url'),
        location = request.form.get('location'),
        seats = request.form.get('seats'),
        has_toilet = bool(request.form.get('has_toilet')),
        has_wifi = bool(request.form.get('has_wifi')),
        has_sockets =bool(request.form.get('has_sockets')),
        can_take_calls =bool(request.form.get('can_take_calls')),
        coffee_price = request.form.get('coffee_price')
    )
    with app.app_context():
        db.session.add(cafe)
        db.session.commit()
    return jsonify(reponse={'success' : "Add successfully"})


## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<cafe_id>', methods = ['PATCH'])
def update_price(cafe_id):
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = request.args.get('new_price')
        db.session.commit()
        return jsonify(response={'success':"Update successfully"}), 200
    else:
        return jsonify(errors={'Not Found':"Id not found in database! Check again!"}), 404
        

## HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=['DELETE'])
def delete_a_cafe(cafe_id):
    api_key = request.args.get('api-key')
    if api_key == API_KEY:
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(reponse={'Success':'Delete successfully'}), 200
        else:
            return jsonify(errors={'Not Found': "Id not found in database! Check again!"}),404
    else:
        return jsonify(errors={'Forbidden', "You should check API KEY to Authenciated"}), 403
       

if __name__ == '__main__':
    app.run(debug=True)
