#TODO: simplify
from sqlalchemy import create_engine
from sqlalchemy.orm import mapper
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql
pymysql.install_as_MySQLdb()

class Db:
    db_log = "root"
    db_pass = "Worldmw1337"
    db_url = "mysql://%s:%s@localhost/esystem" % (db_log, db_pass)
    def __init__(self, Base):
        self.Base = Base
        self.engine = create_engine(self.db_url) 
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_tables(self):
        self.Base.metadata.create_all(self.engine, checkfirst=True)
