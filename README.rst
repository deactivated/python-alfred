=============
python-alfred
=============

:Authors:
        Mike Spindel
:Version: 0.3


`AlfredApp <http://www.alfredapp.com>`_ is an application launcher and
general productivity tool for Mac OS X. It can be extended and
customized with custom workflows and plugin scripts.

Plugin scripts, called
"`script filters <http://www.alfredforum.com/topic/5-generating-feedback-in-workflows/>`_"
by AlfredApp, operate by printing an XML document to standard
output. ``python-alfred`` is a Python library for easily building these
XML documents.

Installation
============

::

  $ pip install alfred


Usage
=====

As an example, consider a filter that converts numeric input into
binary and hexadecimal.::

    import sys
    import alfred
     
     
    if __name__ == "__main__":
        try:
            val = int(sys.argv[1])
        except:
            sys.exit(1)

        # Use the icon associated with the Calculator app
        icon = alfred.Icon(filepath="/Applications/Calculator.app")

        # Create an item for the hex conversion
        hex_item = alfred.Item(
            uid='hex',
            arg="",
            title=hex(val),
            subtitle="Hexadecimal",
            valid=False,
            icon=icon)

        # Create an item for the binary conversion
        bin_item = alfred.Item(
            uid='bin',
            arg="",
            title=bin(val),
            subtitle="Binary",
            valid=False,
            icon=icon)

        # Call alfred.render to generate the XML document
        print alfred.render([hex_item, bin_item])


Requirements
============

``python-alfred`` requires ``lxml``.


Changes
=======

0.3 - Feb. 8, 2014
------------------

* Expose [NSWorkspace launchApplication:] via ctypes
* Add Python 3 support

0.2 - June 8, 2013
------------------

* Added support for new ``<arg></arg>`` elements

0.1 - June 4, 2013
------------------

* Initial release
