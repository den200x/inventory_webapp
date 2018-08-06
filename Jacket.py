from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMYU_DATABASE_URL']=''

@app.route("/")
def inventory():
    return "here is the page"

if __name__=="__main__":
    app.run()
    