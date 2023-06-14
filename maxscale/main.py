import mysql.connector

con = mysql.connector.connect(host = "172.21.0.4", user = "maxuser", password = "maxpwd", port = "4000")
cursor = con.cursor()

# write sql queries based off the assignment rubric on canvas
cursor.execute("SELECT;")
query_output = cursor.fetchall()
# displaying data

