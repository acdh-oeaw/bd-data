import glob

from acdh_tei_pyutils.tei import TeiReader

files = glob.glob("data/editions/*.xml")


for x in files:
    doc = TeiReader(x)
    for y in doc.any_xpath(".//tei:persName[@ref]"):
        old_value = y.attrib["ref"]
        if old_value.startswith("person:"):
            new_value = old_value.replace("person:", "#bd-")
            y.attrib["ref"] = new_value
    doc.tree_to_file(x)
