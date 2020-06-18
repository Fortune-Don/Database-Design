import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'gsolvit'

    @staticmethod
    def init_app(app):
        pass

config = {
    'default': Config,
    'MYSQL_PASSWORD': '102333',
    'DATABASE_NAME': 'studentTrainPlan'
}
 