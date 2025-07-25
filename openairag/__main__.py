
import pyjokes
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def myapp():
    #message = "Invoking pyjokes from flask"
    #return message
    return {"joke": pyjokes.get_joke()}

if __name__ == "__main__":
	app.run()
