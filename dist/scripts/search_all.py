import json
import os

for file in os.listdir('dist/scripts'):
    if file.endswith('_strings.json'):
        d = json.load(open(os.path.join('dist/scripts', file), encoding='utf-8'))
        for k, v in d.items():
            if 'skip' in v.lower() or 'video' in v.lower() or 'redirect' in v.lower():
                print(f"{file} [{k}]: {repr(v)}")
