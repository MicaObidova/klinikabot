import sqlite3
import pandas as pd

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Ma'lumotlarni olib kelish
cursor.execute("SELECT * FROM users")
data = cursor.fetchall()

# Pandas DataFrame yaratish
df = pd.DataFrame(data, columns=["ID", "Chat ID", "Full Name", "Phone", "Address", "Health Issue"])

# CSV faylga saqlash
df.to_csv("users_data.csv", index=False, encoding="utf-8")

print("Ma'lumotlar users_data.csv fayliga saqlandi!")

conn.close()