#!/usr/bin/env python3

from fabric.api import local
from datetime import datetime

"""
pack web stack
"""


def do_pack():
    """Generate tgz archive"""

    local("mkdir -p versions")

    now = datetime.now()
    date_time = now.strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date_time)

    result = local("tar -cvzf {} web_static".format(file_name))

    if result.failed:
        return None
    else:
        return file_name
