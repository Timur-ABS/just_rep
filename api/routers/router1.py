from database import connect

connect.execute("SELECT * FROM users;")
print(connect.fetchall())
connect.__del__()