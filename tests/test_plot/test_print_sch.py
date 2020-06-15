"""
Tests of Printing Schematic files

We test:
- PDF for bom.sch

For debug information use:
pytest-3 --log-cli-level debug

"""

import os
import sys
# Look for the 'utils' module from where the script is running
prev_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if prev_dir not in sys.path:
    sys.path.insert(0, prev_dir)
# Utils import
from utils import context

PDF_DIR = ''
PDF_FILE = 'Schematic.pdf'


def test_print_sch():
    prj = 'bom'
    ctx = context.TestContext('PrSCH', prj, 'print_sch', PDF_DIR)
    ctx.run()
    # Check all outputs are there
    ctx.expect_out_file(PDF_FILE)
    ctx.clean_up()
