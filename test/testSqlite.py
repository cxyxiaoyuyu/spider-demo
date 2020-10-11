import sqlite3

# NULL Interger Real text blob  五种数据类型

conn = sqlite3.connect('test.db')  # 打开或创建数据库文件
print('opend database success')

c = conn.cursor()
# sql = '''
#   create table company
#     (
#       id int primary key not null,
#       name text not null,
#       age int not null,
#       address char(50),
#       salary real
#     );
# '''
# c.execute(sql)   # 执行sql语句
# conn.commit()    # 提交数据库操作
# conn.close()     # 关闭数据库连接
# print('成功建表')

sql1 = '''
  insert into company (id,name,age,address,salary)
  values (1,'张三','18','上海','12000');
'''
sql2 = '''
  insert into company (id,name,age,address,salary)
  values (2,'李四','18','北京','15000');
'''
c.execute(sql1)  
c.execute(sql2) 
conn.commit()    
conn.close()     