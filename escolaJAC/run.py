from siteMain import create_app
import os
from flask import abort
from flask_migrate import upgrade

app = create_app()


@app.route('/<secret_key>/run-migrations')
def run_migrations(secret_key):
    if secret_key != os.environ.get('MIGRATION_KEY'):
        abort(403)
    try:
        upgrade()
        return "Migrações executadas com sucesso!"
    except Exception as e:
        return f"Erro ao executar migrações: {e}", 500



if __name__ == '__main__':
    app.run(debug=True)

