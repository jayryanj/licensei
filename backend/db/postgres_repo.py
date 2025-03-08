from traceback import print_exception

import psycopg2
from flask import current_app
from psycopg2 import DataError, DatabaseError


def __get_connection():
    # TODO move config out
    postgres_config = {
        "dbname": current_app.config["DB_NAME"],
        "user": current_app.config["DB_USER"],
        "password": current_app.config["DB_PASSWORD"],
        "host": current_app.config["DB_HOST"]
    }
    try:
        return psycopg2.connect(**postgres_config)
    except psycopg2.OperationalError as e:
        print_exception(e)
        # TODO create custom exception and implement
        raise Exception("Failed to connect to database")


def get_all_licenses():
    connection = __get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute('SELECT license_key FROM license;')
        rows = cursor.fetchall()
        return [row[0] for row in rows]
    except (DataError, DatabaseError) as e:
        # TODO implement proper error handling
        print(e)
    finally:
        connection.close()


def insert_license(new_license, license_type, expiry, product, description):
    connection = __get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute('''
            INSERT INTO license(
            license_key,
            product,
            created,
            expiration,
            type,
            description
            )
            VALUES(%s, %s, DEFAULT, %s, %s, %s)
        ''', (new_license, product, expiry, license_type, description))
        connection.commit()
    except (DataError, DatabaseError) as e:
        # TODO implement proper error handling
        print(e)
    finally:
        connection.close()
