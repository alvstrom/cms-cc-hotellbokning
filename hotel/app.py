from flask import Flask, request
from flask_cors import CORS 

PORT=8382

app = Flask(__name__)
CORS(app) # Tillåt cross-origin requests

@app.route("/")
def info():
    return {
        "Hotel API, endpoints /rooms, /bookings"
        
    } 

@app.route("/test", methods=['GET', 'POST'])  
def test():
    if request.method == 'POST':
        #skapa rad i databasen, returnera ny id..
        new_id = 555

        return {
            'msg' : f"DU skapade en ny rad i databasen, id är{new_id}",
            'method': request.method
        }
         
         
    else: 
            
        return {
            'msg' : "TESTING!",
            'method': request.method
        }


@app.route("/test/<int:id>", methods=['GET', 'PUT', 'DELETE', 'PATCH'])
def testId(id):
    if request.method == 'GET':
        return {
            'msg' : f"här får du id: {id}",
            'method': request.method
        }
    if request.method == 'PUT' or request.method == 'PATCH':
        return {
            'msg' : f"Du uppdaterar id: {id}",
            'method': request.method
        }
    if request.method == 'DELETE':
        return {
            'msg' : f"Du tar bort id: {id}",
            'method': request.method
        }


@app.route("/ip")
def ip():
    ip = request.remote_addr
    return {'ip': ip}





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True, ssl_context=(
        '/etc/letsencrypt/fullchain.pem', 
        '/etc/letsencrypt/privkey.pem'
    ))
