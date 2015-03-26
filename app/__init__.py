from flask import Flask, render_template
# from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('app.config')
# db = SQLAlchemy(app)
from app.core.views import mod as core

app.register_blueprint(core)
# Aqui registras el resto de blueprints de la misma forma::
#from app.comments.views import mod as commentsModule
#from app.posts.views import mod as postsModule
#app.register_blueprint(commentsModule)
#app.register_blueprint(postsModule)