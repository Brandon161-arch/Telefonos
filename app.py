from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():

    telefono= [ {"nombre": "iPhone 13", "precio": 3500000, "imagen": "iphone.jpg"},
        {"nombre": "Samsung S2", "precio": 3200000, "imagen": "samsung.jpg"},
        {"nombre": "Xiaomi Redmi Note 12", "precio": 1200000, "imagen": "xiaomi.jpg"}]
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

