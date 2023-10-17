import connexion
from flask import render_template

import prometheus

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    # Start up the server to expose the metrics.
    prometheus.start_prometheus() 
    
    # Start up the flask server
    app.run(host="0.0.0.0", port=8080, debug=False)