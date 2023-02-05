from chalice import Chalice

app = Chalice(app_name='jsonapi')

import os

os.environ['LD_LIBRARY_PATH'] = os.path.abspath("./psychopg2/")

import psycopg2 
import psycopg2.extras

@app.route("/occupancy")
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


@app.route("/lotinfo")
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