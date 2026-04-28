import re
import base64

content = open('dist/scripts/content.js', 'r', encoding='utf-8').read()
array_match = re.search(r'const _0x[0-9a-f]+=\[(.*?)\];', content)
if not array_match:
    print('No array found')
    exit()

array_str = array_match.group(1)
# Strings are wrapped in single quotes, so we split by ,
items = [item.strip().strip("'") for item in array_str.split("',")]

print(f"Total items: {len(items)}")

with open('strings.txt', 'w', encoding='utf-8') as out:
    for i, s in enumerate(items):
        # strip any remaining quotes just in case
        s = s.strip("'")
        try:
            # Add padding if needed
            s_padded = s + '=' * (4 - len(s) % 4) if len(s) % 4 != 0 else s
            dec = base64.b64decode(s_padded).decode('utf-8', errors='ignore')
            out.write(f'{i}: {dec}\n')
            
            # Print if it matches our keywords
            if "skip" in dec.lower() or "video" in dec.lower() or "redirect" in dec.lower():
                print(f'Match found at {i}: {dec}')
        except Exception as e:
            pass
            
print("Done extracting relevant strings.")
