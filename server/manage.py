"""
manage.py  
- provides a command line utility for interacting with the
  application to perform interactive debugging and setup
"""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from todoapi.application import create_app
from todoapi.models import db, Todo

app_name = 'TODO-APP'
config_name = "development"
app = create_app(app_name, config_name)

migrate = Migrate(app, db)
manager = Manager(app)

# provide a migration utility command
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
