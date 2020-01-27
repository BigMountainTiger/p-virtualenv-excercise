from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def message():
  name = 'Song Li'
  return jsonify(
    username = name,
    email = 'song.li@email.com',
  )

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=3000)