from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Learning Devops with GIT as a beginner."
    return "Making few changes in this file and testing if that works"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
