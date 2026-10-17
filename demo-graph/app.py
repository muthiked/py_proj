from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import mysqldb
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import MetaData, true
from flask_mysqldb import mySQL
import mysql.connector
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Base(DeclarativeBase, MappedAsDataclass):
    metadata = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(column_0_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    })

class User(db.Model, Base):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]
    db = SQLAlchemy(model_class=Base)



with app.app_context():
    db.create_all()


@app.route('/')
def hello():
    print('My First API !!')

def conn():
    print('Connected')
    return conn

if __name__ == '__app__':
    hello()
