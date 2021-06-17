from setuptools import setup

setup(
    name='ChefRisingStar-Backend',
    version='1.0',
    packages=['app', 'app.apis', 'app.apis.user', 'app.apis.recipe', 'app.apis.challenge', 'app.apis.achievement'],
    url='https://github.com/gordonyen/ChefRisingStar-Backend',
    license='',
    author='Gordon Yen',
    author_email='gordonyen@gmail.com',
    description='PoC'
)
