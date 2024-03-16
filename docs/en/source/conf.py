import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('../..'))

project = 'relogWatch'
copyright = 'Copyright © 2024'
author = 'Ricardo Abuchaim'

release = '1.5.0'

html_build_dir = os.environ.get('READTHEDOCS_OUTPUT', 'docs/pt_br/build/html')

language = 'en'

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.napoleon',
    'recommonmark',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

copyright = u'(c) 2024 Abuchaim Services Ltda. All rights reserved.'

html_css_files = [
    '_static/custom.css',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}
source_parsers = {'.md': 'recommonmark.parser.CommonMarkParser'}

templates_path = ['_templates']

exclude_patterns = []

pygments_style = 'sphinx'

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'logo': 'relogwatch.jpg',
    'github_user': 'rabuchaim',
    'github_repo': 'relogWatch',
    'github_banner': True,
}

html_static_path = ['_static']

highlight_options = {
  'default': {'stripall': True},
}
