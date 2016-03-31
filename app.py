from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

@app.route("/cpw.json")
def json():
	print "tried to get here"
	return render_template("cpw.json")

if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0', port=8000)