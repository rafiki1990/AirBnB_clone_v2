#!/usr/bin/python3
'''Create and distribute archives to web servers'''

import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once

# Define the IP addresses of the web servers
env.hosts = ['52.86.114.220', '52.3.254.18']


@runs_once
def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    if not os.path.isdir("versions"):
        # Create the 'versions' directory if it doesn't exist
        os.mkdir("versions")

    cur_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        cur_time.year,
        cur_time.month,
        cur_time.day,
        cur_time.hour,
        cur_time.minute,
        cur_time.second
    )

    try:
        print("Packing web_static to {}".format(output))
        # Create the .tgz archive
        local("tar -cvzf {} web_static".format(output))
        archive_size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, archive_size))
    except Exception as e:
        print(f"Error during packing: {e}")
        output = None

    return output


def do_deploy(archive_path):
    """Deploy the static files to the host servers.
    
    Args:
        archive_path (str): The path to the archived static files.
    """
    if not os.path.exists(archive_path):
        print(f"Archive not found: {archive_path}")
        return False

    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False

    try:
        # Upload the archive to the remote server
        put(archive_path, "/tmp/{}".format(file_name))

        # Create necessary directories and extract the archive
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))

        # Clean up temporary files and move contents to target directory
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))

        # Update the symbolic link and print a success message
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version deployed successfully!')
        success = True

    except Exception as e:
        print(f"Deployment failed: {e}")
        success = False

    return success


def deploy():
    """Archive and deploy the static files to the host servers."""
    archive_path = do_pack()
    return do_deploy(archive_path) if archive_path else False


def do_clean(number=0):
    """Delete out-of-date archives and releases of static files.
    
    Args:
        number (int): The number of archives to keep.
    """
    # List and sort archives
    archives = os.listdir('versions/')
    archives.sort(reverse=True)

    # Determine the starting index for deletion
    start = int(number) if number else 1

    # Delete out-of-date archives
    if start < len(archives):
        archives_to_delete = archives[start:]
        for archive in archives_to_delete:
            os.unlink('versions/{}'.format(archive))

    # Construct a shell command to remove out-of-date releases on the remote server
    cmd_parts = [
        "rm -rf $(",
        "find /data/web_static/releases/ -maxdepth 1 -type d -iregex",
        " '/data/web_static/releases/web_static_.*'",
        f" | sort -r | tr '\\n' ' ' | cut -d ' ' -f{start + 1}-)"
    ]
    run(''.join(cmd_parts))
