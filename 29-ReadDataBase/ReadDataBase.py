# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第二十九课 读取数据库
# 建议在第八讲之后查看
# 2018-10-30
#安装sqlalchemy模块,pycharm可以在setting里面安装,ide可以使用pip install sqlalchemy来安装
#安装pymysql模块,可以连接mysql,pycharm可以在setting里面安装,ide可以使用pip install pymysql来安装

import pyodbc
import sqlalchemy
import pandas as pd
# sqlalchemy 和 pandas 均可链接数据库，选择其一即可

# pandas 链接字符串
connection = pyodbc.connect('DRIVER={SQL Server}; SERVER=(local); DATABASE=AdventureWorks;USER=sa;PASSWORD=123456')
# sqlalchemy 链接字符串
engine = sqlalchemy.create_engine('mssql+pyodbc://sa:123456@(local)/AdventureWorks?driver=SQL+Server')
#engine=create_engine("mysql+pymysql://root:a5230411@localhost:3306/test",echo=True)    #连接mysql


# 由于数据库中使用单引号，此处使用双引号引用 SQL 语句
query = "SELECT FirstName, LastName FROM Person.Person"
df1 = pd.read_sql_query(query, connection)
df2 = pd.read_sql_query(query, engine)

pd.options.display.max_columns = 999
print(df1.head())
print(df2.head())
