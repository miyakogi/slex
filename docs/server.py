#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
from livereload import Server, shell

server = Server()
cmd = shell(['make', 'html'])

subprocess.run(['make', 'clean'])
subprocess.run(['make', 'html'])

server.watch('./*.py', cmd, ignore=None)
server.watch('./*.rst', cmd, ignore=None)
server.watch('./_static/*.css', cmd, ignore=None)
server.watch('./_templates/*.html', cmd, ignore=None)

server.watch('../*.rst', cmd, ignore=None)
server.watch('../slex/*.html', cmd, ignore=None)
server.watch('../slex/*.py', cmd, ignore=None)
server.watch('../slex/static/*.css_t', cmd, ignore=None)

server.serve(port=8889, root='_build/html', debug=True, restart_delay=1)
