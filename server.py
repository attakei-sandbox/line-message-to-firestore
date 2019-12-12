#!/usr/bin/env python
import logging
import os
from bottle import Bottle, run


app = Bottle()
logging.basicConfig(level=logging.DEBUG)


@app.route('/hello')
def hello():
    logging.debug('Requested hello')
    return "Hello World!"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', '8080'))
    debug = bool(os.environ.get('DEBUG', False))
    run(app, host='0.0.0.0', port=port, debug=debug)
