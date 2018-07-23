# from email.mime.text import MIMEText
# msg = MIMEText('hello,send by python...','plain','utf-8')
#
# from_addr = input('From:')
# password = input('Password:')
# to_addr = input('To:')
# smtp_server = input('SMTP server:')
#
# import  smtplib
# server = smtplib.SMTP(smtp_server,25)
# server.set_debuglevel(1)
# server.login(from_addr,password)
# server.sendmail(from_addr,[to_addr],msg.as_string())
# server.quit()

#
#
# import mysql.connector
# conn = mysql.connector.connect(user='root',password='111111',database='test')
# cursor = conn.cursor()
#
# cursor.execute('create table user(id VARCHAR (20) PRIMARY key ,name VARCHAR (20))')
# cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
# cursor.rowcount
# conn.commit()
# cursor.close()
#
# cursor = conn.cursor()
# cursor.execute('select * from user where id = %s', ('1',))
# values = cursor.fetchall()
# print(values)
# cursor.close()
# conn.close()



from sqlalchemy import  Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(String(20),primary_key=True)
    name = Column(String(20))


engine = create_engine('mysql+mysqlconnector://root:111111@localhost:3306/test')
DBSession = sessionmaker(bind=engine)
#
# print('ok')

# # 创建session对象:
# session = DBSession()
# # 创建新User对象:
# new_user = User(id='5', name='Bob')
# # 添加到session:
# session.add(new_user)
# # 提交即保存到数据库:
# session.commit()
# # 关闭session:
# session.close()

# # 创建Session:
# session = DBSession()
# # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
# user = session.query(User).filter(User.id=='5').one()
# # 打印类型和对象的name属性:
# print('type:', type(user))
# print('name:', user.name)
# # 关闭Session:
# session.close()

def application (environ, start_response):
    start_response('200 ok',[('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']