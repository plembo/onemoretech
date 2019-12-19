#!/usr/bin/env python3
# Backup repositories of a Gitlab user.
import os
import gitlab
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--path", help="Backup path")
args = parser.parse_args()
if args.path:
    backupdir = args.path

glab_token = os.environ.get('GLAB_TOKEN')
gl = gitlab.Gitlab('https://gitlab.com', private_token=glab_token)
projects = gl.projects.list(owned=True, all=True)

for project in projects:
    ssh_url = project.ssh_url_to_repo
    reponame = project.name
    repodir = f'{backupdir}/{reponame}'
    clone_cmd = f'git clone {ssh_url}'
    pull_cmd = f'git pull'

    print(reponame)
    if (os.path.isdir(repodir)):
        os.chdir(repodir)
        os.system(pull_cmd)
    else:
        os.chdir(backupdir)
        os.system(clone_cmd)
