from flask import Flask, render_template, request, session


app = Flask(__name__, static_url_path="/static")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


notes = []

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
    
    return render_template("index.html", notes=notes)
