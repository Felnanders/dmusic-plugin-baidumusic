#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from xdg_support import get_cache_file

def encode_utf8(chars):    
    if isinstance(chars, basestring):
        if isinstance(chars, unicode):
            return chars.encode("utf-8")
        return chars
    return str(chars)


class JSONDict(dict):
    
    def __init__(self, *args, **kwargs):
        super(JSONDict, self).__init__(*args, **kwargs)
        
    def hasOwnProperty(self, key):    
        return self.has_key(key)
    
    
def get_cookie_file(name="baidumusic_cookie"):    
    return get_cache_file("%s/%s" % ("baidumusic", name))


def get_image(name):
    return os.path.join(os.path.dirname(__file__), "images", name)


    
    
