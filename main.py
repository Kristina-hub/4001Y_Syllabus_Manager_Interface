from flask import Flask, render_template

#application = Flask(__name__)
#@application.route('/')
app = Flask(__name__)
@app.route("/")

# def hello_world():
# 	return 'Hello World'

def main.index():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0',port=5000)