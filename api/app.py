'''
Api entry point
'''

import os
import logging
import traceback

from config import create_app

# Initialize the logging
root = logging.getLogger()
root.setLevel(logging.DEBUG)

fh_debug = logging.FileHandler('./logs/debug.log', 'w+')
fh_debug.setLevel(logging.DEBUG)

fh_info = logging.FileHandler('./logs/info.log', 'w+')
fh_info.setLevel(logging.DEBUG)

fh_error = logging.FileHandler('./logs/error.log', 'w+')
fh_error.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh_debug.setFormatter(formatter)
fh_info.setFormatter(formatter)
fh_error.setFormatter(formatter)
ch.setFormatter(formatter)

root.addHandler(fh_debug)
root.addHandler(fh_info)
root.addHandler(fh_error)
root.addHandler(ch)

root.info('Logging initialized')

# Get the correct config
app = create_app(os.getenv('FLASK_ENV') or 'dev')
root.info('App created')


@app.errorhandler(Exception)
def errorhandler(error):
    root.error('Exception from main errorhandler: %s\nStacktrace: %s', error,
               traceback.format_exc())

root.debug('Errorhandler setup')

# Add controllers
root.debug('Registering controllers')
try:
    import src.controller.auth
    app.register_blueprint(src.controller.auth.authBlueprint,
                           url_prefix='{}/auth'.format(os.getenv('BASE_URL')))
    root.debug('Controllers registered')
except Exception as e:  # pylint: disable=broad-except; log any errors
    root.error('Exception while registering blueprints: %s\nStacktrace: %s', e,
               traceback.format_exc())

if __name__ == '__main__':

    # Run app
    try:
        root.info('Running app')
        app.run(host='0.0.0.0')
    except Exception as e:  # pylint: disable=broad-except; log any errors
        root.error('Exception in main(): %s\nStacktrace: %s', e,
                   traceback.format_exc())
