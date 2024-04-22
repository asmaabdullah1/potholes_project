from flask_sqlalchemy import SQLAlchemy
         
db = SQLAlchemy()
         
class Potholes(db.Model): 
    __tablename__ = "tblpotholes_2"
    p_id = db.Column(db.Integer, primary_key=True)   
    longitude = db.Column(db.String(150) ) 
    latitude = db.Column(db.String(150) )
    image = db.Column(db.String(150) )
