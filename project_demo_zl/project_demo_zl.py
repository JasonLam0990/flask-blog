from flask import Flask, render_template,request,redirect,url_for,session
import config
from models import User,Release
from exts import db
# from decorators import login_required

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        stunumber = request.form.get('stunumber')
        password = request.form.get('password')
        user = User.query.filter(User.stunumber == stunumber,User.password == password).first()
        if user:
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return u'学号或者密码错误，请确认后再输入'

@app.route('/release',methods=['GET','POST'])
# @login_required
def release():
    if request.method == 'GET':
        return render_template('release.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        Release(title=title, content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id==user_id).first()
        release.author = user
        db.session(release)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        username = request.form.get('username')
        stunumber = request.form.get('stunumber')
        password = request.form.get('password')
        telephone = request.form.get('telephone')

        user = User.query.filter(User.stunumber==stunumber).first()
        if user:
            return u'该学号已被注册，请重新确认'
        else:
            user = User(username=username, stunumber=stunumber, password=password, telephone=telephone)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
if __name__ == '__main__':
    app.run()

# if password1 != password2:
#     return u'两次密码输入不一致，请核对后再填写'
# else: