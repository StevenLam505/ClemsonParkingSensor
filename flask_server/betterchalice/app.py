from chalice import Chalice, CORSConfig
import sys, os

app = Chalice(app_name='jsonapi')

sys.path.append("python/")

cors_config = CORSConfig(
    allow_origin='*'
)

# os.environ["PGSSLCRLDIR"] = "rootcert/"

import psycopg2 
import psycopg2.extras

@app.route("/occupancy", methods=['GET'], cors=cors_config)
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

@app.route("/lotinfo", methods=['GET'], cors=cors_config)
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

@app.route("/trenddata", methods=['GET'], cors=cors_config)
def trenddata():
    try:
        conn = psycopg2.connect(
            "postgresql://db:Kfvq8rgh6ti0UxVj8U_d6A@hyping-wasp-8765.7tt.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full",
            sslrootcert=os.path.abspath("rootcert/root.crt")
            )
        
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute("select * from public.dailyoccupancytrends order by date, time desc limit 100")
            res = cur.fetchall()
            conn.commit()
            ans1 = []
            for row in res:
                row1 = row.copy()
                row1['date'] = str(row1['date'])
                row1['time'] = str(row1['time'])
                ans1.append(dict(row1))

            return ans1
    except Exception as e:
        return {"error happened":str(e)}
