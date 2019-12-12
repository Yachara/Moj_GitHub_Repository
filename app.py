from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('main.html')

@app.route("/login/")
def login():
	return render_template('login.html')

@app.route("/new_account/")
def new_account():
	return render_template('new_account.html')

@app.route("/password_change/")
def password_change():
	return render_template('password_change.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)
