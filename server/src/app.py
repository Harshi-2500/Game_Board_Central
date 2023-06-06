from flask import Flask,jsonify, request
import http.client
import urllib.parse


app = Flask(__name__)


clients_list = []
pairs = dict()
client_count = 0

@app.route('/message_passing')
def get_message():
    message = request.args.get('message', '')
    print(message)
    data = {'message': message}
    return jsonify(data), 200


@app.route('/connect', methods=['POST'])
def connect():
    client_host = request.args.get('host','')
    client_port = request.args.get('port','')
    global client_count
    curr_client_id = client_count
    client_pair_id = None

    if len(clients_list) == 0:
        client_info = {
            'host': client_host,
            'port': client_port,
            'id': curr_client_id
        }
        clients_list.append(client_info) 
    else:
        topmost_client = clients_list.pop(0)
        client_pair_id = topmost_client['id']
        pairs[client_pair_id] = curr_client_id
        pairs[curr_client_id] = client_pair_id 

        if(client_pair_id==0):
            client_host = topmost_client['host']
            client_port = topmost_client['port']
            
            conn = http.client.HTTPConnection(client_host, client_port)
            data = {
                'data': {
                    'client_id' : client_pair_id, 
                    'pair_id' : curr_client_id
                        }
                    }   
            url = "/get_pair_id?"+urllib.parse.urlencode(data)
            conn.request('GET', url)
            response = conn.getresponse()

    client_count += 1
    data = {
        'client_id': curr_client_id,
        'pair_id': client_pair_id
    }
    return jsonify(data),200


if __name__ == '__main__':
    app.run(host = 'localhost', port=13000, threaded=True)