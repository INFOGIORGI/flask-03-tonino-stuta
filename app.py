from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
prodotti = (("Pomodoro", "S1", 18), ("Salsa", "S2", 17), ("Formaggio", "S3", 14))

@app.route("/prodotti")
def details():
    return render_template("details.html", prodotti=prodotti)


@app.route("/prodottiScaffale/<scaffale>")
def dettagliProdotti(scaffale):
    listaProdotti = []
    print(scaffale)
    for prodotto in prodotti:
        if prodotto[1]==scaffale:
            listaProdotti.append(prodotto)
    return render_template("prodottiScaffale.html", tuple = listaProdotti)
    
app.run(debug="true")