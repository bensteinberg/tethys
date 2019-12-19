This repo is for files having to do with a
[Zooniverse](https://www.zooniverse.org/) experiment. So far, this
includes a script for splitting a PDF into page images and producing a
manifest for import into a subject set. To install the script, install
`python3-venv` if necessary, then run

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
pip install --editable splitpdf
```

You should then be able to run `splitpdf --help`.
