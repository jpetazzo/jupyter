#!/usr/bin/env python

import glob
import json

for source_file in glob.glob("*.txt"):
  cells = []
  for snippet in open(source_file).read().split("@@@"):
    snippet = snippet.strip()
    if not snippet:
      continue
    cells.append(dict(
      cell_type="code",
      metadata=dict(),
      source=snippet,
    ))
  notebook = dict(
    nbformat=4,
    nbformat_minor=0,
    metadata=dict(
      kernelspec=dict(name="python3", display_name="Python 3"),
      language_info=dict(name="python"),
    ),
    cells=cells
  )
  destination_file = "../work/" + source_file[:-4] + ".ipynb"
  with open(destination_file, "w") as f:
    json.dump(notebook, f)
