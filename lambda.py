#!/usr/bin/python3
from splitter import Splitter

import json

def lambdaPdfSplitter(event, context=None):
    print(json.dumps(event))
    spliter = Splitter()
    spliter.split(event)
    return True
