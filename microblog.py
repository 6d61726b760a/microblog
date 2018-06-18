#from app import app

from app import app, db
from app.models import User, Post
app.config['DEBUG'] = True

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
