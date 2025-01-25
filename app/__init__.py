from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'uploads/'

    # Ensure the uploads directory exists
    import os
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    with app.app_context():
        # Import parts of our application
        from . import app as main_app
        app.register_blueprint(main_app.bp)

        # Register error handlers
        app.register_error_handler(404, main_app.page_not_found)
        app.register_error_handler(500, main_app.internal_server_error)

    return app

