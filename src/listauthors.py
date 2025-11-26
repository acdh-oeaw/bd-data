import os

import lxml.etree as ET
from acdh_tei_pyutils.tei import TeiReader
from acdh_tei_pyutils.utils import make_entity_label

authors_file = os.path.join("data", "indices", "listauthors.xml")
doc = TeiReader(authors_file)
nsmap = doc.nsmap

for i, x in enumerate(doc.any_xpath(".//tei:listPerson/tei:person"), start=1):
    xml_id = f"bda-{i:04d}"
    x.attrib["{http://www.w3.org/XML/1998/namespace}id"] = xml_id
    persName = x.xpath(".//tei:persName", namespaces=nsmap)[0]
    x.attrib["n"] = make_entity_label(persName)[0]
    idno = ET.SubElement(x, "{http://www.tei-c.org/ns/1.0}idno", type="GND")

doc.tree_to_file(authors_file)
