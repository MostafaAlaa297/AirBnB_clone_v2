#!/usr/bin/env python3

from fabric.api import local
from datetime import datetime
import os

"""
pack web stack
"""

def do_pack():
    """Generate tgz archive"""
    try:
        local("mkdir -p versions")

        now = datetime.now()
        date_time = now.strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_" + date_time + ".tgz"


        local("tar -cvzf {} web_static".format(file_name))

        print("web_static packed {} -> {}Bytes".format(file_name, os.path.getsize(file_name)))

        return file_name
    
    except Exception as e:
        return None