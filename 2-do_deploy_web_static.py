#!/usr/bin/python3

from fabric.api import run, put, env
import os

"""
deploy web stack
"""

env.hosts = ['54.197.130.4', '52.91.160.210']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not os.path.isfile(archive_path):
        return False
    try:
        filename = archive_path.split("/")[-1]
        name = filename.split(".")[0]

        # Upload archive to tmp
        if put(archive_path, "/tmp/{}".format(filename)).failed is True:
            return False

        # Create directory for extraction
        if run('mkdir -p {}'.format("/data/web_static/releases/{}").format(name)).failed is True:
            return False

        # Uncompress the archive
        if run(
                'tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(
                    filename, name
                    )).failed is True:
            return False

        # Remove the archive
        if run('rm {}'.format(filename)).failed is True:
            return False

        # Move contents of extracted folder to release folder
        if run(
                'mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}'.format(
                    name, name
                    )).failed is True:
            return False

        # remove empty web static folder
        if run('rm -rf /data/web_static/releases/{}/web_static'.format(name)).failed is True:
            return False

        # Remove current symlink
        if run('rm -rf /data/web_static/current').failed is True:
            return False

        # Create new symlink
        if run(
                'ln -s /data/web_static/releases/{} /data/web_static/current'.format(
                    name
                    )).failed is True:
            return False

        print("New version deployed")
        return True
    except Exception as e:
        print("Deployment Failed:", e)
        return False
