from chalice import Chalice
import os 
import psycopg2 
import psycopg2.extras

app = Chalice(__name__)

@app.route("/occupancy/")
def occupancy():
    conn = psycopg2.connect("postgresql://getonly:Ew7uOPF4K1SxARyA0moRJA@hyping-wasp-8765.7tt.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full")
    
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("SELECT * FROM public.parkingoccupancy")
        res = cur.fetchall()
        conn.commit()
        ans1 = []
        for row in res:
            ans1.append(dict(row))

        return ans1


@app.route("/lotinfo/")
def lotinfo():
    conn = psycopg2.connect("postgresql://getonly:Ew7uOPF4K1SxARyA0moRJA@hyping-wasp-8765.7tt.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full")
    
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("SELECT * FROM public.lotinfo")
        res = cur.fetchall()
        conn.commit()
        ans1 = []
        for row in res:
            ans1.append(dict(row))

        return ans1

# import os
# import psycopg2

# # use export DATABASE_URL="postgresql://getonly:<ENTER-SQL-USER-PASSWORD>@hyping-wasp-8765.7tt.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full"
# # before running this script in python (replace export with set in windows)

# conn = psycopg2.connect(os.environ["DATABASE_URL"])

# with conn.cursor() as cur:
#     print("HERE")
#     cur.execute("SELECT * FROM public.parkingoccupancy")
#     res = cur.fetchall()
#     conn.commit()
#     print(res)