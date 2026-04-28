import re
import base64
import json

def decode_array():
    content = open('dist/scripts/content.js', 'r', encoding='utf-8').read()
    array_match = re.search(r'const _0x[0-9a-f]+=\[(.*?)\];', content)
    if not array_match:
        print('No array found')
        return

    array_str = array_match.group(1)
    items = [item.strip().strip("'") for item in array_str.split("',")]

    results = []
    for i, s in enumerate(items):
        s = s.strip("'")
        try:
            padded = s + '=' * (4 - len(s) % 4) if len(s) % 4 != 0 else s
            dec = base64.b64decode(padded).decode('utf-8', errors='ignore')
            if 'skip' in dec.lower() or 'video' in dec.lower() or 'redirect' in dec.lower() or 'pro' in dec.lower() or '+' in dec:
                results.append((i, dec, s))
        except Exception:
            pass

    with open('decoded_matches.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    print(f"Found {len(results)} matches.")

decode_array()
