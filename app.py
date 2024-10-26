from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///charging_stations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ChargingStation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    availability = db.Column(db.Boolean, default=True)

# Create tables before the first request


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/findst")
def findst():
    return render_template("findst.html")

@app.route("/bookslot")
def  bookslot():
    return render_template("bookslot.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/price")
def price():
    return render_template("price.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/second")
def second():
    return render_template("second.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/terms")
def term():  # Changed from 'contact' to 'terms' for correct routing
    return render_template("term.html")



# API Endpoints
@app.route("/api/stations", methods=["GET"])
def get_stations():
    stations = ChargingStation.query.all()
    return jsonify([
        {"id": station.id, "name": station.name, "location": station.location, "availability": station.availability}
        for station in stations
    ])

@app.route("/api/stations", methods=["POST"])
def add_station():
    data = request.get_json()
    new_station = ChargingStation(
        name=data['name'], 
        location=data['location'], 
        availability=data['availability']
    )
    db.session.add(new_station)
    db.session.commit()
    return jsonify({"message": "Station added!"}), 201

if __name__ == "__main__":
    app.run(debug=True)
