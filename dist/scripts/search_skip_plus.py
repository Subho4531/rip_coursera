import json
import os

for file in os.listdir('dist/scripts'):
    if file.endswith('_strings.json'):
        d = json.load(open(os.path.join('dist/scripts', file), encoding='utf-8'))
        for k, v in d.items():
            if 'skip' in v.lower() and '+' in v:
                print(file, k, v)
