import http.client
import urllib.parse
import json
from flask import Flask,jsonify, request
import socket


app = Flask(__name__)

server_host = 'localhost'
current_client_port = 13001

def send_message():
    try: 
        conn=http.client.HTTPConnection(server_host, 13000)
        req_data = {'message': 'Hello'}

        url = "/message_passing?"+urllib.parse.urlencode(req_data)
        conn.request('GET', url)
        response = conn.getresponse()

        if response.status == 200:
            response_content = json.loads(response.read().decode('utf-8'))
            print(response_content)

        else:
            print("Response not recieved")

    except Exception as e:
        print(f"Error message:{e}")

def establish_connection():
    global current_client_port
    try: 
        conn=http.client.HTTPConnection(server_host, 13000)

        client_host = 'localhost'
        req_data = {
                        'host': client_host, 
                        'port': current_client_port
                    }
        
        url = "/connect?"+ urllib.parse.urlencode(req_data)
        conn.request('POST', url)
        response = conn.getresponse()

        if response.status == 200:
            response_content = json.loads(response.read().decode('utf-8'))
            print(response_content)

        else:
            print("Response not recieved")

    except Exception as e:
        print(f"Error message:{e}")

@app.route('/get_pair_id')
def get_pair_id():
    data = request.args.get('data', '')
    print(data)
    response = {'message': 'success'}
    return json.dumps(response), 200

if __name__ == '__main__':
    send_message()
    establish_connection()
    app.run(host = 'localhost', port=current_client_port)
    current_client_port+=1