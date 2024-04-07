from flask import Flask, request
from flask_cors import CORS 

PORT=8382

app = Flask(__name__)
CORS(app) # Tillåt cross-origin requests

rooms =[
    { 'number': 101, 'type': "single"},
    { 'number': 202, 'type': "double"}, 
    { 'number': 303, 'type': "suite"} 
]

@app.route("/")
def info():
    return  "Hotel API, endpoints /rooms, /bookings"
        
    

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
        return rooms
            
        


@app.route("/rooms/<int:id>", methods=['GET', 'PUT', 'DELETE', 'PATCH'])
def one_room_endpoint(id):
    if request.method == 'GET':
        return rooms[id]
        
    
@app.route("/ip")
def ip():
    ip = request.remote_addr
    return {'ip': ip}





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True, ssl_context=(
        '/etc/letsencrypt/fullchain.pem', 
        '/etc/letsencrypt/privkey.pem'
    ))
