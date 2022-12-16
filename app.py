import os
import psycopg2
from flask import Flask,render_template

app=Flask(__name__)

def get_connection():
	conn=psycopg2.connect(
	host="localhost",
	database="dbname",
	user="read_only_user",
	password="your-pass"
)

return conn


@app.route('/')
def main_page():
	return render_template('main.html')


@app.route('/country_rankings')
def get_countries_list():
	conn=get_db_connection()
	cur=conn.cursor()
	cur.execute(
		SELECT country_name,fire_power_rank FROM country LIMIT 10
		)
	countryname=cur.fetchall()

	cur.close()
	conn.close()
	return render_template('firepower.html',L=countryname)


@app.route('/army')
def get_army_details():
	conn=get_db_connection()
	cur=conn.cursor()
	cur.execute(
		SELECT country_name,combat_tanks,armored_fighters,self_propelled_artillery,towered_artillery,rocket_projectors
		FROM country,army
		WHERE army.army_id=country.army_id
		)
	army_table=cur.fetchall()

	cur.close()
	conn.close()
	return render_template('army.html',L=army_table)



@app.route('/navy')
def get_navy_details():
	conn=get_db_connection()
	cur=conn.cursor()
	cur.execute(
		SELECT country_name,naval_assets,aircraft_carriers,frigates,destroyers,corvettes,submarines,patrol_crafts,warfare_vessels
		FROM country,army
		WHERE navy.navy_id=country.army_id
		)

	countryname=cur.fetchall()

	cur.close()
	conn.close()
	return render_template('navy.html',L=countryname)



@app.route('/airforce')
def get_airpower():
	conn=get_db_connection()
	cur=conn.cursor()
	cur.execute(
		SELECT country_name,aircraft_rank,aircrafts,fighter_aircrafts,attack_aircrafts,transport_aircrafts,trainer_aircrafts,helicopters,attack_helicopters
		FROM country,airforce
		WHERE country.airforce_id=airforce.airforce_id
		)
	countryname=cur.fetchall()

	cur.close()
	conn.close()
	return render_template('airforce.html',L=countryname)



@app.route('/country_details/<str:ctr_name>')
def get_countrydetails(ctr_name):
	conn=get_db_connection()
	cur=conn.cursor()
	query=
		SELECT country_name,iso3,iso2,capital,currency,region,subregion,population,area,GDP
		FROM country,economy,geography,manpower
		WHERE country.economy_id=economy.economy_id AND country.geography_id=geography.geography_id AND country.manpower_id=manpower.manpower_id
		AND country_name={}

	query=query.format(ctr_name)
	cur.execute(query)
	countryname=cur.fetchall()

	cur.close()
	conn.close()
	return render_template('country_details.html',L=countryname)

@app.route('/economy')
def get_economy():
	conn=get_db_connection()
	cur=conn.cursor()
	cur.execute(
		SELECT country_name,defense_budget,external_debt,forex,purchasing_power,gdp
		FROM country,economy
		WHERE country.economy_id=economy.economy_id
		)
	countryname=cur.fetchall()

	cur.close()
	conn.close()
	return render_template('economy.html',L=countryname)

@app.route('/geography')
def get_geography():
	conn=get_db_connection()
	cur=conn.cursor()
	cur.execute(
		SELECT country_name,land_area,coastline_length,shared_borders,waterway
		FROM country,geography
		WHERE country.geography_id=geography.geography_id
		)
	countryname=cur.fetchall()

	cur.close()
	conn.close()
	return render_template('geography.html',L=countryname)

@app.route('/states')
def get_economy():
	conn=get_db_connection()
	cur=conn.cursor()
	cur.execute(
		SELECT country_name,name,state_code
		FROM country,states
		WHERE country.country_id=states.country_id
		)
	countryname=cur.fetchall()

	cur.close()
	conn.close()
	return render_template('states.html',L=countryname)
    
@app.route('/cities')
def get_economy():
	conn=get_db_connection()
	cur=conn.cursor()
	cur.execute(
		SELECT states.name,cities.name
		FROM states,cities
		WHERE state.state_id=cities.state_id
		)
	countryname=cur.fetchall()

	cur.close()
	conn.close()
	return render_template('cities.html',L=countryname)


@app.route('/contribute')
def get_airpower():
	conn=get_db_connection()
	cur=conn.cursor()
	cur.execute(
		"SELECT * FROM country"
		)
	countryname=cur.fetchall()

	cur.close()
	conn.close()
	return render_template('contribute.html',L=countryname)


	