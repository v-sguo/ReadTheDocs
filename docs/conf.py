# conf.py
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'My Project'
copyright = '2023, My Name'
author = 'My Name'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
]

templates_path = ['_templates']

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

html_context = {
    "display_github": True,  # 不显示 'Edit on Github' 链接，而是显示 'View page source'
    "last_updated": True,
    "commit": False,
}