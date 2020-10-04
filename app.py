from flask import Flask, request, redirect, render_template, jsonify, make_response


app = Flask(__name__)


@app.route('/',methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        return render_template("index.html")

    return render_template("index.html")




if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
