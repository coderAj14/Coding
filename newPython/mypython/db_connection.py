import psycopg2
import traceback
import os
import logging
import re
from psycopg2 import pool
from flask import current_app as app

logger = logging.getLogger('wslog')

def get_public_studies():
    query = "select acc from studies where status = 3;"
    query = query.replace('\\', '')
    postgresql_pool, conn, cursor = get_connection()
    cursor.execute(query)
    data = cursor.fetchall()
    release_connection(postgresql_pool, conn)
    return data




def release_connection(postgresql_pool, ps_connection):
    try:
        postgresql_pool.putconn(ps_connection)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
        logger.error("Error while releasing PostgreSQL connection. " + str(error))




def get_connection():
    try:
        params = {'database': 'mmimtbldev', 'user': 'isatab', 'password': 'QD1yYfmcTIwY', 'host': 'pgsql-hxvm-017.ebi.ac.uk', 'port': 5432}
        conn_pool_min = 1
        conn_pool_max = 20
        postgresql_pool = psycopg2.pool.SimpleConnectionPool(conn_pool_min, conn_pool_max, **params)
        conn = postgresql_pool.getconn()
        cursor = conn.cursor()
    except Exception as e:
        logger.error("Could not query the database " + str(e))
        postgresql_pool.closeall
    return postgresql_pool, conn, cursor