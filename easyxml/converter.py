"""Converts a iterable and dict-based structure to element trees.
"""
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element, SubElement
from itertools import chain
from functools import partial


class EasyXmlConverter(object):

    def reprstag(self, x):
        """Determines if the object `x` represents a tag.

        Probably needs a different check for python 3
        """
        return not isinstance(x, basestring)

    def reprsattribs(self, x):
        return isinstance(x, dict)

    def elements(self, node, parent=None):
        it = iter(node)
        name = next(it)
        try:
            maybe_attribs = next(it)
        except StopIteration:
            attribs = {}
            children = ()
        else:
            # TODO: improve this check
            if self.reprsattribs(maybe_attribs):
                attribs = maybe_attribs
                children = it
            else:
                children = chain((maybe_attribs,), it)
                attribs = {}
        make = Element if parent is None else partial(SubElement, parent)
        elem = make(name, attribs)
        last = None
        for child in children:
            if self.reprstag(child):
                last = self.elements(child, elem)
            elif last is None:
                elem.text = child
            else:
                last.tail = child
        return elem

    def dump(self, node):
        return ET.tostring(self.elements(node))
