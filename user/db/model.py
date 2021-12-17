from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, DateTime
from user import app

app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'm_user'
    id = Column('mu_id', Integer, primary_key=True, autoincrement=True)

    first_name = Column('mu_first_name', String(80), nullable=False)

    last_name = Column('mu_last_name', String(80))

    age = Column('mu_age', Integer)

    mail_id = Column('mu_mail_id', String(80))

    created_date_time = Column('mu_created_date_time', DateTime, nullable=False)

    modified_date_time = Column('mu_modified_date_time', DateTime)


