from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'sql_learn'
USERNAME = 'root'
PASSWORD = 'zxcvBnm123'

# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

engine = create_engine(DB_URI)

# 判断是否连接成功
# db = engine.connect()
# result = db.execute('select 1')
# print(result.fetchone())

### ORM介绍：
# 1. ORM：Object Relationship Mapping
# 2. 大白话：对象模型与数据库表的映射

Base = declarative_base(engine)

# Session = sessionmaker(engine)
# session = Session()
session = sessionmaker(engine)()


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    age = Column(Integer)
    number = Column(String(50))

    def __str__(self):
        return "<Student(name:%s,age:%s,studentnumber:%s)>" % (self.name, self.age,self.studentnumber)

Base.metadata.create_all()




# 增
# 创建对象，也即创建一条数据,将这个对象添加到`session`会话对象中,将session中的对象做commit操作（提交）
def add_data():
    p1 = Student(name='jason', age=19, number='20161380162')
    p2 = Student(name='lam', age=20, number='20161380254')
    session.add_all([p1, p2])
    session.commit()



if __name__ == '__main__':
    add_data()