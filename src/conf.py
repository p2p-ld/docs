# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'p2p-ld'
copyright = '2023, Jonny Saunders'
author = 'Jonny Saunders'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinxcontrib.mermaid',
    'sphinxcontrib.bibtex',
    'myst_parser'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_baseurl = '/docs/'

# -----------
# Extension config

# myst
myst_heading_anchors = 3
myst_enable_extensions = [
    'tasklist',
    'linkify',
    'attrs_block'
]
myst_linkify_fuzzy_links = False

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# bibtex
bibtex_bibfiles = ['p2p_ld_docs.bib']
bibtex_reference_style = 'author_year'
bibtex_default_style = 'bbibtex'

# mermaid
mermaid_init_js = """
mermaid.initialize({
    "startOnLoad":true,
    "theme": "base",
    "themeVariables": {
      "darkMode": true,
      "primaryColor": "#202020",
      "primaryBorderColor": "#00A5CF",
      "primaryTextColor": "#FFFFFF",
      "secondaryColor": "#ffffff",
      "mainBkg": "#30303000",
      "lineColor": "#999999"
    }
})
"""

## Formatting to handle dates that are in the `date` field rather than `year`
import re
import pybtex.plugin
from pybtex.richtext import Symbol, Text
from pybtex.style.formatting.unsrt import Style as UnsrtStyle
from pybtex.style.formatting import unsrt as unsrt_module
from pybtex.style.formatting import toplevel
from pybtex.style.template import (
    field, first_of, href, join, names, optional, optional_field, sentence,
    tag, together, words
)

def dashify(text):
    dash_re = re.compile(r'-+')
    return Text(Symbol('ndash')).join(text.split(dash_re))

date = first_of [
    field('date'),
    words [optional_field('month'), field('year')]
]
pages = field('pages', apply_func=dashify)

# monkey patch date
unsrt_module.date = date


class BetterBibTeXStyle(UnsrtStyle):
    def get_article_template(self, e):
        volume_and_pages = first_of [
            # volume and pages, with optional issue number
            optional [
                join [
                    field('volume'),
                    optional['(', field('number'),')'],
                    ':', pages
                ],
            ],
            # pages only
            words ['pages', pages],
        ]
        template = toplevel [
            self.format_names('author'),
            self.format_title(e, 'title'),
            sentence [
                tag('em') [first_of [
                    field('journaltitle'),
                    field('journal')
                ]],
                optional[ volume_and_pages ],
                date],
            sentence [ optional_field('note') ],
            self.format_web_refs(e),
        ]
        return template

# ----------------
# Handle when dates are in `date` and not `year`

# fuck it just monkey patch it

from sphinxcontrib.bibtex.style.template import node
from typing import Dict
from sphinxcontrib.bibtex.style.template import first_of as first_of_
from sphinxcontrib.bibtex.style.template import optional as optional_
from sphinxcontrib.bibtex.style.template import field as field_
from sphinxcontrib.bibtex.style import template as template_module



def split_year(date:str) -> str:
    return date.split('-')[0]

@node
def year(children, data: Dict[str, Any]) -> "BaseText":
    assert not children
    return first_of_[optional_[field_('year')], optional_[field_('date', apply_func=split_year)], 'n.d.'].format_data(data)

template_module.year = year


pybtex.plugin.register_plugin('pybtex.style.formatting', 'bbibtex', BetterBibTeXStyle)