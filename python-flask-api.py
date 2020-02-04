import sys, os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def message():
  return jsonify(pid = os.getpid())

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=3000)