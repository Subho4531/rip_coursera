import re

for file in ['dist/scripts/content.js', 'dist/scripts/popup.js']:
    content = open(file, 'r', encoding='utf-8').read()
    matches = re.findall(r'[\'\"`]([^\'\"`]*?(?:skip|video|redirect)[^\'\"`]*?)[\'\"`]', content, re.IGNORECASE)
    print(file)
    for m in set(matches):
        print('  ', repr(m))
