#!/usr/bin/python3
"""Distributes an archive to your web servers, using the function do_deploy"""
from fabric.contrib import files
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['54.224.33.148', '54.234.37.54']

def do_deploy(archive_path):
    """Function for deploy"""
    if exists(archive_path) is False:
        return False

    try:
        # Extract relevant information from the archive path
        file = archive_path.split("/")[-1]
        no_ext = file.split(".")[0]
        path = "/data/web_static/releases/"

        # Upload the archive to /tmp/ on the remote server
        put(archive_path, '/tmp/')

        # Create the necessary directory structure
        run('mkdir -p {}{}/'.format(path, no_ext))

        # Extract the contents of the archive
        run('tar -xzf /tmp/{} -C {}{}/'.format(file, path, no_ext))

        # Remove the temporary archive file
        run('rm /tmp/{}'.format(file))

        # Move the contents of the extracted folder to the release folder
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))

        # Remove the now-empty web_static folder
        run('rm -rf {}{}/web_static'.format(path, no_ext))

        # Remove the existing /data/web_static/current folder
        run('rm -rf /data/web_static/current')

        # Create a symbolic link to the new release
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))

        return True
    except Exception as e:
        print(e)
        return False
