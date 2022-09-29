from flask import Flask
from flask_restx import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('var1', type=str, help='variable 1')
parser.add_argument('var2', type=str, help='variable 2')

parser = reqparse.RequestParser()
parser.add_argument('var1', type=str, help='variable 1')
parser.add_argument('var2', type=str, help='variable 2')

parser = reqparse.RequestParser()
parser.add_argument('var1', type=str, help='variable 1')
parser.add_argument('var2', type=str, help='variable 2')


@api.route("/hello")
class HelloWorld(Resource):
    @api.doc(parser=parser)
    def get(self):
        args = parser.parse_args()
        get_var1 = args['var1']
        get_var2 = args['var2']
        return 'hello :' 'world' + get_var1 + get_var2


@api.route("/home")
class HomeSoftware(Resource):
    @api.doc(parser=parser)
    def post(self):
        args = parser.parse_args()
        post_var1 = args['var1']
        post_var2 = args['var2']
        return 'home :' 'software' + post_var1 + post_var2

@api.route("/delete")
class DeletePanel(Resource):
    @api.doc(parser=parser)
    def delete(self):
        args = parser.parse_args()
        delete_var1 = args['var1']
        delete_var2 = args['var2']
        return 'delete :' 'panel' + delete_var1 + delete_var2




if __name__ == '__main__':
    app.run(debug=True)
