from flask import Flask, request, jsonify
import json
app = Flask(__name__)
@app.route('/', methods=['GET'])
def postback():
    print('postback')
    print(request.json)
    return json.dumps({
        'body': request.data.decode('utf-8')}
                      )

if __name__ == '__main__':
    app.run(host= '192.168.18.71', port="5000", debug=True)
