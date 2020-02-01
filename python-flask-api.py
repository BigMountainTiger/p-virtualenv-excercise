import sys, os
from flask import Flask, request, jsonify

app = Flask(__name__)

port = 3000
if len(sys.argv) > 1:
  port = int(sys.argv[1])

@app.route('/')
def message():
  name = 'Song Li'
  return jsonify(
    username = name,
    email = 'song.li@email.com',
    pid = os.getpid(),
    port = port
  )

@app.route('/port')
def getPort():
  return jsonify(
    port = port
  )

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=port)