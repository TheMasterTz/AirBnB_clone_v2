#!/usr/bin/python3
from fabric.api import run, put, env
from os.path import exists
env.hosts = ['34.73.110.10', '54.234.193.97']


def do_deploy(archive_path):
    if exists(archive_path) is False:
        return False
    try:
        tokenFile = archive_path.split('/')[-1]
        folderName = tokenFile.split('.')[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}'.format(path, folderName))
        run("tar -xzf /tmp/{} -C {}{}/".format(tokenFile, path, folderName))
        run("rm /tmp/{}".format(tokenFile))
        run("mv {0}{1}/web_static/* {0}{1}/".format(path, folderName))
        run("rm -rf {}{}/web_static".format(path, folderName))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{} /data/web_static/current".format(path, folderName))
        return True
    except:
        return False
