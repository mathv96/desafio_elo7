from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from validation.validate_event import validate_event


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
        #insert
        inputed_json = request.get_json()
        response_validation = validate_event(inputed_json)
        print(response_validation)
        if response_validation == False:
            response = jsonify(result="Please, send the right structure of event json.")
            response.status_code = 200
            return response
        else:    
            #dao will be called
            response = jsonify({'result':'Event saved.'})
            response.status_code = 201
            return response    

#routes
api.add_resource(Index, '/')
api.add_resource(Insert_event, '/insert_event')

if __name__== '__main__':
    app.run(debug=True)