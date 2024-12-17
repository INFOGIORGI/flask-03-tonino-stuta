from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/prodotti")
def prodotti():
    prodotti = (("Pomodoro", "S1", 18), ("Salsa", "S2", 17), ("Formaggio", "S3", 14) )
    return render_template("details.html", prodotti = prodotti)
app.run(debug="true")

# @app.route("/prodottiScaffale/<scaffale>")
# def dettagliProdotti(scaffale)
    
    