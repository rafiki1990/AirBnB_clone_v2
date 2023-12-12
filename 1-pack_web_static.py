#!/usr/bin/python3
"""Fabric script to generate .tgz archive"""

from fabric.api import local
from datetime import datetime

def do_pack():
    """Generates .tgz archive from the contents of the web_static folder"""

    # Get the current time for timestamp in the archive name
    time = datetime.now()

    # Create a unique archive name using the timestamp
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'

    # Create the versions directory if it doesn't exist
    local("mkdir -p versions")

    # Create the .tgz archive using tar
    path = local("tar -cvzf versions/{} web_static".format(archive))

    # Check if the archive was created successfully
    if path is not None:
        return archive
    else:
        return None
