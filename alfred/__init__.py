from lxml.builder import E
from lxml import etree as et


class Icon(object):

    def __init__(self, iconpath=None, filetype=None, filepath=None):
        self.iconpath = iconpath
        self.filetype = filetype
        self.filepath = filepath

    def element(self):
        if self.iconpath:
            return E.icon(self.iconpath)

        if self.filepath:
            return E.icon(self.filepath, type='fileicon')

        if self.filetype:
            return E.icon(self.filetype, type='filetype')


class Item(object):

    def __init__(self,
                 title=None,
                 subtitle=None,
                 icon=None,
                 uid=None,
                 arg=None,
                 valid=True,
                 autocomplete=None,
                 type=None):
        self.icon = icon
        self.title = title
        self.subtitle = subtitle
        self.uid = uid
        self.arg = arg
        self.valid = valid
        self.autocomplete = autocomplete
        self.type = type

    def element(self):
        attrs = dict(uid=self.uid,
                     arg=self.arg,
                     valid="yes" if self.valid else "no",
                     autocomplete=self.autocomplete,
                     type=self.type)
        attrs = {k: v for k, v in attrs.iteritems() if v is not None}

        items = []

        if self.title:
            title = E.title(self.title)
            items.append(title)

        if self.subtitle:
            subtitle = E.subtitle(self.subtitle)
            items.append(subtitle)

        if isinstance(self.icon, str):
            icon = Icon(iconpath=self.icon).element()
        elif isinstance(self.icon, Icon):
            icon = self.icon.element()
        else:
            icon = None

        if icon is not None:
            items.append(icon)

        return E.item(*items, **attrs)


def render(items):
    root = E.items(
        *[item.element() for item in items]
    )

    return et.tostring(root, pretty_print=True, xml_declaration=True)
