import flask_restx

api = flask_restx.Namespace('recipe', description='recipe api endpoint')

ingredient = api.model('Ingredient', {
    'name': flask_restx.fields.String(required=True, description='name'),
    'quantity': flask_restx.fields.Float(required=True, description='quantity'),
    'measurement': flask_restx.fields.String(required=True, description='measurement'),
})

recipe = api.model('Recipe', {
    'id': flask_restx.fields.String(required=True, description='identifier'),
    'name': flask_restx.fields.String(required=True, description='name'),
    'ingredients': flask_restx.fields.List(flask_restx.fields.Nested(ingredient))
})

recipes = [
    {
        "id": "2e48b2bf-3273-4b02-9efa-7369480d7413",
        "name": "popcorn",
        "ingredients": [
            {
                "name": "uncooked popcorn kernels",
                "quantity": "0.5",
                "measurement": "cup"
            },
            {
                "name": "popcorn popping oil",
                "quantity": "1",
                "measurement": "tsp"
            },
            {
                "name": "uncooked popcorn kernels",
                "quantity": "1",
                "measurement": "tsp"
            }
        ]
    },
            {
                "id": "a32cc083-bf7d-49da-9b3d-9cc7dd764d09",
                "name": "Guacamole",
                "ingredients": [
                    {
                        "name": "avocado",
                        "quantity": "5",
                        "measurement": "count"
                    },
                    {
                        "name": "fresh lemon juice",
                        "quantity": "2",
                        "measurement": "tbsp"
                    },
                    {
                        "name": "minced green onion",
                        "quantity": "0.75",
                        "measurement": "cup"
                    },
                    {
                        "name": "minced fresh cilantro",
                        "quantity": "0.5",
                        "measurement": "cup"
                    },
                    {
                        "name": "salt",
                        "quantity": "1",
                        "measurement": "count"
                    },
                    {
                        "name": "pepper",
                        "quantity": "1",
                        "measurement": "count"
                    },
                ]
            },
]


@api.route('/')
class RecipeList(flask_restx.Resource):
    @api.doc('list_recipes')
    @api.marshal_list_with(recipe)
    def get(self):
        return recipes


@api.route('/<name>')
@api.param('name', 'name')
@api.response(404, 'not found')
class Recipe(flask_restx.Resource):
    @api.doc('get_recipe')
    @api.marshal_with(recipe)
    def get(self, name):
        for recipe in recipes:
            if recipe['name'] == name:
                return recipe
        api.abort(404)
