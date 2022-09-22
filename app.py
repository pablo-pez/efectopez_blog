import os

from efectopez import app
from efectopez.utils.migration import migrate_templates, migrate_static

if __name__ == "__main__":
    # HTML templates
    migrate_templates(f'{os.getcwd()}/efectopez', "core")
    migrate_templates(f'{os.getcwd()}/efectopez', "blog")

    # Static files
    migrate_static(f'{os.getcwd()}/efectopez', "core")
    migrate_static(f'{os.getcwd()}/efectopez', "blog")

    # Run server
    app.run(debug=True)
