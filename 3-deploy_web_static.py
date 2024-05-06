#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers, using the function deploy
"""
from fabric.api import env, run
from fabric.operations import put
from fabric.contrib.files import exists
from datetime import datetime
import os


env.user = 'ubuntu'
env.hosts = ['52.91.134.237', '54.158.211.199']


def do_pack():
    """Create a compressed archive of the web_static folder."""
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timestamp)
    local("mkdir -p versions")
    local("tar -czvf {} web_static".format(archive_path))
    return archive_path

def do_deploy(archive_path):
    """Distribute an archive to web servers and deploy it."""
    if not os.path.exists(archive_path):
        print("Archive {} doesn't exist".format(archive_path))
        return False

    
    filename_ext = os.path.basename(archive_path)
    filename = os.path.splitext(filename_ext)[0]

    put(archive_path, '/tmp/')

    run('mkdir -p /data/web_static/releases/{}/'.format(filename)
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(filename_ext, filename))
    run('rm /tmp/{}'.format(filename_ext))

    run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(filename, filename))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(filename))

    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(filename))

    return True

def deploy():
    """Create and distribute an archive to web servers."""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
