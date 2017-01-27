import unittest
import contextlib
from StringIO import StringIO

import easyxml
from easyxml import elements, dump, dumps


@contextlib.contextmanager
def strio(buffer=''):
    sio = StringIO(buffer)
    try:
        yield sio
    finally:
        sio.close()


class ConverterTester(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual('<root />', dumps(['root']))

    def test_basic_print_case(self):
        with strio() as f:
            dump(['root'], f)
            self.assertEqual('<root />\n', f.getvalue())

    def test_simple_html(self):
        doc = ['html',
               ['head',
                ['title', 'Sample Page'],
                ['style', {'type': 'text/css'},
                 'body { background-color: #ddddd; } '
                 '.red { color: #ff0000; }']],
               ['body',
                ['h1', 'Example HTML'],
                ['p', {'class': 'red'}, 'Lots of text']]]
        text = '<html><head><title>Sample Page</title><style type="text/css">body { background-color: #ddddd; } .red { color: #ff0000; }</style></head><body><h1>Example HTML</h1><p class="red">Lots of text</p></body></html>'
        self.assertEqual(dumps(doc), text)
