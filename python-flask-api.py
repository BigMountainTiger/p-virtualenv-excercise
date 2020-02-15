import sys, os, time
from threading import Thread, current_thread
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def message():
  time.sleep(10)
  return jsonify(pid = os.getpid(), thread = current_thread().name)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=3000)