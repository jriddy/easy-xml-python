# easy-xml-python
Easy way to turn base python data structures into XML

# Ugh, XML
XML is annoying.  Libraries for it expect you to care about XML and its own
weird structure.  Not this library.  Tags are just Python iterables with a first
element as a tag name, optional second element of `dict` of attributes, and
optional subsequent elements of child nodes.  That's it.
