import os

from acdh_tei_pyutils.tei import TeiReader
from acdh_tei_pyutils.utils import make_entity_label

# files = glob.glob("data/editions/*.xml")


# for x in files:
#     doc = TeiReader(x)
#     for y in doc.any_xpath(".//tei:persName[@ref]"):
#         old_value = y.attrib["ref"]
#         if old_value.startswith("person:"):
#             new_value = old_value.replace("person:", "#bd-")
#             y.attrib["ref"] = new_value
#     doc.tree_to_file(x)


listperson_file = os.path.join("data", "indices", "listperson.xml")

doc = TeiReader(listperson_file)
nsmap = doc.nsmap

for x in doc.any_xpath(".//tei:person[@xml:id]"):
    name = x.xpath("./tei:persName", namespaces=nsmap)[0]
    label = make_entity_label(name)[0]
    x.attrib["n"] = label
doc.tree_to_file(listperson_file)
