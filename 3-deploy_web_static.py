#!/usr/bin/python3

from fabric.api import local, run, put, env
from datetime import datetime
import os

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

"""
deploy web stack
"""

env.hosts = ['54.197.130.4', '52.91.160.210']


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not archive_path:
        print("False archive_path")
        return False
    try:
        filename = archive_path.split("/")[-1]
        name = filename.split(".")[0]
        release_path = "/data/web_static/releases"
        full_path = "/data/web_static/releases/{}/".format(name)

        # Remove dir and achive name if exists
        if run("rm -rf {}/{}".format(release_path, name)).failed is True:
            print("False")
            return False

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(full_path))

        # Uncompress the archive
        if run(
                'tar -xzf /tmp/{} -C {}/{}'.format(
                    filename, release_path, name
                    )).failed is True:
            print("False")
            return False

        # Remove the archive
        if run('rm /tmp/{}'.format(filename)).failed is True:
            print("False")
            return False

        # Move contents of extracted folder to release folder
        if run(
                'mv {}/{}/web_static/* {}/{}'.format(
                    release_path, name, release_path, name
                    )).failed is True:
            print("False")
            return False

        # remove empty web static folder
        if run(
                'rm -rf {}/{}/web_static'.format(
                    release_path, name)).failed is True:
            print("False")
            return False

        # Remove current symlink
        if run('rm -rf /data/web_static/current').failed is True:
            return False

        # Create new symlink
        if run(
                'ln -s {}/{}/ /data/web_static/current'.format(
                    release_path, name
                    )).failed is True:
            return False

        print("New version deployed")
        return True
    except Exception as e:
        print("Deployment Failed:", e)
        return False

def deploy():
    """
    creates and distributes
    an archive to your web servers
    """
    archive_path = do_pack()
    if not archive_path:
        return False
