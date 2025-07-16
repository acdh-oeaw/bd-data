import glob
import os
import shutil

from acdh_tei_pyutils.tei import TeiReader
from tqdm import tqdm

from config import editions_dir, output_dir, template_dir

shutil.rmtree(editions_dir, ignore_errors=True)
os.makedirs(editions_dir, exist_ok=True)

header_mapping = {
    "Baedeker-Indien": "indien.xml",
    "Baedeker-Konstantinopel": "kleinasien.xml",
    "Baedeker-Mittelmeer": "mittelmeer.xml",
    "Baedeker-Nordamerika": "nordamerika.xml",
    "Baedeker-Palaestina": "palaestina.xml",
}

files = sorted(glob.glob(f"{output_dir}/*/*jpg.xml"))
print(f"Adding TEI-Headers to {len(files)} files...")
for i, x in tqdm(enumerate(files), total=len(files)):
    cur_file_name = os.path.split(x)[-1].split("_")[0]
    template_name = header_mapping[cur_file_name]
    f_name = os.path.split(x)[-1].replace(".jpg", "")
    save_path = os.path.join(editions_dir, f_name)
    with open(os.path.join(template_dir, template_name), "r", encoding="utf-8") as f:
        tei_header = f.read()

    with open(x, "r", encoding="utf-8") as f:
        doc = f.read()
    doc = doc.replace("{http://www.w3.org/XML/1998/namespace}", "xml:")
    doc = doc.replace(' continued="true"', "")
    doc = doc.replace("<TEI>", '<TEI xmlns="http://www.tei-c.org/ns/1.0">\n#####\n')
    doc = doc.replace("#####", tei_header)
    doc = doc.replace("&", "&amp;")
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(doc)
    try:
        doc = TeiReader(save_path)
    except Exception as e:
        print(f"failed to parse {save_path} due to {e}")
        continue
    page = doc.any_xpath(".//tei:pb[@n]/@n")[0]
    title = doc.any_xpath(".//tei:title[@level='a']")[0]
    title.text = page
    doc.tree_to_file(save_path)
