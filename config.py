import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1234@localhost:3377/baby_feeding"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

