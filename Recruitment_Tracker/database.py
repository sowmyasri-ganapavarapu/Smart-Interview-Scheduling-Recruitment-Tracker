import mysql.connector
import config


def connect():
    connection = mysql.connector.connect(
        host=config.host,
        user=config.user,
        password=config.password,
        database=config.database
    )
    return connection