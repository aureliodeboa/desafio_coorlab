from flask import Flask, jsonify,json

app = Flask(__name__)

# Carregar os dados do arquivo JSON
with open('data.json', 'r') as f:
    data = json.load(f)

#all  trips
@app.route('/trips')
def get_all_trips():
    return jsonify(data)


app.run(debug=True, port=3000, host='localhost')

