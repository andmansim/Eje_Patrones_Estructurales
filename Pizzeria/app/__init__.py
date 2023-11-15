from flask import Flask
from app import routes
from codigoPizza import builders
app = Flask(__name__)

director = builders.Director() #Chef
builder = builders.ConcreteBuilder1() #Tipo de pizza
director.builder = builder #Le decimos al chef que tipo de pizza queremos
if __name__ == '__main__':
    app.run(debug=True)