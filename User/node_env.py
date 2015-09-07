import os
import getpass

user = getpass.getuser()

nvm_default_file_path = '/Users/%(user)s/.nvm/alias/default' % {'user': user}

with open(nvm_default_file_path, 'r') as content_file:
    content = content_file.read()

version = content.strip()

node_path = "/Users/%(user)s/.nvm/v%(version)s/bin:/Users/%(user)s/.nvm/v%(version)s/lib" % {'version':version, 'user':user}

# Sublime's default path is
# /usr/bin:/bin:/usr/sbin:/sbin
# it'll be prepended to your custom one
os.environ['PATH'] += ':'
os.environ['PATH'] += node_path
