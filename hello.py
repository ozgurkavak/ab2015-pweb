from flask import render_template
from flask import Flask
app=Flask(__name__)
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(instructors=None):
  instructor=[
  "ozgur",  "KAVAK", "COMU"]
  return render_template('hello.html,instructors=instructors)
  
if __name__ in "main":
  app.run(port=8001.debug=True)
