from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd, lcd, sudo
from fabric.operations import put
from fabric.contrib.console import confirm


code_dir = '/var/adget/git'
project_dir = '/var/adget/git/parent'

def checkout():
    with settings(warn_only=True):
        if local("test -d %s" % code_dir).failed:
            local("git clone git@adget:reducedata/adget.git %s" % code_dir)
    with lcd(project_dir):
        local("git pull")

def package():
    checkout()
    with lcd(project_dir):
       local("./depsinstall.sh")
       local("mvn clean install -Dmaven.test.skip=true")
       with lcd("./adget-server"):
           local("mvn rpm:rpm")


def copyrpm(src_rpm):
     with cd("/tmp/"):
        put(src_rpm, "adget.rpm")
        sudo("rpm -iU /tmp/adget.rpm")
  
