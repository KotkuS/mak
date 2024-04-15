import psycopg2

conn = psycopg2.connect(dbname="postgres", user="user8", password="O8Je0iSal", host="217.76.60.77", port=6666)
cursor = conn.cursor()
