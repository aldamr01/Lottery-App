from config import AppConfig, GeneralConfig
from apps.dashboard.views import dashboard_blueprint
from apps.lottery.views import lottery_blueprint
from apps.auth.views import auth_blueprint
from extensions import db, csrf, login_manager

from flask import Flask
from flask_migrate import Migrate

app = Flask(
    GeneralConfig.APP_NAME,
    template_folder="apps/templates",
    static_folder="apps/static",
)
app.config.from_object(AppConfig)

app.register_blueprint(dashboard_blueprint)
app.register_blueprint(lottery_blueprint)
app.register_blueprint(auth_blueprint)

migrate = Migrate(app, db)

csrf.init_app(app)
db.init_app(app)
login_manager.init_app(app)

if __name__ == "__main__":
    app.run()
