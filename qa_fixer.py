import os
import re
from bs4 import BeautifulSoup
import datetime

# Configuration
base_url = "https://www.aktashafkashmir.com"
input_dir = "."
files_modified = 0

# ---------------------------------------------------------
# 1. DEFINE STANDARDIZED COMPONENTS
# ---------------------------------------------------------

# Standard Header (Will start with no active classes, we set them programmatically)
standard_header = """
    <header class="header" id="header">
        <div class="container">
            <div class="header-content">
                <a href="/index.html" class="logo">
                    <div class="logo-icon-wrapper">
                        <img src="/images/logo-new.png" alt="AKTASHAF KASHMIR Icon">
                    </div>
                    <div class="logo-text">
                        <div class="logo-brand" style="font-size: 24px; font-weight: 700; color: #1a2332; font-family: 'Poppins', sans-serif;">AKTASHAF <span style="color: #FF6B00;">KASHMIR</span></div>
                        <span class="tagline" style="font-size: 10px; color: #636e72; letter-spacing: 1px; text-transform: uppercase; font-weight: 500;">Your Gateway to Kashmir</span>
                    </div>
                </a>

                <nav class="nav" id="nav">
                    <ul class="nav-list">
                        <li><a href="/index.html" class="nav-link" data-page="index.html">Home</a></li>
                        <li><a href="/about.html" class="nav-link" data-page="about.html">About us</a></li>
                        <li><a href="/domestic.html" class="nav-link" data-page="domestic.html">Domestic Tours</a></li>
                        <li><a href="/international.html" class="nav-link" data-page="international.html">International Tours</a></li>
                        <li><a href="/blogs.html" class="nav-link" data-page="blogs.html">Blogs</a></li>
                        <li><a href="/contact.html" class="nav-link" data-page="contact.html">Contact us</a></li>
                    </ul>
                </nav>

                <div class="header-right">
                    <div class="call-info">
                        <a href="tel:+919796664664" class="phone-number" style="font-weight: 700; color: #1a2332; text-decoration: none;"><i class="fas fa-phone-alt" style="color: #FF6B00;"></i> +91 9796664664</a>
                    </div>
                    <button class="mobile-menu-toggle" id="mobileMenuToggle">
                        <i class="fas fa-bars"></i>
                    </button>
                </div>
            </div>
        </div>
    </header>
"""

