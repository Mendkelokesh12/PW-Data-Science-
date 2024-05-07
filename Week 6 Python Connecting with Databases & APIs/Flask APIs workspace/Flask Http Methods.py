from flask import  Flask

app =  Flask(__name__)

@app.rote("//")
def hellp_world():
    return "<h1>Hello, world!</h1>"

if __name__=="__main__":
    app.run(host="0.0.0.0")
