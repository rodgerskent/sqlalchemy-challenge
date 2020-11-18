# sqlalchemy-challenge
Name
SQLalchemy challenge – Surfs Up!

Overview
This project requires utilizing climate data for Hawaii and presenting summary insights/analytics via an web api. 

Approach & Methodology
The project required building the initial analysis in Jupyter Notebook for planning purposes. Then Python code was utilized to present the desired data in a json format via a web api. 

Step 1 – Setup
All of the analysis is completed using SQLAlchemy ORM queries, Pandas, and Matplotlib. The analysis is performed using the Hawaii.sqlite database provided with the exercise. The analysis was targeted on the trailing 12 months of data leading up to August 23, 2017; the last available date provided in the database. 

Step 1 – Precipitation Analysis Deliverables
1.	Design a query to retrieve the last 12 months of precipitation data.
2.	Select only the `date` and `prcp` values.
3.	Load the query results into a Pandas DataFrame and set the index to the date column.
4.	Sort the DataFrame values by `date`.
5.	Plot the results using the DataFrame `plot` method.
6.	Use Pandas to print the summary statistics for the precipitation data.

Step 1 - Station Analysis Deliverables
1.	Design a query to calculate the total number of stations.
2.	Design a query to find the most active stations.
3.	List the stations and observation counts in descending order.
4.	Identify which station has the highest number of observations
5.	Design a query to retrieve the last 12 months of temperature observation data (TOBS).
6.	Filter by the station with the highest number of observations.
7.	Plot the results as a histogram with `bins=12`.

Step 2 - Climate App
The second step involves converting the initial analysis performed in the Jupyter Notebook to build a Flask API. The following routes and deliverables were created in Visual Studio:

Routes
* `/` …   * Home page …  * List all routes that are available.
* `/api/v1.0/precipitation` …  * Convert the query results to a dictionary using `date` as the key and `prcp` as the value …  * Return the JSON representation of your dictionary.
* `/api/v1.0/stations` …  * Return a JSON list of stations from the dataset
* `/api/v1.0/tobs` … * Query the dates and temperature observations of the most active station for the last year of data … * Return a JSON list of temperature observations (TOBS) for the previous year.
* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>` …  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range. … * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date … * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

Key Takeaways
The project is a building block for being able to provide HTML dashboards in future efforts. 

Repository Summary & Deliverables Locator
•	Juypter Notebook = climate_starter.ipynb
•	Application = app.py
- Rodgers_PitchBook_SurfsUp = Images of charts and web pages from the effort

Support
Again thanks to tutor to support pushing through the start/end enabled query. 

Roadmap
Not applicable

Contributing
This project was complete on an individual basis

License
Not applicable

Project status
Core assignment is complete. The bonus section is submitted but with limited success. 
