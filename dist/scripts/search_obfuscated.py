import re
import base64

content = open('dist/scripts/content.js', 'r', encoding='utf-8').read()
array_match = re.search(r'const _0x[0-9a-f]+=\[(.*?)\];', content)
if not array_match:
    print('No array found')
    exit()

array_str = array_match.group(1)
array = re.findall(r"'(.*?)'", array_str)

with open('strings.txt', 'w', encoding='utf-8') as out:
    for i, s in enumerate(array):
        try:
            dec = base64.b64decode(s).decode('utf-8', errors='ignore')
            if "skip" in dec.lower() or "video" in dec.lower() or "redirect" in dec.lower():
                out.write(f'{i}: {dec}\n')
        except:
            pass
print("Done extracting relevant strings.")
