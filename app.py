from flask import Flask, render_template

app = Flask(__name__)

# Define a list of user dictionaries with some initial data
USERS = [
    {
      'name': 'Alice', 
      'experience':'Great service! My confidence in working without the insecurity is now long gone.'
    },
    {
      'name': 'Bob', 
      'experience': 'I love the site experience.',
    },
    {
       'name': 'Charlie', 'experience': 'Terrible service.'
    }
]

@app.route("/")
def MwangaFloat():
  return render_template('home.html',
                              user_experience=USERS)

@app.route("/api/user_experience")
def user_experience():
  return jsonify(USERS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
