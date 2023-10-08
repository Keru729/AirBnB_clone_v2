#!/usr/bin/python3
<<<<<<< HEAD
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['142.44.167.228', '144.217.246.195']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False
=======
""" 0x03. AirBnB clone - Deploy static, task 2. Deploy archive!
"""
from fabric.api import env, put, run
from os import path

env.hosts = ['35.196.49.136', '34.74.70.223']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ Distributes a .tgz archive from the contents of `web_static/` in AirBnB
    clone repo to the web servers

    Retruns:
        (bool): `True` if all operations successful, `False` otherwise
    """
    if not path.exists(archive_path) or archive_path is None:
        return False

    f_name = path.basename(archive_path)
    d_name = f_name.split('.')[0]

    put(local_path=archive_path, remote_path='/tmp/')
    run('mkdir -p /data/web_static/releases/{}/'.format(d_name))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
        f_name, d_name))
    run('rm /tmp/{}'.format(f_name))
    run('mv /data/web_static/releases/{}/web_static/* '.format(d_name) +
        '/data/web_static/releases/{}/'.format(d_name))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(d_name))
    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(
        d_name))

    return True
>>>>>>> 318c2c43b7aa34bfcf27ad33b000421b146d92e4
