#!/usr/bin/env python
import logging
import os
from bottle import route, run


logging.basicConfig(level=logging.DEBUG)


@route('/hello')
def hello():
    logging.debug('Requested hello')
    return "Hello World!"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', '8080'))
    debug = bool(os.environ.get('DEBUG', False))
    run(host='0.0.0.0', port=port, debug=debug)
