from flask import Flask
from routes.labRoutes import lab_blueprint
from datetime import timedelta
from flask_jwt_extended import JWTManager

# Initialize the Flask app
app = Flask(__name__)

# Setup the Flask-JWT-Extended extension

app.secret_key = "9514bcfe52538f01f1e4de931fbb272f5e60b65dc6ada80080ea4ccdd4929dd2"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours= 1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(hours= 1)
jwt = JWTManager(app)

app.register_blueprint(lab_blueprint)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)