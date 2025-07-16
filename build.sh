#!/bin/bash

uv run src/split.py
uv run src/add_header.py
add-attributes -g "./data/editions/*.xml" -b "https://baedeker.acdh.oeaw.ac.at"

