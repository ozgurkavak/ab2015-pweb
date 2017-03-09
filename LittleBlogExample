from flask import Flask
from flask import request,render_template
from pymongo import Connection

app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
  db=Connection()["akademikbilisim"]
  table = db["message1"]
  
  list1=list(table.find())
  
  if request.method == 'POST':
    name=request.from.get("name")
    table.insert({"name":name,"massage":massage})
    
    return "Registration is complete <a href='/'>back</a>"
  else:
    return render_template("newForm.html",registrations=list1)
if __name__== "__main__":
  app.run(port=8000,debug=True)
