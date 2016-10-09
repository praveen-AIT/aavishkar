# This is the login route with basically handles the logging activities of the
# web application. For prototype purpose this route has not been made generic
# and only handles one username and password.

@app.route('/login', methods=["GET", "POST"])
def login():
	error = None
	if(request.method=="POST"):
		if(request.form['username'] == "admin" and request.form['password'] == "jenny"):
			session['logged_in'] = True
			return redirect(url_for('home'))

		else:
			error = "Invalid Credentials!!!"
	return render_template("login.html", error=error)
