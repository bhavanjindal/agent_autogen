
from flask import Flask, request
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

app = Flask(__name__)

@app.route("/gensql", methods=["POST"])
def generate_sql():
    load_dotenv()
    data = request.get_json()
    sql_instruction = data["table_description"]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are a sql expert who can write very good sqls."},
            {"role": "user", "content": sql_instruction}
        ],
        max_tokens=200,
        temperature=0.5,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    """ This app will run on port 3000 on the host and return the SQL query based on user input 
    by doing a post with endpoint /gensql and mentioning the requirement in JSON format 
    e g :
    {
    "table_description": "can you write a query to find out department with highest average salary by joining it with employee table on a column dep_id"
    }
    """
    app.run(debug=True, host="0.0.0.0", port=3000)

