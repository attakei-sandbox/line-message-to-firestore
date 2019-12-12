#!/usr/bin/env python
import os
from bottle import route, run


@route('/hello')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', '8080'))
    debug = bool(os.environ.get('DEBUG', False))
    run(host='0.0.0.0', port=port, debug=debug)
