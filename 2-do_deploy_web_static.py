#!/usr/bin/python3

from fabric.api import local
from datetime import datetime
import os

"""
deploy web stack
"""

env.hosts = ['54.197.130.4', '52.91.160.210']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        archive_filename = os.path.basename(archive_path)
        split_no_ext = os.path.split(archive_filename)
        remote_tmp_path = '/tmp/' + archive_filename
        remote_extract_path = '/data/web_static/releases/' + archive_no_ext

        # Upload archive to tmp
        put(archive_path, remote_tmp_path)

        # Create directory for extraction
        run('mkdir -p {}'.format(remote_extract_path))

        # Uncompress the archive
        run(
                'tar -xzf {} -C {}'.format(
                    remote_tmp_path, remote_extract_path
                    ))

        # Remove the archive
        run('rm {}'.format(remote_tmp_path))

        # Move contents of extracted folder to release folder
        run(
                'mv {}/web_static/* {}'.format(
                    remote_extract_path, remote_extract_path
                    ))

        # remove empty web static folder
        run('rm -rf {}/web_static'.format(remote_extract_path))

        # Remove current symlink
        run('rm -rf /data/web_static/current')

        # Create new symlink
        run(
                'ln -s {} /data/web_static/current'.format(
                    remote_extract_path
                    ))

        print("New version deployed")
        return True
    except Exception as e:
        print("Deployment Failed:", e)
        return False
