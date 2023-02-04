import os
import psycopg2

# use export DATABASE_URL="postgresql://getonly:<ENTER-SQL-USER-PASSWORD>@hyping-wasp-8765.7tt.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full"
# before running this script in python (replace export with set in windows)

conn = psycopg2.connect(os.environ["DATABASE_URL"])

with conn.cursor() as cur:
    print("HERE")
    cur.execute("SELECT * FROM public.parkingoccupancy")
    res = cur.fetchall()
    conn.commit()
    print(res)