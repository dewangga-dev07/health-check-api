from flask import Flask
import redis

app = Flask(__name__)
data = redis.Redis(host="redis", port=6379, decode_responses=True)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/visit")
def visit():
    jumlah = data.incr("visit")
    return {"visit": jumlah}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
