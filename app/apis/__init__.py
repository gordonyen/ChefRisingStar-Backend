from flask_restx import Api

from .user import api as user_api
from .recipe import api as recipe_api

api = Api(
    title='Chef Rising Start API',
    version='1.0',
    description='test',
)

api.add_namespace(user_api, path='/api/user')
api.add_namespace(recipe_api, path='/api/recipe')