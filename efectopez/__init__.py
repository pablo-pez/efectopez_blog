from flask import Flask

from efectopez.core.views import core
from efectopez.blog.views import blog

app = Flask(__name__)

# Importar las vistas
app.register_blueprint(core)
app.register_blueprint(blog)
