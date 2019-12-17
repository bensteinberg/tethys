import os
import csv
import click
import fitz
from datetime import datetime


@click.command()
@click.option('--pdf', required=True, help='PDF file to split into pages')
@click.option('--out', default='.', help='Output directory')
def split_pdf(pdf, out):
    path, filename = os.path.split(pdf)
    base = os.path.splitext(filename)[0]

    # from https://stackoverflow.com/a/53009444
    doc = fitz.open(pdf)
    # control resolution: scale factor in x and y direction
    mat = fitz.Matrix(2, 2)

    with open(os.path.join(out, '{}.csv'.format(base)), 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['pdffile', 'pagefile', 'timestamp'])
        for page in doc:
            pix = page.getPixmap(matrix=mat, alpha=False)
            pagefile = '{}-{:04d}.png'.format(base, page.number)
            pix.writePNG(os.path.join(out, pagefile))
            writer.writerow([filename, pagefile, datetime.utcnow()])
