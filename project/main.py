from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Insert_event(Resource):
    def get(self):
        #insert
        return {'teste':'testando'}, 200

api.add_resource(Insert_event, '/')

if __name__== '__main__':
    app.run(debug=True)