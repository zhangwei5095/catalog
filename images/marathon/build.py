#!/usr/bin/env python
from jinja2 import Template, Environment, FileSystemLoader
from subprocess import call
from os import remove

user='llparse'
versions=['0.11.0-centos-7', '0.11.0-ubuntu-15.04']

env = Environment(
  loader=FileSystemLoader('./templates'),
  trim_blocks=True)

for version in versions:
  image='{0}/marathon:{1}'.format(user, version)
  dockerfile='Dockerfile.{0}'.format(version)

  with open(dockerfile, 'w') as f:
    template = env.get_template('Dockerfile.j2')
    f.write(template.render(version=version))
    
  call(['docker', 'build', '-f', dockerfile, '-t', image, '.'])
  call(['docker', 'push', image])
  remove(dockerfile)
