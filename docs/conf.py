# Configuration file for the Sphinx documentation builder.

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

html_context = {
    "display_github": True, # 是否显示编辑按钮
    "display_bitbucket": True, # 是否显示Bitbucket链接
    "display_gitlab": False, # 是否显示GitLab链接
    "display_toc": False, # 是否显示目录
    "collapse_navigation": False, # 是否折叠导航
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
