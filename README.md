This repo is for files having to do with an experiment using
[Zooniverse](https://www.zooniverse.org/). So far, this includes
a script for splitting a PDF into page images and producing a manifest
for import into a subject set. To install the script, run

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
pip install --editable .
```

You should then be able to run `splitpdf --help`.
