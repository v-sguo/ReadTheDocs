# -- Project information

project = 'ReadTheDocs'
copyright = '2021, v-sguo'
author = 'v-sguo'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
  "display_version": False,
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

# -- Options for EPUB output
epub_show_urls = 'footnote'