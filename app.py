from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    return (jsonify({ 'test': 'test prediction results'}))

if __name__ == '__main__':
  app.run()