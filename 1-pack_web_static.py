#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime
from os.path import isdir


def do_pack():
    """fuction"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")

        fileName = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(fileName))

        return fileName

    except Exception:
        return None
