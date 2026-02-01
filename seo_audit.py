import os
from bs4 import BeautifulSoup
import re

# Configuration
crawled_pages = []
report = []
base_url = "https://www.aktashafkashmir.com"
keywords_target = ["Kashmir tour packages", "Kashmir travel agency", "honeymoon", "family", "group tour"]

def audit_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    filename = os.path.basename(filepath)
    rel_path = filepath.replace(os.getcwd() + '/', '')
    
    page_report = {
        "file": rel_path,
        "title": None,
        "description": None,
        "h1": [],
        "h2": [],
        "canonical": None,
        "images_missing_alt": [],
        "keywords_found": [],
        "viewport": False,
        "robots_meta": None
    }

    # Title
    if soup.title:
        page_report["title"] = soup.title.string.strip() if soup.title.string else ""
    
    # Meta Description
    desc_tag = soup.find('meta', attrs={'name': 'description'})
    if desc_tag:
        page_report["description"] = desc_tag.get('content', '').strip()
    
    # H1
    h1_tags = soup.find_all('h1')
    page_report["h1"] = [h.get_text(strip=True) for h in h1_tags]

    # H2
    h2_tags = soup.find_all('h2')
    page_report["h2"] = [h.get_text(strip=True) for h in h2_tags]

    # Canonical
    canonical = soup.find('link', attrs={'rel': 'canonical'})
    if canonical:
        page_report["canonical"] = canonical.get('href')

    # Images
    images = soup.find_all('img')
    for img in images:
        if not img.get('alt'):
            page_report["images_missing_alt"].append(img.get('src', 'unknown'))
    
    # Viewport
    viewport = soup.find('meta', attrs={'name': 'viewport'})
    if viewport:
        page_report["viewport"] = True
        
    # Keywords
    text_content = soup.get_text().lower()
    for kw in keywords_target:
        if kw.lower() in text_content:
            page_report["keywords_found"].append(kw)

    return page_report

files_to_scan = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            files_to_scan.append(os.path.join(root, file))

results = []
titles = {}
descriptions = {}

for filepath in files_to_scan:
    res = audit_file(filepath)
    results.append(res)
    
    # Uniqueness check
    t = res.get("title")
    if t:
        if t in titles:
            titles[t].append(res["file"])
        else:
            titles[t] = [res["file"]]
            
    d = res.get("description")
    if d:
        if d in descriptions:
            descriptions[d].append(res["file"])
        else:
            descriptions[d] = [res["file"]]

# Generate Report
print("SEO AUDIT REPORT")
print("=================")

for res in results:
    print(f"\nFILE: {res['file']}")
    
    # Title
    if not res["title"]:
        print(f"  [CRITICAL] Missing Title")
    elif len(res["title"]) < 10:
        print(f"  [WARN] Title too short: {res['title']}")
    elif len(res["title"]) > 70:
        print(f"  [WARN] Title too long: {len(res['title'])} chars")
    else:
        print(f"  [OK] Title: {res['title']}")

    # Description
    if not res["description"]:
        print(f"  [CRITICAL] Missing Meta Description")
    elif len(res["description"]) < 50:
        print(f"  [WARN] Description too short")
    elif len(res["description"]) > 170:
        print(f"  [WARN] Description too long")
    else:
        print(f"  [OK] Description present")

    # H1
    if len(res["h1"]) == 0:
        print(f"  [CRITICAL] Missing H1")
    elif len(res["h1"]) > 1:
        print(f"  [WARN] Multiple H1 tags: {res['h1']}")
    else:
        print(f"  [OK] H1: {res['h1'][0]}")

    # Canonical
    if not res["canonical"]:
        print(f"  [WARN] Missing Canonical Tag")
    else:
        print(f"  [OK] Canonical: {res['canonical']}")

    # Images
    if res["images_missing_alt"]:
        print(f"  [WARN] Missing ALT text on {len(res['images_missing_alt'])} images")

    # Keywords
    missing_kw = set(keywords_target) - set(res["keywords_found"])
    if missing_kw:
        print(f"  [INFO] Missing Keywords: {', '.join(missing_kw)}")

print("\n\nDUPLICATE CHECK")
print("===============")
for t, files in titles.items():
    if len(files) > 1:
        print(f"[DUPLICATE TITLE] '{t}' found in: {', '.join(files)}")

for d, files in descriptions.items():
    if len(files) > 1:
        print(f"[DUPLICATE DESC] Found in: {', '.join(files)}")
