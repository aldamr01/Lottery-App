from config import AppConfig, GeneralConfig
from apps.dashboard.views import dashboard_blueprint
from apps.lottery.views import lottery_blueprint
from basemodel import db

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(GeneralConfig.APP_NAME, template_folder='apps/templates')
app.config.from_object(AppConfig)

app.register_blueprint(dashboard_blueprint)
app.register_blueprint(lottery_blueprint)

db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':    
    app.run()
    