from flask import Flask, send_from_directory
from flask_cors import CORS


"""
Configuration
"""
app = Flask(__name__, static_url_path='/html')
app.config["SECRET_KEY"] = 'vjti_super_duper_secret_k'
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/", defaults={'path': 'index.html'})
@app.route("/<path:path>")
def home(path):
    """
    If any static file is requested, return it from the directory
    instead of processing the request via route
    :param path: path of the file from html folder
    :return: file
    """
    return send_from_directory("html", path)


@app.errorhandler(404)
def page_not_found(e):
    """
    If a page is not found, return the index page instead of a 404 error,
    This is done to make single page website work properly
    :param e: error
    :return: index page
    """
    return send_from_directory("html", 'index.html')


@app.route("/api")
def api():
    """
    Route saved for api endpoint
    :return: static string
    """
    return "This routes are used for api"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
