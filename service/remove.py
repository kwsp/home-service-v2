import get_db

db = get_db.db()
c = db.cursor()

c.execute("DELETE from sensor_data where temperature = 11")
db.commit()
db.close()