# Premium Footer
current_year = datetime.datetime.now().year
standard_footer = f"""
    <footer class="footer" style="background: #1a2332; color: #fff; padding: 60px 0 20px;">
        <div class="container">
            <div class="footer-content" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 40px; margin-bottom: 40px;">
                <div class="footer-col">
                    <h3 style="color: #fff; font-size: 18px; margin-bottom: 20px; font-weight: 700;">About AKTASHAF KASHMIR</h3>
                    <p style="color: #a0a0a0; line-height: 1.6; margin-bottom: 15px;">Your trusted Kashmir travel partner. We specialize in creating unforgettable Kashmir experiences with personalized service, local expertise, and unbeatable value.</p>
                    <div class="payment-icons" style="font-size: 24px; color: #a0a0a0; display: flex; gap: 15px;">
                        <i class="fab fa-cc-visa"></i>
                        <i class="fab fa-cc-paypal"></i>
                        <i class="fab fa-cc-mastercard"></i>
                    </div>
                </div>

                <div class="footer-col">
                    <h3 style="color: #fff; font-size: 18px; margin-bottom: 20px; font-weight: 700;">Quick Links</h3>
                    <ul class="footer-links" style="list-style: none; padding: 0;">
                        <li style="margin-bottom: 10px;"><a href="/domestic.html" style="color: #a0a0a0; text-decoration: none; transition: 0.3s;">Domestic Tours</a></li>
                        <li style="margin-bottom: 10px;"><a href="/international.html" style="color: #a0a0a0; text-decoration: none; transition: 0.3s;">International Tours</a></li>
                        <li style="margin-bottom: 10px;"><a href="/blogs.html" style="color: #a0a0a0; text-decoration: none; transition: 0.3s;">Travel Blog</a></li>
                        <li style="margin-bottom: 10px;"><a href="/contact.html" style="color: #a0a0a0; text-decoration: none; transition: 0.3s;">Contact Us</a></li>
                    </ul>
                </div>

                <div class="footer-col">
                    <h3 style="color: #fff; font-size: 18px; margin-bottom: 20px; font-weight: 700;">Contact Us</h3>
                    <p style="color: #a0a0a0; margin-bottom: 10px;"><i class="fas fa-map-marker-alt" style="color: #FF6B00; width: 20px;"></i> Srinagar, Jammu and Kashmir 190002</p>
                    <p style="color: #a0a0a0; margin-bottom: 10px;"><a href="tel:+919796664664" style="color: #a0a0a0; text-decoration: none;"><i class="fas fa-phone-alt" style="color: #FF6B00; width: 20px;"></i> +91 9796664664</a></p>
                    <p style="color: #a0a0a0; margin-bottom: 10px;"><a href="mailto:aktashafkmr@gmail.com" style="color: #a0a0a0; text-decoration: none;"><i class="fas fa-envelope" style="color: #FF6B00; width: 20px;"></i> aktashafkmr@gmail.com</a></p>
                    <div class="social-links" style="display: flex; gap: 15px; margin-top: 20px;">
                        <a href="https://www.facebook.com/aktashafkashmir" target="_blank" style="width: 35px; height: 35px; background: rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; border-radius: 50%; color: #fff; text-decoration: none; transition: 0.3s;"><i class="fab fa-facebook-f"></i></a>
                        <a href="https://www.instagram.com/aktashafkashmir" target="_blank" style="width: 35px; height: 35px; background: rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; border-radius: 50%; color: #fff; text-decoration: none; transition: 0.3s;"><i class="fab fa-instagram"></i></a>
                        <a href="https://wa.me/919796664664" target="_blank" style="width: 35px; height: 35px; background: rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; border-radius: 50%; color: #fff; text-decoration: none; transition: 0.3s;"><i class="fab fa-whatsapp"></i></a>
                    </div>
                </div>
            </div>
            
            <div class="footer-seo-text" style="max-width: 900px; margin: 0 auto 30px; font-size: 13px; opacity: 0.6; text-align: center; line-height: 1.6; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 20px;">
                <p>Plan your perfect trip with <strong>AKTASHAF KASHMIR</strong>, the leading <strong>Kashmir travel agency based in Srinagar</strong>. 
                We offer exclusive <strong>Kashmir tour packages</strong> for every traveler, including romantic <strong>honeymoon packages</strong>, 
                fun-filled <strong>family tours</strong>, and exciting <strong>group tours</strong>. Explore the beauty of Srinagar, Gulmarg, Pahalgam, and more with our budget-friendly and luxury deals.</p>
            </div>

            <div class="footer-bottom" style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 20px; text-align: center;">
                <p style="color: #a0a0a0; font-size: 14px; margin: 0;">
                    Copyright &copy; {current_year} AKTASHAF KASHMIR. All Rights Reserved. 
                    <span style="margin: 0 10px; color: #444;">|</span> 
                    <span style="font-family: 'Poppins', sans-serif; font-weight: 500;">Developed with <span style="color: #ff4757;">&hearts;</span> by <a href="https://nexevai.com" target="_blank" style="color: #FDB714; text-decoration: none;">nexevai</a></span>
                </p>
            </div>
        </div>
    </footer>
    
    <!-- WhatsApp Floating Button -->
    <a href="https://wa.me/919796664664" class="whatsapp-float" target="_blank" aria-label="Chat on WhatsApp" style="position: fixed; bottom: 30px; left: 30px; background: #25d366; color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 30px; box-shadow: 0 4px 15px rgba(37, 211, 102, 0.4); z-index: 9999; transition: transform 0.3s ease;">
        <i class="fab fa-whatsapp"></i>
    </a>
    
    <div class="mobile-cta-bar">
        <a href="tel:+919796664664" class="mobile-cta-button mobile-cta-call">
            <i class="fas fa-phone-alt"></i> Call Now
        </a>
        <a href="https://wa.me/919796664664" class="mobile-cta-button mobile-cta-whatsapp">
            <i class="fab fa-whatsapp"></i> WhatsApp
        </a>
    </div>
"""

# ---------------------------------------------------------
# 2. PROCESSING FUNCTION
# ---------------------------------------------------------

def standardize_file(filepath):
    print(f"Processing {filepath}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    filename = os.path.basename(filepath)
    is_blog = "blogs/" in filepath

    # A. HEAD SECTION: Inject mobile-app.css and favicon
    head = soup.head
    if head:
        # Check URL depth for relative links
        prefix = "../" if is_blog else ""
        
        # Link to mobile-app.css if missing
        mobile_css_exists = False
        for link in head.find_all('link'):
            if 'mobile-app.css' in str(link):
                mobile_css_exists = True
                break
        
        if not mobile_css_exists:
            new_link = soup.new_tag("link", rel="stylesheet", href=f"{prefix}css/mobile-app.css")
            head.append(new_link)
            
        # Ensure FontAwesome is there
        fa_exists = False
        for link in head.find_all('link'):
             if 'font-awesome' in str(link):
                 fa_exists = True
        if not fa_exists:
            fa_link = soup.new_tag("link", rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css")
            head.append(fa_link)

    # B. REPLACE HEADER
    old_header = soup.find('header')
    if old_header:
        # Parse standardized header
        new_header_soup = BeautifulSoup(standard_header, 'html.parser')
        
        # Adjust links for blog pages
        if is_blog:
            for a in new_header_soup.find_all('a'):
                if a.get('href') and not a['href'].startswith('http') and not a['href'].startswith('tel') and not a['href'].startswith('mailto'):
                    a['href'] = "../" + a['href'].lstrip('/')
            for img in new_header_soup.find_all('img'):
                if img.get('src'):
                    img['src'] = "../" + img['src'].lstrip('/')
        else:
             # Remove leading slashes for local dev if needed, or keep relative
             for a in new_header_soup.find_all('a'):
                if a.get('href') and a['href'].startswith('/'):
                    a['href'] = a['href'].lstrip('/')
             for img in new_header_soup.find_all('img'):
                if img.get('src') and img['src'].startswith('/'):
                    img['src'] = img['src'].lstrip('/')

        # Set ACTIVE stat logic
        target_page = filename
        if is_blog: target_page = "blogs.html"
        
        for link in new_header_soup.find_all('a', class_='nav-link'):
            if link.get('data-page') == target_page:
                link['class'] = link.get('class', []) + ['active']
            # Clean data attribute
            del link['data-page']

        old_header.replace_with(new_header_soup)

    # C. REPLACE FOOTER
    old_footer = soup.find('footer')
    
    # Also find/remove any existing .whatsapp-float or .mobile-cta-bar to avoid dupes
    for extra in soup.find_all('a', class_='whatsapp-float'): extra.decompose()
    for extra in soup.find_all('div', class_='mobile-cta-bar'): extra.decompose()

    if old_footer:
        new_footer_soup = BeautifulSoup(standard_footer, 'html.parser')
        
        if is_blog:
             for a in new_footer_soup.find_all('a'):
                if a.get('href') and not a['href'].startswith('http') and not a['href'].startswith('tel') and not a['href'].startswith('mailto'):
                    a['href'] = "../" + a['href'].lstrip('/')
        else:
             for a in new_footer_soup.find_all('a'):
                if a.get('href') and a['href'].startswith('/'):
                    a['href'] = a['href'].lstrip('/')

        old_footer.replace_with(new_footer_soup)
    elif soup.body:
        # If no footer, append to body
        new_footer_soup = BeautifulSoup(standard_footer, 'html.parser')
        soup.body.append(new_footer_soup)
        
    # D. FIX FORMS
    forms = soup.find_all('form')
    for form in forms:
        # Check if it looks like a submission form (inputs inside)
        if form.find('input'):
            # Add Netlify attributes
            form['data-netlify'] = "true"
            form['method'] = "POST"
            if not form.get('action'):
                form['action'] = "/success.html" if not is_blog else "../success.html"
            
            # Netlify Honeypot
            if not form.get('netlify-honeypot'):
                form['netlify-honeypot'] = "bot-field"
                # Add the hidden input for honeypot
                hidden_p = soup.new_tag("p", style="display: none;")
                hidden_label = soup.new_tag("label")
                hidden_label.string = "Don't fill this out: "
                hidden_input = soup.new_tag("input", name="bot-field")
                hidden_label.append(hidden_input)
                hidden_p.append(hidden_label)
                form.insert(0, hidden_p)
            
            # Form Name
            if not form.get('name'):
                 form['name'] = "contact" # Default name
            
            # Add hidden form-name input if missing
            has_form_name = False
            for inp in form.find_all('input', {'type': 'hidden'}):
                if inp.get('name') == 'form-name':
                    has_form_name = True
            
            if not has_form_name:
                hidden_name = soup.new_tag("input", type="hidden", name="form-name", value=form['name'])
                form.insert(1, hidden_name)

    # E. GENERAL CLEANUP
    # Remove any extra empty space text nodes
    for element in soup.find_all(text=lambda text: isinstance(text, str) and not text.strip()):
        # element.extract() # Be careful not to remove spacing between words
        pass

    # Save
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup.prettify()))
    
    return True

# ---------------------------------------------------------
# 3. RUN
# ---------------------------------------------------------

for root, dirs, files in os.walk(input_dir):
    for file in files:
        if file.endswith('.html') and 'includes' not in root:
            filepath = os.path.join(root, file)
            standardize_file(filepath)
            files_modified += 1

print(f"QA Fix Complete. {files_modified} files standardized.")
