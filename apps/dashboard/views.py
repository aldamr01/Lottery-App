from flask import Blueprint
from flask import render_template

from apps.dashboard.models import Xmin2

dashboard_blueprint = Blueprint('Dashboard', __name__, template_folder="templates")

@dashboard_blueprint.route('/')
def index():
    fruits = ['Apel', 'Jeruk', 'Pisang', 'Duren']    
    
    return render_template('index.html', fruits=fruits, app_name=GeneralConfig.APP_NAME, ) 

@dashboard_blueprint.route('/halaman_kedua')
def halaman_kedua():
    return render_template('halaman_kedua.html')