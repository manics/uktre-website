# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "UK TRE"
copyright = "2023, UK TRE"
author = "UK TRE"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
myst_enable_extensions = ["fieldlist", "linkify"]
myst_linkify_fuzzy_links = False


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# https://pydata-sphinx-theme.readthedocs.io/en/stable/

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]

html_logo = "_static/uktre-logo.svg"
html_favicon = "_static/uktre-logo.svg"

html_theme_options = {
    "footer_start": ["copyright"],
    "footer_end": ["footer-links"],
}

# -- Link checker configuration
# https://www.swansea.ac.uk/the-university/location/#bay-campus=is-expanded
# is a JavaScript only anchor
linkcheck_anchors_ignore = ["bay-campus=is-expanded"]
