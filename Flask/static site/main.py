#we are making a website for an agency which provides services like promotions, video editing, etc.
#our render  template --> index.html is home.html 
#we took inspo from bootstrap from where we took the navigation bar code and made some changes as per our requirements then we copy pasted it to  all other html files because we want to show these navigation bars  in all options


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

app.run(debug=True)