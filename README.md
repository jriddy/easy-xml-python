# easy-xml-python
Easy way to turn base python data structures into XML

## XML made simple
XML is annoying.  Libraries for it expect you to care about XML and its own
weird structure.  Not this library.  Tags are just Python iterables with a first
element as a tag name, optional second element of `dict` of attributes, and
optional subsequent elements of child nodes.  That's it.

Underneath, it uses the Python standard library's `xml.etree.ElementTree` to
generate documents.  The main `elements` function will return an
`ElementTree.Element` object.  The `dump` and `dumps` will write to a file-like
object and return a string, respectively.

## Basic Usage

Say you want to make a basic HTML page.  You could write it in code something
like this:

    doc = ['html',
           ['head',
            ['title', 'Sample Page'],
            ['style', {'type': 'text/css'},
             'body { background-color: #ddddd; } '
             '.red { color: #ff0000; }']],
           ['body',
            ['h1', 'Example HTML'],
            ['p', {'class': 'red'}, 'Lots of text']]]

    output = easyxml.dumps(doc) # get a string
    # or
    with open('samplepage.html', 'w') as file:
        easyxml.dump(doc, file)
