import requests
import json
import psycopg2
import random

response = requests.get("https://restcountries.com/v3.1/all?fields=name,capital,flag,subregion,population")
resp = response.json()

connection = psycopg2.connect(
    host = 'localhost',
    user = 'postgres',
    password = 'postgres',
    database = 'Countries'
)

curson = connection.cursor()

def insert_country (*info) :
    try :
        with connection:
            with connection.cursor() as curs: #open and close the cursor
                query = f"""INSERT INTO country (name, capital, flag, subregion, population)
                VALUES {info}
                """
                curs.execute(query)
                connection.commit()
    except Exception as err :
        print(err)

listR = random.sample(range (250), 10)
for i in listR:
    insert_country(resp[i]['name']['common'], resp[i]['capital'][0], resp[i]['flag'], resp[i]['subregion'], resp[i]['population'])

connection.close()