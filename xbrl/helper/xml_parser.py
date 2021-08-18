"""
This module wraps the parse function of the Element Tree library to parse XML files with a
namespace map. Element tree discards all prefixes when parsing the file.
It is used by the different parsing modules.
"""
import lxml.html
from lxml import etree as ET

def parse_file(path: str) -> (ET,dict):
    """
    Parses a file, returns the Root element with an attribute 'ns_map' containing the prefix - namespaces map
    @return:
    """
    is_html = path.lower().split('.')[-1] in ['htm','html']

    if is_html is True:
        # parse as html
        tree = lxml.html.parse(path)
    else:
        # parse as xml, xsd
        tree = ET.parse(path)

    # extract namespace map
    ns_map = dict()
    for item in tree.iter():
        for k,v in item.attrib.items():
            if ':' in k:
                nm = k.split(':')[-1]
                if not nm in ns_map:
                    ns_map[nm] = v
    return ET.ElementTree(tree.getroot()), ns_map
 