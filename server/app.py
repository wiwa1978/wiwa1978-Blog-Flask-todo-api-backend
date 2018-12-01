"""
appserver.py  
- creates an application instance and runs the dev server
"""

app_name = 'TODO-APP'
config_name = "development"  # config_name = "development"

if __name__ == '__main__':
    from todoapi.application import create_app
    app = create_app(app_name, config_name)
    app.run()
