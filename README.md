# flask-demo
## Using this Demo
First, git clone and navigate inside the directory by running these commands:
```bash
git clone https://github.com/umd-python-cas/flask-demo.git
cd flask-demo
```
Then, install the dependencies:
```bash
pip install -r requirements.txt
```
Finally, run the flask webserver locally. The environment variable `FLASK_APP` tells flask what python file to run, and `FLASK_DEBUG` tells flask to restart the server when any changes are made to the code.
```bash
FLASK_APP=flask_client_demo.py \
FLASK_DEBUG=1 \
flask run
```
Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser to view the app.
## Starting from Scratch
The following are instructions on how this template was made, so you can better understand how to integrate umd-cas-python into your project.
### Installation
First, install flask and umd-python-cas, and create a new folder for the project, by running these commands:
```bash
pip install flask umd-python-cas
mkdir flask-demo
cd flask-demo
```
### App Files
Create a file `flask_client_demo.py` with the contents of [this file](flask_client_demo.py). In the file, change `app.secret_key = "test12345"` to be a random value.

Create a folder `templates` by running `mkdir templates`.

Create a file `templates/index.html` with the contents of [this file](templates/index.html).
### Run
Run the flask webserver locally. The environment variable `FLASK_APP` tells flask what python file to run, and `FLASK_DEBUG` tells flask to restart the server when any changes are made to the code.
```bash
FLASK_APP=flask_client_demo.py \
FLASK_DEBUG=1 \
flask run
```
Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser to view the app.
