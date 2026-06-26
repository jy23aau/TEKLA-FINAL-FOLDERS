Hugging Face's logo
Hugging Face
Models
Datasets
Spaces
Buckets
new
Docs
Enterprise
Pricing

Website
Community
Solutions

Spaces:
john5554
/
TEKLAFINALFOLDER


like
0

Logs
App
Files
Community
Settings
TEKLAFINALFOLDER/
app.py

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
⌄
⌄
⌄
⌄
⌄
import os
import fitz
import gradio as gr
import tempfile
import subprocess
import zipfile
import math
import re
import warnings
from docx import Document
from docx.shared import Pt, Inches

warnings.filterwarnings("ignore", category=DeprecationWarning)

A4_LANDSCAPE = (842.0, 595.0)
A3_LANDSCAPE = (1190.0, 842.0)
A4_PORTRAIT = (595.0, 842.0)

class Bolt:
    def __init__(self, qty1, size, length, standard, qty2):
        self.qty1 = int(qty1); self.size = size.upper(); self.length = int(length)
        self.standard = standard.strip(); self.qty2 = int(qty2) if qty2 is not None else None

    def generate_line(self):
        std_upper = self.standard.upper()
        if "FIRE" in std_upper: text = f"{self.size} X150 LONG W/ 1N/1W THREADED STUD"
        elif "HILTI" in std_upper: text = f"{self.size} X250 LONG W/ 1N/1W THREADED STUD"
        else: text = f"{self.size} x {self.length} Long{' '*(18 - len(f'{self.size} x {self.length} Long'))}{self.standard}"
        
        line = f"{self.qty1:>6}   {text}"
        if self.qty2 is not None:
            padding = max(1, 68 - len(line))
            return line + (" " * padding) + f"{self.qty2}"
        return line

def process_xsr_to_docx(xsr_path, output_dir):
Commit directly to the
main
branch
Open as a pull request to the
main
branch
Commit changes
Upload images, audio, and videos by dragging in the text input, pasting, or clicking here.
