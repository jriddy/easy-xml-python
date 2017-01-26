"""Converts a iterable and dict-based structure to element trees.
"""
from xml.etree import ElementTree as ET
from itertools import chain


class EasyXmlConverter(object):

    def elements(self, node):
        it = iter(node)
        name = next(it)
        try:
            maybe_attribs = next(it)
        except StopIteration:
            attribs = {}
        else:
            # TODO: improve this check
            if isinstance(maybe_attribs, dict):
                attribs = maybe_attribs
                children = chain((maybe_attribs,), it)
            else:
                children = it
        return ET.Element(name, attribs)

    def dump(self, node):
        return ET.tostring(self.elements(node))
