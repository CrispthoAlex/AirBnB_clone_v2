#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers
"""
from fabric.api import *
from datetime import datetime
from os.path import isfile


env.hosts = ["34.73.138.116", "54.145.53.228"]
# Set the username env.user = "ubuntu"


def do_pack():
    """ generates a .tgz archive from the contents of the web_static """
    date_file = datetime.now().strftime("%Y%m%d%H%M%S")
    di_crea = "versions"   # new directory to keep tgz files
    di_src = "web_static"  # source directory
    fi_name = "{}_{}.tgz".format(di_src, date_file)  # file name to create

    local("mkdir -pv {}".format(di_crea))
    succeess = local("tar -cvzf {}/{} {}".format(
        di_crea, fi_name, di_src))

    if succeess:
        return fi_name
    else:
        return None


def do_deploy(archive_path):
    """ script that distributes an archive to your web servers """
    if isfile(archive_path) is False:
        print(archive_path)
        return False
    # Gets file name
    fi_name_tgz = archive_path.split("/")[1]  # file_name.tgz
    print(fi_name_tgz)
    fi_name = fi_name_tgz.split(".")[0]  # file_name without .tgz
    print(fi_name)

    try:

        print("Ok try")
        put("{}".format(archive_path), "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(
            fi_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            fi_name_tgz, fi_name))
        run("rm /tmp/{}".format(fi_name_tgz))
        run("mv /data/web_static/releases/{0}/web_static/* \
        /data/web_static/releases/{0}/".format(fi_name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(fi_name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ \
        /data/web_static/current".format(fi_name))

        return True

    except Exception:
        print("Ok Exception")
        return False


def deploy():
    """ deploy function  """
    file_path = do_pack()

    if file_path:
        return do_deploy(file_path)
    else:
        return False
