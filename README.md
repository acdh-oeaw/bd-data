# BD-DATA

Repo to process data from

> Czeitschner, U., & Krautgartner, B. (2018). travel!digital Collection (U. Czeitschner & B. Krautgartner, Eds.; Version 1) [Data set]. ARCHE. https://hdl.handle.net/21.11115/0000-000C-29F3-4

The idea is to process the data in a way it can be easily (re)published using [dse-static-coociecutter](https://github.com/acdh-oeaw/dse-static-cookiecutter)

## Tasks

* Split files: Each page should be contained by in a single TEI/XML document
* Add proper headers: Each TEI/XML file should have a propert TEI-Header

## How to

* clone the repo
* download Baedeker TEI/XML files from ARCHE and move them into a folder `xml` in the repo's root directory
* run `./build.sh`

## License
* `Milestone` class found in [`milestone.py`](src/utils/milestone.py) and written by Zeth is licensed under BSD Licence and was adapted by Daniel Elsner.
* All other code in the Repo is under MIT-License. 
* All data in the Repo is under https://creativecommons.org/licenses/by/4.0/.