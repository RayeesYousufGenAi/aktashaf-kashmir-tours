import os
import re
import datetime

base_url = "https://www.aktashafkashmir.com"
today = datetime.datetime.now().strftime("%Y-%m-%d")

# SEO Paragraph for footer
seo_text = """
            <div class="footer-seo-text" style="max-width: 800px; margin: 30px auto 0; font-size: 14px; opacity: 0.7; text-align: center; line-height: 1.6;">
                <p>Plan your perfect trip with <strong>AKTASHAF KASHMIR</strong>, the leading <strong>Kashmir travel agency based in Srinagar</strong>. 
                We offer exclusive <strong>Kashmir tour packages</strong> for every traveler, including romantic <strong>honeymoon packages</strong>, 
                fun-filled <strong>family tours</strong>, and exciting <strong>group tours</strong>. Explore the beauty of Srinagar, Gulmarg, Pahalgam, and more with our budget-friendly and luxury deals.</p>
            </div>"""

# 1. FIX FILES
files_fixed = 0
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html') and 'includes' not in root:
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content
            
            # A. Fix Header H1 -> div (using regex)
            # Pattern matches the specific structure in index.html and others
            # <h1>AKTASHAF <span class="highlight">KASHMIR</span></h1>
            header_h1_pattern = r'<h1>\s*AKTASHAF\s*<span class="highlight">KASHMIR</span>\s*</h1>'
            header_replacement = r'<div class="logo-brand" style="font-size: 24px; font-weight: 700; color: #333;">AKTASHAF <span class="highlight">KASHMIR</span></div>'
            
            content = re.sub(header_h1_pattern, header_replacement, content, flags=re.IGNORECASE)

            # B. Add Canonical
            rel_path = path.replace('./', '').replace('\\', '/')
            if rel_path.startswith('/'): rel_path = rel_path[1:]
            if rel_path.startswith('.'): rel_path = rel_path[1:] # clean up leading ./
            
            canonical_url = f"{base_url}/{rel_path}"
            
            if '<link rel="canonical"' not in content and '</head>' in content:
                canonical_tag = f'<link rel="canonical" href="{canonical_url}">'
                content = content.replace('</head>', f'    {canonical_tag}\n</head>')

            # C. Add SEO Footer Text
            # Insert before <div class="footer-bottom"> or if not found, before </footer>
            if "footer-seo-text" not in content:
                if '<div class="footer-bottom">' in content:
                    content = content.replace('<div class="footer-bottom">', seo_text + '\n            <div class="footer-bottom">')
                elif '</footer>' in content:
                     content = content.replace('</footer>', seo_text + '\n</footer>')

            # D. Fix Thank-You Metadata
            if "thank-you.html" in path:
                if '<meta name="description"' not in content:
                    meta = '<meta name="description" content="Thank you for booking with AKTASHAF KASHMIR. We have received your inquiry and will contact you shortly.">'
                    content = content.replace('<title>', f'{meta}\n    <title>')

            # E. Shorten Titles
            # Find title
            title_match = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
            if title_match:
                title_text = title_match.group(1)
                if len(title_text) > 75: # Slightly more lenient
                    parts = title_text.split('|')
                    if len(parts) > 1:
                         # Keep first part and Brand
                         new_title = parts[0].strip() + " | AKTASHAF KASHMIR"
                         if len(new_title) > 75:
                             new_title = parts[0].strip()
                         content = content.replace(f'<title>{title_text}</title>', f'<title>{new_title}</title>')
                    else:
                        # Try splitting by hyphen if pipe not present
                        parts_hyphen = title_text.split('-')
                        if len(parts_hyphen) > 1:
                            new_title = parts_hyphen[0].strip() + " | AKTASHAF KASHMIR"
                            if len(new_title) > 75:
                                new_title = parts_hyphen[0].strip()
                            content = content.replace(f'<title>{title_text}</title>', f'<title>{new_title}</title>')

            if content != original_content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                files_fixed += 1
                print(f"Fixed: {path}")

print(f"Total files fixed: {files_fixed}")

# 2. GENERATE SITEMAP
print("Generating Sitemap...")
sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html') and 'includes' not in root and 'google' not in file: 
            # skipping includes and google verification files if any
            path = os.path.join(root, file)
            rel_path = path.replace('./', '').replace('\\', '/')
            if rel_path.startswith('/'): rel_path = rel_path[1:]
            if rel_path.startswith('.'): rel_path = rel_path[2:] # ./index.html -> index.html
            
            url = f"{base_url}/{rel_path}"
            priority = "0.8"
            if rel_path == "index.html": priority = "1.0"
            if "blogs/" in rel_path: priority = "0.9"
            if rel_path in ["contact.html", "about.html"]: priority = "0.7"
            
            sitemap_content += f"""  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>
"""
sitemap_content += "</urlset>"

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_content)

print("Sitemap generated.")
