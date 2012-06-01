from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd
from fabric.contrib.console import confirm


code_dir = '/var/adget'

def checkout():
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone git@adget:reducedata/adget.git %s" % code_dir)
    with cd(code_dir):
        run("git pull")

def package():
    checkout()
    cd(code_dir + 'parent')
    run("./depsinstall.sh")
    run("mvn clean install")
    cd("adget-server")
    run("mvn rpm:rpm")

