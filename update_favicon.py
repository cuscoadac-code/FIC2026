import os
import glob
import re

files = glob.glob("*.html")

favicon_tag = '<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🚴</text></svg>">\n'

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Remove Readdy Scripts (They dynamically inject the Readdy favicon and banner)
    readdy_script_pattern = r'<script>\s*window\.host\s*=\s*[\'"]readdy\.ai[\'"];\s*</script>\s*<script\s+src=[\'"]https://static\.readdy\.ai/static/share\.js[\'"]></script>'
    content = re.sub(readdy_script_pattern, '', content)

    # Clean up any other remaining instances of share.js just in case
    content = re.sub(r'<script\s+src=[\'"]https://static\.readdy\.ai/static/share\.js[\'"]></script>', '', content)

    # 2. Inject Favicon into head
    if 'rel="icon"' not in content:
        content = content.replace("</head>", favicon_tag + "</head>")
        
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Favicon updated and Readdy scripts removed from all HTML files.")
