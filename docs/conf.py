# -*- coding: utf-8 -*-
import sys
import os

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))
import semantic_release  # noqa

# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'python-semantic-release'
copyright = u'2015, Rolf Erik Lekang'

version = semantic_release.__version__
release = semantic_release.__version__

# language = None
# today = ''
# today_fmt = '%B %d, %Y'

exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'alabaster'
html_static_path = ['_static']
htmlhelp_basename = 'python-semantic-releasedoc'


# -- Options for LaTeX output ---------------------------------------------
latex_documents = [
    ('index', 'python-semantic-release.tex', u'python-semantic-release Documentation',
     u'Rolf Erik Lekang', 'manual'),
]


# -- Options for manual page output ---------------------------------------
man_pages = [
    ('index', 'python-semantic-release', u'python-semantic-release Documentation',
     [u'Rolf Erik Lekang'], 1)
]


# -- Options for Texinfo output -------------------------------------------
texinfo_documents = [
    ('index', 'python-semantic-release', u'python-semantic-release Documentation',
     u'Rolf Erik Lekang', 'python-semantic-release', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'python-semantic-release'
epub_author = u'Rolf Erik Lekang'
epub_publisher = u'Rolf Erik Lekang'
epub_copyright = u'2015, Rolf Erik Lekang'
epub_exclude_files = ['search.html']
