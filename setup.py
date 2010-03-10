# hook to find setup tools if not installed
import os
import re
from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

app_name = 'django-chronograph'
root_dir = os.path.dirname(__file__)
if not root_dir:
    root_dir = '.'

def get_svn_revision(path=None):
    rev = None
    entries_path = '%s/.svn/entries' % path

    if os.path.exists(entries_path):
        entries = open(entries_path, 'r').read()
        # Versions >= 7 of the entries file are flat text.  The first line is
        # the version number. The next set of digits after 'dir' is the revision.
        if re.match('(\d+)', entries):
            rev_match = re.search('\d+\s+dir\s+(\d+)', entries)
            if rev_match:
                rev = rev_match.groups()[0]
        # Older XML versions of the file specify revision as an attribute of
        # the first entries node.
        else:
            from xml.dom import minidom
            dom = minidom.parse(entries_path)
            rev = dom.getElementsByTagName('entry')[0].getAttribute('revision')

    if rev:
        return u'svn-r%s' % rev
    return u'svn-unknown'

setup(
    name = app_name,
    version = get_svn_revision(root_dir),
    packages = find_packages(),

    include_package_data=True,
    zip_safe=False,

    description='Django chronograph application.',
    author='Weston Nielson',
    author_email='wnielson@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    url = "http://code.google.com/p/django-chronograph/",   # project home page, if any
)
