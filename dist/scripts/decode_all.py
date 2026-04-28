import re
import base64
import json
import os

def decode_file(filepath):
    if not os.path.exists(filepath): return
    content = open(filepath, 'r', encoding='utf-8').read()
    array_match = re.search(r'const _0x[0-9a-f]+=\[(.*?)\];', content)
    if not array_match: return
    array_str = array_match.group(1)
    items = [item.strip().strip("'") for item in array_str.split("',")]
    
    results = {}
    for i, s in enumerate(items):
        s = s.strip("'")
        try:
            padded = s + '=' * (4 - len(s) % 4) if len(s) % 4 != 0 else s
            dec = base64.b64decode(padded).decode('utf-8', errors='ignore')
            results[str(i)] = dec
        except:
            results[str(i)] = s
    
    with open(filepath + '_strings.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

decode_file('dist/scripts/content.js')
decode_file('dist/scripts/popup.js')
decode_file('dist/scripts/background.js')
decode_file('dist/scripts/settings.js')
decode_file('dist/scripts/xyz.js')
decode_file('dist/scripts/rdr.js')
print("Decoded strings for all scripts.")
