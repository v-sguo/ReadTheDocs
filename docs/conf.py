project = 'ReadTheDocs'
copyright = '2021, v-sguo'
author = 'v-sguo'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

# html_context = {
# "display_github": False, # Add 'Edit on Github' link instead of 'View page source'
# "last_updated": False,
# "commit": False,
# }

intersphinx_mapping = {
    'rtd': ('https://docs.readthedocs.io/en/stable/', None),
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
  "display_version": True,
  "logo_only": True,
  "style_nav_header_background": "#151033",
}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
html_logo = "_static/amulet-logo2021.png"

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#
html_favicon = "_static/amlt-logo2021.ico"

html_static_path = ["_static"]
html_sidebars = {
  "**": [
    # "about.html",
    # "navigation.html",
    # "relations.html",  # needs 'show_related': True theme option to display
    # "searchbox.html",
    # "donate.html",
  ]
}



# -- Options for EPUB output
epub_show_urls = 'footnote'
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []