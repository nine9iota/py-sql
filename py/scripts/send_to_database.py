import pandas as pd
import mysql.connector

data = pd.read_csv(r'C:\Users\<myusername>\Documents\<mycsvfile.csv>')
df = pd.DataFrame(data)

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="1234"
)

cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS python_test")
mydb.commit()
mydb = None


mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="1234",
    database="python_test"
)

cursor = mydb.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            employee_id int primary key AUTO_INCREMENT,
            company_name varchar(250),
            contact varchar(250),
            email varchar(250)
            )
''')

for row in df.itertuples():
    sql = f"INSERT INTO employees (company_name, contact, email) VALUES ('{row.company}', '{row.contact}', '{row.email}');"
    cursor.execute(sql)

mydb.commit()
mydb = None
