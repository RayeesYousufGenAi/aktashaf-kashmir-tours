
import os

ga_script = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-FN74X73LGP"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-FN74X73LGP');
</script>
"""

files_updated = 0
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if 'G-FN74X73LGP' not in content:
                    # Insert after <head>
                    if '<head>' in content:
                        new_content = content.replace('<head>', '<head>\n' + ga_script, 1)
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        files_updated += 1
                        print(f'Updated: {filepath}')
                    else:
                        print(f'Skipped (no head tag): {filepath}')
                else:
                    print(f'Skipped (already present): {filepath}')
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

print(f'Total files updated: {files_updated}')
