import sys
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def message():
  name = 'Song Li'
  return jsonify(
    username = name,
    email = 'song.li@email.com',
  )

port = 3000
if len(sys.argv) > 1:
  port = sys.argv[1]

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=port)