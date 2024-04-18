from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_cors import CORS, cross_origin
from models import db, Potholes

app = Flask(__name__)

api_v1_cors_config = {
    "origins": ["http://localhost:5173"],
    "methods": ["GET"],
    "allow_headers": ["Authorization", "Content-Type"]
}



CORS(app, resources={
    r"/api/v1/*": api_v1_cors_config
})


app.config['SECRET_KEY'] = 'asma-coding'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flaskreact'
 
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
  
CORS(app, supports_credentials=True)
 
db.init_app(app)
        
with app.app_context():
    db.create_all()
 
ma=Marshmallow(app)


class PotholeSchema(ma.Schema):
    class Meta:
        fields = ('p_id','location','district','longitude', 'latitude')
  
pothole_schema = PotholeSchema()
potholes_schema = PotholeSchema(many=True)
 
@app.route('/api/v1/potholes', methods=['GET']) 
def listpothles():
    all_potholes = Potholes.query.all()
    results = potholes_schema.dump(all_potholes)
    return jsonify(results)
  
@app.route('/api/v1/potholedetails/<p_id>',methods =['GET'])
def potholedetails(p_id):
    pothole = Potholes.query.get(p_id)
    return pothole_schema.jsonify(pothole)

@app.route('/api/v1/newpothole',methods=['POST'])
def newuser():
    location = request.json['location']
    district = request.json['district']
    longitude = request.json['longitude']
    latitude = request.json['latitude']
 
    print(location)
    print(district)
    print(longitude)
    print(latitude)

    potholes = Potholes(location=location, district=district, longitude=longitude, latitude=latitude)

    db.session.add(potholes)
    db.session.commit()
    return pothole_schema.jsonify(potholes)
  
if __name__ == "__main__":
    app.run(debug=True)
