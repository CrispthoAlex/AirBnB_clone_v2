#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers
"""
from fabric.api import *
import os


env.hosts = [
    34.73.138.116,
    54.145.53.228,
]
# Set the username
env.user = "ubuntu"


def do_deploy(archive_path):
    """ script that distributes an archive to your web servers """
    if !os.path(archive_path):
        return False
    # Gets file name
    fi_name_tgz = archive_path.split("/")[1]  # file_name.tgz
    fi_name = fi_name_tgz.split(".")[0]  # file_name without .tgz

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p /data/web_static/releases/{}".format(
            fi_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            fi_name_tgz, fi_name))
        run("rm /tmp/{}".format(fi_name_tgz))
        run("mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/".format(fi_name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(fi_name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ \
        /data/web_static/current".format(fi_name))

        return True

    except:
        return False
