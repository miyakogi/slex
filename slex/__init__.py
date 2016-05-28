#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path

def get_path():
    return path.dirname(path.dirname(path.abspath(__file__)))

def setup(app):
    return {'version': '0.0.1'}

