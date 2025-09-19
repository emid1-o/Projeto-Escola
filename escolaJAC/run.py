from siteMain import create_app
import os
from flask import abort
from flask_migrate import upgrade

app = create_app()



if __name__ == '__main__':
    app.run(debug=True)

