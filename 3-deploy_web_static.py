#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env, local
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['34.73.110.10', '54.234.193.97']


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")

        fileName = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(fileName))

        return fileName

    except Exception:
        return None


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        nameFile = archive_path.split("/")[-1]
        NFile_no_ext = nameFile.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, NFile_no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(nameFile, path, NFile_no_ext))
        run('rm /tmp/{}'.format(nameFile))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, NFile_no_ext))
        run('rm -rf {}{}/web_static'.format(path, NFile_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, NFile_no_ext))
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
