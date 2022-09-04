from flask import Blueprint
from flask import render_template

from apps.lottery.models import Lottery

dashboard_blueprint = Blueprint('dashboard', __name__, template_folder="templates")

@dashboard_blueprint.route('/')
def index():
    lotteries = Lottery.query.all()
    for lottery in lotteries:
        print(lottery.description)
        
    return render_template('index.html', lotteries=lotteries) 

@dashboard_blueprint.route('/create')
def create():
    return render_template('create.html')