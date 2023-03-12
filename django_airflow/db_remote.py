

from sqlalchemy import create_engine
import pymysql
import pandas as pd

pymysql.install_as_MySQLdb()
engine=create_engine("mysql+mysqld:/root"+"123"+"@Localhost/KIPRIS",encoding="utf-8")
conn=engine.connect()

frame.to_sql(name='mytable',con=engine,if_exists='append',index=False)
df3=pd.read_sql