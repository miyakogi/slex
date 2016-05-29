#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import path
import subprocess
from livereload import Server, shell

join = path.join
docdir = path.dirname(path.abspath(__file__))
doctreedir = join(docdir, '_build')
builddir = join(docdir, '_build')

server = Server()
cmd = shell(['sphinx-build', '-b', 'html', '-E', '-W', '-a',
             '-d', join(builddir, 'doctrees'),
             docdir, join(builddir, 'html'),
             ])

subprocess.run(['make', 'clean'])
subprocess.run(['make', 'html'])

server.watch('./*.py', cmd, ignore=None)
server.watch('./*.rst', cmd, ignore=None)
server.watch('./_static/*.css', cmd, ignore=None)
server.watch('./_templates/*.html', cmd, ignore=None)

server.watch('../*.md', cmd, ignore=None)
server.watch('../*.rst', cmd, ignore=None)
server.watch('../slex/*.html', cmd, ignore=None)
server.watch('../slex/*.py', cmd, ignore=None)
server.watch('../slex/static/*.css_t', cmd, ignore=None)

server.serve(port=8889, root='_build/html', debug=True, restart_delay=1)
