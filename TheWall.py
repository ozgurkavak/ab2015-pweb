import sys
from datetime import datetime
from flask import Flask, jsonify, request
from pymongo import Connection

app = Flask(__name__)
db = Connection()['thewall']

@app.route("/api/messages")
def hello():
    messages = db.messages.find().sort([
        ('date_sent', -1),    ])

    result = []

    for message in messages:
        result.append({
            "name": message.get("name"),            "message": message.get("message"),            "date_sent": message.get("date_sent"),        })

    return jsonify(messages=result)


@app.route('/api/messages', methods=['POST'])
def post_message():
    if request.json is None:
        request_data = request.form
    else:
        request_data = request.json

    data = {
        'name': request_data.get('name'),        'message': request_data.get('message'),        'date_sent': datetime.now()
    }
    db.messages.insert(data)
    del data['_id']
    return jsonify(data)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000    app.run(debug=True, host='0.0.0.0', port=port)
