#!/usr/bin/env python3
"""
Fabric script that generates a .tgz archive from the contents of
the web_static folder
"""
from fabric.api import *
from datetime import datetime


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
