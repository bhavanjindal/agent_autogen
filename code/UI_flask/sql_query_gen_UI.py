from flask import Flask, render_template
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/gensql")
def gensql():
    return render_template("index_sql.html")




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3002)


