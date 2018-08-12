import os
import sys
from flask_script import Manager, Server

sys.path.append(os.path.abspath(os.path.join
                                (os.path.dirname(__file__), '..')))
from blog_with_flask import app
from flask_migrate import MigrateCommand

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver',
                    Server(use_debugger=True,
                           use_reloader=True,
                           host=os.getenv('IP', '0.0.0.0'),
                           port=int(os.getenv('PORT', 5000))))

if __name__ == "__main__":
    manager.run()
