from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
#from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import DataRequired, Length   #校验器

app = Flask(__name__)
bootstrap = Bootstrap(app)
#db = SQLAlchemy(app)
app.config.from_pyfile('config.py')

class Nameform(Form):
    #用户名
    name=StringField('name', validators=[DataRequired(message=u"用户名不能为空"),
        Length(10, 20, message=u'长度位于10~20之间')], render_kw={'placeholder': u'输入用户名'})
    #密码
    password=PasswordField('password', validators=[DataRequired(message=u"密码不能为空"),
        Length(10, 20, message=u'长度位于10~20之间')], render_kw={'placeholder': u'输入密码'})
    submit = SubmitField('submit')


@app.route('/')
def index():
    contents = {
        'username': 'Jason',
        'group': ['group1', 'group2', 'group3'],
        'user': {
            'name': 'jason',
            'age': '21',
            'country': 'china'
        }
    }
    return render_template('index.html', **contents)


@app.route('/login')
def login():
    return render_template('login.html')


# @app.route('/user/<name>')
# def user(name):
#     return 'Hello %s!' % name
#
# @app.route('/user/user_agent')
# def user_agent():
#     user_agent = request.headers.get('User_Agent')
#     return 'your browser is %s!' % user_agent

if __name__ == '__main__':
    app.run()
