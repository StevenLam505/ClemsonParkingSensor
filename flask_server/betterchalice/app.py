from chalice import Chalice
import sys, os

app = Chalice(app_name='jsonapi')

sys.path.append("python/")

# os.environ["PGSSLCRLDIR"] = "rootcert/"

import psycopg2 
import psycopg2.extras

@app.route("/occupancy")
def occupancy():
    try:
        conn = psycopg2.connect(
            "postgresql://db:Kfvq8rgh6ti0UxVj8U_d6A@hyping-wasp-8765.7tt.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full",
            sslrootcert=os.path.abspath("rootcert/root.crt")
            )
        
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute("SELECT * FROM public.parkingoccupancy")
            res = cur.fetchall()
            conn.commit()
            ans1 = []
            for row in res:
                ans1.append(dict(row))

            return ans1
    except Exception as e:
        return {"error happened":str(e)}

@app.route("/lotinfo")
def lotinfo():
    try:
        conn = psycopg2.connect(
            "postgresql://db:Kfvq8rgh6ti0UxVj8U_d6A@hyping-wasp-8765.7tt.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full",
            sslrootcert=os.path.abspath("rootcert/root.crt")
            )
        
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute("SELECT * FROM public.lotinfo")
            res = cur.fetchall()
            conn.commit()
            ans1 = []
            for row in res:
                ans1.append(dict(row))

            return ans1
    except Exception as e:
        return {"error happened":str(e)}
