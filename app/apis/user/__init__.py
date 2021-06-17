from flask_restx import Namespace, Resource, fields

api = Namespace('user', description='user api endpoint')

user = api.model('User', {
    'id': fields.String(required=True, description='identifier'),
    'username': fields.String(required=True, description='username'),
})

users = [
    {
        "id": "9cff5231-7c5a-4fc8-9edc-b9b7aafca058",
        "username": "Felix"
    },
    {
        "id": "4cb3b039-99d4-4f4d-a4b5-bd54660cc68c",
        "username": "Adelaida"
    },
    {
        "id": "574b2c58-ffbf-467d-a30d-8abaca49b2af",
        "username": "Adey"
    },
    {
        "id": "68fc5722-56d2-4e01-8a62-21ddc4076ec0",
        "username": "Layney"
    },
    {
        "id": "10e8b880-c25f-4e51-8e1d-a7a80a5fd6a4",
        "username": "Rochella"
    },
    {
        "id": "01fd79ac-51f8-41dd-913c-dcfd63fd3bbb",
        "username": "Georgia"
    },
    {
        "id": "7bf132e3-3ca4-4848-ab6f-89d8abedffb9",
        "username": "Trudy"
    }
]


@api.route('/')
class UserList(Resource):
    @api.doc('list_users')
    @api.marshal_list_with(user)
    def get(self):
        return users


@api.route('/<name>')
@api.param('name', 'username')
@api.response(404, 'not found')
class User(Resource):
    @api.doc('get_user')
    @api.marshal_with(user)
    def get(self, name):
        for user in users:
            if user['username'] == name:
                return user
        api.abort(404)
