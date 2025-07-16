import glob
import os
import shutil

from tqdm import tqdm

from __init__ import Milestone
from utils import remove_tei_ns

editions_dir = os.path.join("data", "editions")
shutil.rmtree(editions_dir, ignore_errors=True)
os.makedirs(editions_dir, exist_ok=True)

attribute_name = "facs"
output_dir = "bar"
milestone = "pb"
os.makedirs(output_dir, exist_ok=True)
transform_without_split = False

files = glob.glob("./xml/*.xml")
print(f"Splitting {len(files)} files...")
for file in tqdm(files, total=len(files)):
    remove_tei_ns(file)
    input_filenames = [
        file,
    ]
    splitter = Milestone(
        milestone,
        input_filenames,
        attribute_name,
        output_dir,
        transform_without_split,
    )
    splitter.split()

files = sorted(glob.glob(f"{output_dir}/*/*jpg.xml"))
print(f"Adding TEI-Headers to {len(files)} files...")
for i, x in tqdm(enumerate(files), total=len(files)):
    f_name = os.path.split(x)[-1].replace(".jpg", "")
    save_path = os.path.join(editions_dir, f_name)
    with open(x, "r", encoding="utf-8") as f:
        doc = f.read()
    doc = doc.replace("{http://www.w3.org/XML/1998/namespace}", "xml:")
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(doc)
