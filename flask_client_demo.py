from flask import Flask, redirect, request, session, render_template
from umd_python_cas import UMDCASClient


app = Flask(__name__)

app.secret_key = "test12345"

client = UMDCASClient(host_name="http://127.0.0.1:5000", post_auth_route="/secure") 

@app.route('/', methods=["GET", "POST"])
def index():
	return render_template('index.html', user_id=session.get('username'))
	
@app.route('/login', methods=["GET", "POST"])
def login():
	return redirect(client.get_login_cas_url())

@app.route('/secure')
def secure():
	session['username'] = client.validate_ticket(request)
	return redirect('/')

@app.route('/logout')
def logout():
	session.clear()
	return redirect(client.get_logout_cas_url())

if __name__ == '__main__':
	app.run(debug=True)