
# Import Dependencies
from matplotlib import style
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as sts
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify

# database setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()
# reflect the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

@app.route("/")
def Welcome():
    print("Server received request for 'Welcome' page...")
    return(
        f"Welcome to the Rodgers bootstrap Hawaii weather site<br/>"
        f"------------------------------------------------------------------<br/>"
        f"Please chose from one of the following routes<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/statistics/&lt;start&gt;/&lt;end&gt;"
        )

# Note &lt ... less than, &gt ... greater than

@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'Precipitation' page...")
  
    # Create our session (link) from Python to the DB
    session = Session(engine)
    # Query precipitation data for Waikiki station
    precip1 = session.query(Measurement.station, Measurement.date, Measurement.prcp).\
        filter(Measurement.station == 'USC00519397').\
        filter(Measurement.date >= '2016-08-24' ).\
        order_by(Measurement.date).all()

    session.close()

    # Convert list of tuples into normal list
    waikiki = list(np.ravel(precip1))

    return jsonify(waikiki)

    #return(
    #    f"Waikiki Precipitation for the Trailing 12 Months"
    #)

@app.route("/api/v1.0/stations")
def stations():
    print("Server received request for 'Stations' page...")
    
    # Create our session (link) from Python to the DB
    session = Session(engine)
    # Query precipitation data for Waikiki station
    active = session.query(Station.station, Station.name).\
    order_by(Station.station).all()

    session.close()

    # Convert list of tuples into normal list
    stationlist = list(np.ravel(active))

    return jsonify(stationlist)

@app.route("/api/v1.0/tobs")
def Temperature():
    print("Server received request for 'Observed Temperatures' page...")
    
    # Create our session (link) from Python to the DB
    session = Session(engine)
    # Query temperature data for Waikiki station
    templ = session.query(Measurement.station, Measurement.date, Measurement.tobs).\
        filter(Measurement.station == 'USC00519397').\
        filter(Measurement.date >= '2016-08-24' ).\
        order_by(Measurement.date).all()

    session.close()

    # Convert list of tuples into normal list
    waikikitemp = list(np.ravel(templ))

    return jsonify(waikikitemp)

#2016-08-24/2017-08-23
@app.route("/api/v1.0/statistics/<start>/<end>")
def Statistics(start, end):
    print("Server received request for 'Temperature Statistics' page...")
    
# Create our session (link) from Python to the DB
    session = Session(engine)

    minimum = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.station == 'USC00519397').\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).\
        order_by(Measurement.date).all()

    return jsonify(minimum)

if __name__ == "__main__":
    app.run(debug=True)



