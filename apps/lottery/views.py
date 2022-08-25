from flask import Blueprint
from flask import render_template

from apps.lottery.models import Lottery

lottery_blueprint = Blueprint('Lottery', __name__, template_folder="templates")

@lottery_blueprint.route('/lottery/')
def index():
    return render_template('index.html')

