from flask_app import create_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_app import db

app = create_app()
manager = Manager(app)
Migrate(app, db)
#  MigrateCommand  是一个Command对象
manager.add_command('db', MigrateCommand)

# 函数名test和上面的'db'一样
# python3 manage.py test -n=jack 或者 python3 manage.py test -n jack
@manager.option('-n', '--name', dest='name')
def test(name, url):
    print(name, url)

if __name__ == '__main__':
    manager.run()



