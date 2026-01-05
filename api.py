from flask import Flask, render_template, request
import mysql.connector

# Flask --> creates web application
# render_template --> loads HTML page
# request --> collects form data
# mysql.connector --> connects Python with MySQL

app = Flask(__name__)
# Creates a Flask application object


@app.route('/')        #decorator 
def home():
    return render_template('gpro.html')
# '/' ---> is the home page
# When browser opens the site, it shows your form
# Flask looks inside templates/form.html


@app.route('/submit-crime', methods=['POST'])
# This URL matches your form action: /register
# POST method is used to receive form data securely
def register():
    case_id = request.form['case_id']
    crime_year = int(request.form['crime_year'])
    crime_month = int(request.form["crime_month"])
    crime_day = int(request.form["crime_day"])
    crime_time_slot = request.form["crime_time_slot"]
    zone = request.form['zone']
    police_station = request.form["police_station"]
    area_type = request.form["area_type"]
    population_density = int(request.form["population_density"])
    festival_season =int(request.form["festival_season"])
    prior_criminal_record = int(request.form["prior_criminal_record"])
    victim_age = request.form["victim_age"]
    victim_gender = request.form["victim_gender"]
    crime_type = request.form["crime_type"]
    # request.form fetches input values
    # data in stored in python variables 

    connector = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="rags25",
        database="crime",
        port=3306)
    # Connects form.html to MySQL
   
    ex = connector.cursor()
    # Cursor is used to execute SQL queries

    query = """
    INSERT INTO crimedetail
    (case_id, crime_year,crime_month,crime_day,crime_time_slot,zone,police_station,area_type,
    population_density,festival_season,prior_criminal_record,victim_age,victim_gender,crime_type)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    # SQL INSERT statement
    # Matches table column order

    values = (case_id, crime_year,crime_month,crime_day,crime_time_slot,zone,police_station,area_type,
    population_density,festival_season,prior_criminal_record,victim_age,victim_gender,crime_type)
    # Tuple containing form values
    # Sent to SQL query

    ex.execute(query, values)
    connector.commit()
    ex.close()
    connector.close()


    # execute() → runs SQL command
    # commit() → saves data permanently
    # close() → closes database connection

    return render_template('gpro.html')
    # used to Sends confirmation message to browse
if __name__ == '__main__':
    app.run(debug=True)
