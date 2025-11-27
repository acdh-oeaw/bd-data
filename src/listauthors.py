import os

from acdh_tei_pyutils.tei import TeiReader
from acdh_tei_pyutils.utils import make_entity_label

authors_file = os.path.join("data", "indices", "listauthors.xml")
doc = TeiReader(authors_file)
nsmap = doc.nsmap
lookup = {
    "Palästina u. Syrien 1875": "Baedeker-Palaestina_und_Syrien_a0001.xml",
    "Unter-Aegypten 1877": "",
    "Ober-Ägypten 1891": "",
    "Nordamerika u. Mexiko 1893": "Baedeker-Mittelmeer_a0001.xml",
    "Konstantinopel u. Kleinasien 1905": "Baedeker-Konstantinopel_und_Kleinasien_a0001.xml",
    "Indien u. Ceylon 1914": "Baedeker-Indien_a0001.xml",
    "Mittelmeer 1909": "Baedeker-Mittelmeer_a0001.xml",
}

for i, x in enumerate(doc.any_xpath(".//tei:listPerson/tei:person"), start=1):
    xml_id = f"bda-{i:04d}"
    x.attrib["{http://www.w3.org/XML/1998/namespace}id"] = xml_id
    persName = x.xpath(".//tei:persName", namespaces=nsmap)[0]
    x.attrib["n"] = make_entity_label(persName)[0]
    # idno = ET.SubElement(x, "{http://www.tei-c.org/ns/1.0}idno", type="GND")
    for y in x.xpath(".//tei:bibl[@type='volume']", namespaces=nsmap):
        target = lookup[y.text]
        if target:
            y.attrib["source"] = target

doc.tree_to_file(authors_file)
