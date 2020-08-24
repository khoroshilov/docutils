# Authors: Alexey Khoroshilov <khoroshilov@ispras.ru>
# Copyright: This module has been placed in the public domain.

"""
HTML Fragment Writer. 
"""

__docformat__ = 'reStructuredText'

import docutils
from docutils.writers import html4css1

class Writer(html4css1.Writer):

    settings_spec = html4css1.Writer.settings_spec

    config_section = 'html_fragment writer'
    config_section_dependencies = ('writers', 'html4css1 writer')

    def __init__(self):
        html4css1.Writer.__init__(self)

    def translate(self):
        self.visitor = visitor = self.translator_class(self.document)
        self.document.walkabout(visitor)
        self.fragment = ''.join(visitor.fragment)
        self.output = self.fragment

    def assemble_parts(self):
        pass

