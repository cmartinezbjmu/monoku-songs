import psycopg2
from psycopg2 import sql
import os
import csv


def connect_db():
    try:
        connection = psycopg2.connect(user = os.environ.get('DBUSER', None),
                                      password = os.environ.get('DBPASS', None),
                                      host = os.environ.get('DBHOST', None),
                                      port = os.environ.get('DBPORT', None),
                                      database = os.environ.get('DBNAME', None))        

    except (Exception, psycopg2.Error) as error :        
        return None
    
    else:        
        return connection

{
    "artist": 5,

}

def update_db_single_register(connection):
    cursor = connection.cursor()
    with open('../files/prueba_back_monoku_2021_datos.csv', newline='\n') as csvfile:
        read_data = csv.reader(csvfile, delimiter=',')
        line_count = 0
        for row in read_data:
            if line_count == 0:
                line_count += 1
            else:
                register = row[5]
                query = sql.SQL("SELECT name FROM artist where name = '{}'".format(register))
                cursor.execute(query)
                result = cursor.fetchall()
                if len(result) == 0:
                    print('Inserta artista ' + register)                    
                    query = sql.SQL("INSERT INTO artist (name) VALUES ('{}')".format(register))
                    cursor.execute(query)
                    connection.commit()
                    
                    # Registra banda
                    register = row[4]
                    query = sql.SQL("SELECT id FROM band where name = '{}'".format(register))
                    cursor.execute(query)
                    result = cursor.fetchall()
                    if len(result) == 0:
                        print('Inserta banda ' + register)                    
                        query = sql.SQL("INSERT INTO band (name, artist_id) VALUES ('{}', {})".format(register, line_count))
                        cursor.execute(query)
                        connection.commit()
                    else:
                        print('La banda ' + register + ' ya existe')
                else:
                    print('El artista ' + register + ' ya existe')                        
                line_count += 1
        cursor.close()
        print(f'Processed {line_count-1} lines.')


def update_db(connection):
    cursor = connection.cursor()
    with open('../files/prueba_back_monoku_2021_datos.csv', newline='\n') as csvfile:
        read_data = csv.reader(csvfile, delimiter=',')
        line_count = 0
        for row in read_data:
            if line_count == 0:
                line_count += 1
            else:
                similar_bands = row[9].split(';')
                for similar_band in similar_bands:
                    similar_band = similar_band.strip()
                    query = sql.SQL("SELECT name FROM band where name = '{}'".format(similar_band))
                    cursor.execute(query)
                    result = cursor.fetchall()
                    if len(result) == 0:
                        print('Inserta banda ' + similar_band)                    
                        query = sql.SQL("INSERT INTO band (name) VALUES ('{}')".format(similar_band))
                        cursor.execute(query)
                        connection.commit()
                    else:
                        print('La banda ' + similar_band + ' ya existe')
                line_count += 1
        cursor.close()
        print(f'Processed {line_count-1} lines.')


def populate_db():
    connection_db = connect_db()
    if connection_db:
        update_db_single_register(connection_db)
        connection_db.close()
    else:
        print('No se pudo establecer conexion a la base de datos')


populate_db()