from flask import Flask, render_template, views, request
from functools import wraps
from datetime import datetime

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        username = request.args.get('username')
        if username and username == '123':
            return func(*args,**kwargs)
        else:
            return '请先登陆'
    return wrapper

class LoginView(views.MethodView):
    def get(self,error=None):
        return render_template('login.html',error=error)

    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')
        if username == '123' and password == '123':
            return '登陆成功'
        else:
            return self.get(error="账号或密码错误")


app.add_url_rule('/login/', view_func=LoginView.as_view('login'))

@app.route('/')
def index():
    context = {
        'position': -9,
        'people':['俊贤','雨彤'],
        'users':['jason1','jason2','jason3'],
        'create_time':datetime(2018,3,10,23,0,0),
        'persons':{
            'username'
        }
    }
    return render_template('index.html', **context)

@app.template_filter('handle_time')
def handle_time(time):
    if isinstance(time,datetime):
        now=datetime.now()
        timestamp=(now-time).total_seconds()
        if timestamp < 60:
            return '刚刚'
        elif timestamp >=60 and timestamp<60*60:
            minutes = timestamp/60
            return "%s分钟前" % int(minutes)
        elif timestamp >= 60*60 and timestamp < 60*60*24:
            hours = timestamp/(60*60)
            return "%s小时前" % int(hours)
        elif timestamp>=60*60*24 and timestamp<60*60*24*30:
            days = timestamp/(60*60*24)
            return "%s天前" % int(days)
        else:
            return time.strftime('%Y/%m/%d %H:%M')
    else:
        return time

@app.route('/setting/')
@login_required
def setting():
    return render_template('setting.html')

class ProfileView(views.View):
    decorators = [login_required]
    def dispatch_request(self):
        return '这是个人中心页面'

app.add_url_rule('/profile/',view_func=ProfileView.as_view('profile'))


if __name__ == '__main__':
    app.run(debug=True)
