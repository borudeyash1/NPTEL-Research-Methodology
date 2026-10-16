# -*- coding: utf-8 -*-
import json
import os
from collections import Counter

files = [
    r'd:\Interview\SAA\NPTEL\quiz_data\m01_10.json',
    r'd:\Interview\SAA\NPTEL\quiz_data\m11_20.json',
    r'd:\Interview\SAA\NPTEL\quiz_data\m21_30.json',
    r'd:\Interview\SAA\NPTEL\quiz_data\m31_40.json',
    r'd:\Interview\SAA\NPTEL\quiz_data\m41_51.json',
]

with open(r'd:\Interview\SAA\NPTEL\scripts\modules_meta.json', 'r', encoding='utf-8') as f:
    meta = json.load(f)

meta_map = {m[0]: {'title': m[1], 'week': m[2]} for m in meta}

all_questions = []
for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        all_questions.extend(data)

print(f"Total questions loaded from parts: {len(all_questions)}")

for idx, q in enumerate(all_questions, 1):
    q['id'] = idx
    mod_id = q['module']
    if mod_id in meta_map:
        title_str = meta_map[mod_id]['title']
        q['moduleTitle'] = f"Module {mod_id}: {title_str}"
        q['week'] = meta_map[mod_id]['week']

counts = Counter(q['module'] for q in all_questions)
all_10 = True
for m in range(1, 52):
    c = counts.get(m, 0)
    if c != 10:
        print(f"Warning: Module {m} has {c} questions")
        all_10 = False

if all_10:
    print("SUCCESS: Exactly 10 questions for all 51 modules (Total: 510 high-quality questions)!")

out_full = r'd:\Interview\SAA\NPTEL\quiz_data\nptel_all_questions.json'
with open(out_full, 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, indent=2)

print(f"Master question database written to {out_full}")
