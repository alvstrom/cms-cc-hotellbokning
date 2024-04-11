import os, psycopg
from psycopg.rows import dict_row
from flask import Flask, request
from flask_cors import CORS 
from dotenv import load_dotenv

load_dotenv()

PORT=8382

db_url = os.environ.get("DB_URL")
print(db_url)
print (os.environ.get("FOO"))

conn = psycopg.connect(db_url, autocommit=True, row_factory=dict_row)


app = Flask(__name__)
CORS(app) # Tillåt cross-origin requests

rooms=[
    { 'number': 101, 'type': "single"},
    { 'number': 202, 'type': "double"}, 
    { 'number': 303, 'type': "suite"} 
]

@app.route("/test")
def dbtest():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM people")
        rows = cur.fetchall()
        return rows
         
        
    

@app.route("/")
def info():
    return  "Hotel API, endpoints /rooms, /bookings"
        

@app.route("/bookings, methods=['GET', 'POST']")
def bookings():
    if request.method == 'POST':
         return {"skapa ny bokning"}        
    


    

@app.route("/rooms", methods=['GET', 'POST'])  
def rooms_endpoint():
    if request.method == 'POST':
        request_body = request.get_json()
        print(request_body)
        rooms.append(request_body)
        return {
            'msg' : f"DU skapade ett nytt rum, id{len(rooms)-1}",

        }
         
         
    else: 
        with conn.cursor() as cur:   
            cur.execute("SELECT * FROM hotel_room ORDER BY room_number")
            rows = cur.fetchall()
            return rows     
        


@app.route("/rooms/<int:id>", methods=['GET', 'PUT', 'DELETE', 'PATCH'])
def one_room_endpoint(id):
    if request.method == 'GET':
            with conn.cursor() as cur:   
                        cur.execute("""SELECT *
                                     FROM hotel_room
                                        WHERE id = %s""", [id,])
                        return cur.fetchone()
            
    
@app.route("/ip")
def ip():
    ip = request.remote_addr
    return {'ip': ip}





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True, ssl_context=(
        '/etc/letsencrypt/fullchain.pem', 
        '/etc/letsencrypt/privkey.pem'
    ))
