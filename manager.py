from multiprocessing import managers
from flask_script import Manager
from flask_migrate import MigrateCommand
from shop import creat_app

app = creat_app()
manager = Manager(app)
manager.add_command('db',MigrateCommand)
if __name__ == '__main__':
    manager.run()