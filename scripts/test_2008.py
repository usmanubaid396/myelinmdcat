import os
import sys
sys.path.append(os.path.dirname(__file__))
from parser_helper import parse_year_text, save_year_json

p = os.path.join(os.getcwd(), "data", "years", "2008.txt")
with open(p, "r", encoding="utf-8") as f:
    text = f.read()

questions = parse_year_text(2008, text)
save_year_json(2008, questions)

# Check subject breakdown
from collections import Counter
c = Counter(q["subject"] for q in questions)
print("2008 Breakdown:", dict(c))
