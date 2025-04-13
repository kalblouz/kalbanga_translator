from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/salut')
def json():
    data = {"message" : "Salut depuis Python !"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)