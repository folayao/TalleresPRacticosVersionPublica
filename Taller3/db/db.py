import mysql.connector as mysql
conex = mysql.MySQLConnection(
    host = "127.0.0.1",
    port = 3306,
    user = "Su_Usuario",
    password = "Su_clave",
    database = "evergreen"
)