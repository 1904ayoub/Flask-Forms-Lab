from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "llo2ay"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina","noor","messi","adi","afu","majd","joelle","yoav","bouls"]


@app.route('/',methods=['GET','POST'])  # '/' for the default page
def login():
	if request.method=='POST':
		username1=request.form['username']
		password1=request.form['password']
		if username == username1 and password==password1:
			return redirect(url_for('home'))

	return render_template('login.html')

@app.route('/home')
def home():
	return render_template('home.html',facebook_friends=facebook_friends)
@app.route('/friend_exists/<string:name>',methods=['GET','POST'])
def friend(name):
	if name in facebook_friends:
		result=True
	else:
	 result=False	
	return render_template('friend_exists.html',name=name,result=result)
if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)