from application import app
from flask.mysqldb import MySQL
from MySQLdb.cursors import Cursor

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'coltis_movie_flask'
app.config['MYSQL_PORT'] = '3307'
MySQL = MySQL(app)

def excecute(sql: str) -> Cursor:
    cursor = mysql.connection.cursor()
    cursor.excute(sql)
    return cursor

def commit() -> None:
    mysql.connection.commit()