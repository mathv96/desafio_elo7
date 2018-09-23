from flask import Flask, request, jsonify
from flask_restful import Resource, Api

from validation.validate_event import validate_event
from DAO.insert import insert_event
from DAO.create_table import create_table


app = Flask(__name__)
api = Api(app)

#def to the execution of each route
class Index(Resource):
    def get(self):
        response = jsonify({'result':'API is working.'})
        response.status_code = 200
        return response

class Insert_event(Resource):
    def post(self):
        inputed_json = request.get_json()
        response_validation = validate_event(inputed_json)
        print(response_validation)
        if response_validation == False:
            response = jsonify(result="Please, send a request with the right json structure.")
            response.status_code = 200
            return response
        else:    
            response_creatiion = create_table()
            response_insert = insert_event(inputed_json)
            if response_insert:
                response = jsonify({'result':'Event saved.'})
                response.status_code = 201
                return response
            else:
                response = jsonify({'result':'Event was not saved.'})
                response.status_code = 200
                return response    

#routes
api.add_resource(Index, '/')
api.add_resource(Insert_event, '/insert_event')

if __name__== '__main__':
    app.run(debug=True)