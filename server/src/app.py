from flask import Flask,jsonify, request


app = Flask(__name__)


clients = []
pairs = dict()
client_count = 0

@app.route('/message_passing')
def get_message():
    message = request.args.get('message', '')
    print(message)
    data = {'message': message}
    return jsonify(data), 200


@app.route('/connect')
def connect():
    global client_count
    curr_client_id = client_count
    client_pair_id = None

    if len(clients) == 0:
        clients.append(curr_client_id) 
    else:
        client_pair_id = clients.pop()
        pairs[client_pair_id] = curr_client_id
        pairs[curr_client_id] = client_pair_id
    
    client_count += 1
    data = {
        'client_id': curr_client_id,
        'pair_id': client_pair_id
    }
    return jsonify(data),200

if __name__ == '__main__':
    app.run(host = 'localhost', port=13000, threaded=True)