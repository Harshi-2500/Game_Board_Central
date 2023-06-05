from flask import Flask,jsonify, request


app = Flask(_name_)

@app.route('/message_passing')
def get_message():
    message = request.args.get('message', '')
    print(message)
    data = {'message': message}
    return jsonify(data), 200

if _name_ == '_main_':
    app.run()