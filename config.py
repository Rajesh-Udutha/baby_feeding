import os
from datetime import timedelta

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1234@localhost:3377/baby_feeding"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)

