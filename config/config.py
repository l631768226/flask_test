DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'info'
PASSWORD = '111111'
HOST = '192.168.4.58'
PORT = '3306'
DATABASE = 'info'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'\
    .format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

# 每次请求结束后会自动提交数据库中的变动
SQLALCHEMY_COMMIT_ON_TEARDOWN = True

# 事件系统跟踪修改
SQLALCHEMY_TRACK_MODIFICATIONS = False