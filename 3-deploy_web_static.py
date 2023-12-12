#!/usr/bin/python3
"""Create and distributes an archive to web servers"""
import os.path
import time
from fabric.api import local
from fabric.operations import env, put, run

env.hosts = ['52.86.114.220', '52.3.254.18']

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        # Create the versions directory if it doesn't exist
        local("mkdir -p versions")

        # Create a .tgz archive with a timestamp in the filename
        local("tar -cvzf versions/web_static_{}.tgz web_static/"
              .format(time.strftime("%Y%m%d%H%M%S")))

        # Return the path to the created archive
        return "versions/web_static_{}.tgz".format(time.strftime("%Y%m%d%H%M%S"))
    except Exception as e:
        print(e)
        return None
