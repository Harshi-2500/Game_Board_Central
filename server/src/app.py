from flask import Flask,jsonify, request


app = Flask(__name__)

@app.route('/message_passing')
def get_message():
    message = request.args.get('message', '')
    print(message)
    data = {'message': message}
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host = 'localhost', port=13000, threaded=True)