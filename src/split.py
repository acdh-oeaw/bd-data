import glob
import os

from tqdm import tqdm

from config import output_dir
from utils import remove_tei_ns
from utils.milestone import Milestone

attribute_name = "facs"
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
