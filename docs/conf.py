# -- Project information -----------------------------------------------------

project = 'Basic Sphinx Example Project'
copyright = '2022, Read the Docs core team'
author = 'Read the Docs core team'

# -- General configuration ---------------------------------------------------
html_context = {
"display_github": False, # Add 'Edit on Github' link instead of 'View page source'
"last_updated": True,
"commit": False,
}

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'rtd': ('https://docs.readthedocs.io/en/stable/', None),
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for EPUB output
epub_show_urls = 'footnote'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []