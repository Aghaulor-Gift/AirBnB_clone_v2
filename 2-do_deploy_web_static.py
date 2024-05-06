#!/usr/bin/python3
# Fabric script (based on the file 1-pack_web_static.py) that distributes an
# archive to your web servers, using the function do_deploy
from fabric.api import env, put, run
import os


env.user = 'ubuntu'
env.key_filename = '/path/to/your/ssh/private/key.pem'
env.hosts = ['52.91.134.237', '54.158.211.199']


def do_deploy(archive_path):
    """Distribute an archive to web servers and deploy it."""

    # Check if the archive exists
    if not os.path.exists(archive_path):
        return False

    # Extract the archive filename without extension
    filename_ext = os.path.basename(archive_path)
    filename = os.path.splitext(filename_ext)[0]

    run('mkdir -p /data/web_static/releases/{}/'.format(filename))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
        filename_ext, filename))

    # Delete the archive from the servers
    run('rm /tmp/{}'.format(filename_ext))

    # Move contents to the proper location and remove unnecessary folder
    run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases
        /{}/'.format(filename, filename))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(filename))

    # Delete the symbolic link /data/web_static/current from the servers
    run('rm -rf /data/web_static/current')

    # New symbolic link /data/web_static/current linked to the new version
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(
        filename))

    return True
