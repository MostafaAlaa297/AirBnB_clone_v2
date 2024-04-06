#!/usr/bin/python3

__import__('1-pack_web_static')
__import__('2-2-do_deploy_web_static')
"""
deploy web stack
"""


def deploy():
    """
    creates and distributes
    an archive to your web servers
    """
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)
