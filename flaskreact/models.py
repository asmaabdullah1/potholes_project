from flask_sqlalchemy import SQLAlchemy
         
db = SQLAlchemy()
         
class Potholes(db.Model): 
    __tablename__ = "tblpotholes_2"
    p_id = db.Column(db.Integer, primary_key=True) 
    location = db.Column(db.String(150) ) 
    district = db.Column(db.String(150) ) 
    longitude = db.Column(db.String(150) ) 
    latitude = db.Column(db.String(150) )