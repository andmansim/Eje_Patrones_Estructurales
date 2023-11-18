from flask import Flask
from apps import routes
from codigoPizza import builders

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)