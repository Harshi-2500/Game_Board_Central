import http.client
import urllib.parse
import json
from flask import Flask,jsonify, request


app = Flask(__name__)

server_host = 'localhost'

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
    try: 
        conn=http.client.HTTPConnection(server_host, 13000)

        url = "/connect?"
        conn.request('GET', url)
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
    data = request.data
    try: 
        d = json.loads(data)
        print(d)
        return 200
    except json.JSONDecodeError as e:
        print(f'{e}')
        return 404


if __name__ == '__main__':
    send_message()
    establish_connection()
    app.run(host = 'localhost', port=13001)