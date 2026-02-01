import os

# Configuration
directory = "/Users/rayees/omer website"

def update_blogs(root_dir):
    updated_files = 0
    
    # Walk through all files
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # 1. Update 2025 to 2026
                content = content.replace('2025', '2026')
                
                # 2. Remove date from blog listings (in blogs.html)
                if 'blogs.html' in filepath:
                    import re
                    # Remove the date span: <span><i class="far fa-calendar-alt"></i> Also removes surrounding spaces
                    # Regex to match the span with date
                    pattern = r'<span>\s*<i class="far fa-calendar-alt">\s*</i>\s*.*?2026\s*</span>'
                    content = re.sub(pattern, '', content, flags=re.DOTALL)

                # 3. Remove date from individual posts (usually in blog-single-meta)
                if '/blogs/' in filepath:
                    import re
                    # Same pattern for individual blogs
                    pattern = r'<span>\s*<i class="far fa-calendar-alt">\s*</i>\s*.*?2026\s*</span>'
                    content = re.sub(pattern, '', content, flags=re.DOTALL)
                
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated: {filepath}")
                    updated_files += 1

    print(f"Total files updated: {updated_files}")

if __name__ == "__main__":
    update_blogs(directory)
