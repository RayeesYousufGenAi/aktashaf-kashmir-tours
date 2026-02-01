import os
from bs4 import BeautifulSoup

# Base directory
base_dir = "/Users/rayees/omer website"
template_path = os.path.join(base_dir, "blogs/best-time-to-visit-kashmir.html")

# New Blogs Data
new_blogs = [
    {
        "filename": "kashmir-houseboat-vs-hotel-guide.html",
        "title": "Kashmir Houseboat vs Hotel: Where Should You Stay?",
        "shorter_title": "Houseboat vs Hotel Guide",
        "description": "Confused between a luxury houseboat and a hotel? We compare costs, comfort, and experiences to help you decide.",
        "category": "Accommodation",
        "image": "kashmir-houseboat.jpg", # Will need to be mapped or a placeholder used
        "content_intro": """
            <p class="lead">One of the biggest dilemmas travellers face when planning a trip to Kashmir is choosing between a <strong>traditional houseboat on Dal Lake</strong> and a <strong>comfortable hotel in Srinagar</strong>. Both offer unique experiences, but which one is right for you?</p>
            <p>In this 2026 guide, we compare the pros and cons, pricing, and amenities of Kashmir houseboats versus hotels to help you make the best choice for your vacation.</p>
            
            <h2>The Houseboat Experience</h2>
            <p>Staying in a houseboat is a quintessential Kashmir experience. Carved from cedar wood and anchored on the calm waters of Dal Lake or Nigeen Lake, these floating palaces offer a romantic and heritage feel.</p>
            <ul>
                <li><strong>Pros:</strong> Unique experience, stunning lake views, heritage interiors, peaceful atmosphere.</li>
                <li><strong>Cons:</strong> Limited mobility (you need a shikara to cross), fixed meal times, can be colder in winter.</li>
                <li><strong>Best For:</strong> Couples, Honeymooners, and those seeking a 1-2 night unique stay.</li>
            </ul>

            <h2>The Hotel Experience</h2>
            <p>Kashmir boasts a wide range of hotels from budget stays to 5-star luxury resorts like The Lalit and Taj Vivanta.</p>
            <ul>
                <li><strong>Pros:</strong> Modern amenities (central heating, 24/7 hot water), easier accessibility, room service flexibility.</li>
                <li><strong>Cons:</strong> Lacks the traditional 'floating' charm of a houseboat.</li>
                <li><strong>Best For:</strong> Families with kids, elderly travelers, and long-duration stays.</li>
            </ul>

            <h2>Price Comparison (2026 Rates)</h2>
            <table class="table">
                <tr><th>Category</th><th>Houseboat (Per Night)</th><th>Hotel (Per Night)</th></tr>
                <tr><td>Budget/Standard</td><td>₹2,500 - ₹4,000</td><td>₹2,000 - ₹3,500</td></tr>
                <tr><td>Deluxe/Premium</td><td>₹5,000 - ₹8,000</td><td>₹4,500 - ₹9,000</td></tr>
                <tr><td>Luxury</td><td>₹10,000+</td><td>₹12,000+</td></tr>
            </table>

            <h2>Our Verdict</h2>
            <p>We recommend a <strong>combination stay</strong>. Spend your first night in a houseboat to soak in the charm of Dal Lake, and then move to a hotel for the rest of your trip for convenience and comfort. Contact <strong>AKTASHAF KASHMIR</strong> to book the best combo packages!</p>
        """
    },
    {
        "filename": "top-5-offbeat-places-in-kashmir-2026.html",
        "title": "Top 5 Offbeat Places in Kashmir to Visit in 2026",
        "shorter_title": "Top 5 Offbeat Places 2026",
        "description": "Escape the crowds! Discover hidden gems like Warwan Valley, Bangus, and Chatpal in our latest travel guide.",
        "category": "Hidden Gems",
        "image": "offbeat-kashmir.jpg",
        "content_intro": """
            <p class="lead">While Gulmarg and Pahalgam are stunning, the true soul of Kashmir lies in its untouched villages. In 2026, travelers are moving beyond the tourist trail to explore raw, virgin beauty.</p>
            <p>Here are the <strong>top 5 offbeat destinations in Kashmir</strong> that you must add to your bucket list this year.</p>

            <h2>1. Warwan Valley</h2>
            <p>Located in Kishtwar district, Warwan is arguably the most isolated and beautiful valley in Kashmir. With waterfalls at every turn and no mobile network, it is a digital detox paradise.</p>

            <h2>2. Bangus Valley</h2>
            <p>A vast meadow in Kupwara, Bangus is blooming with wildflowers and surrounded by dense forests. It is an emerging eco-tourism spot perfect for picnics and day trips.</p>

            <h2>3. Chatpal</h2>
            <p>Often called 'Mini Pahalgam' without the crowds, Chatpal in South Kashmir offers silence, pine forests, and gushing streams. There are lovely government wooden cottages for a stay.</p>

            <h2>4. Aharbal Waterfall</h2>
            <p>Known as the 'Niagara of Kashmir', Aharbal is a massive waterfall on the Veshu River. It is majestic in summer and offers trekking routes to Kausar Nag lake.</p>

            <h2>5. Daksum</h2>
            <p>A trekker's delight, Daksum is the gateway to Sinthan Top. The road journey through pine forests is breathtaking.</p>

            <h2>Tips for Offbeat Travel</h2>
            <ul>
                <li>Hire a private cab as public transport is rare.</li>
                <li>Carry cash; ATMs are hard to find in remote areas.</li>
                <li>Respect local culture and dress modestly.</li>
            </ul>
        """
    },
    {
        "filename": "how-to-reach-kashmir-flight-train-road-guide.html",
        "title": "How to Reach Kashmir: Flight vs Train vs Road (2026 Guide)",
        "shorter_title": "How to Reach Kashmir Guide",
        "description": "The complete travel logistics guide. Updates on the new Vande Bharat train to Srinagar and flight connectivity.",
        "category": "Travel Logistics",
        "image": "reach-kashmir.jpg",
        "content_intro": """
            <p class="lead">Planning a trip to magnificent Kashmir? The first step is getting there. With major infrastructure upgrades in 2026, reaching Srinagar has never been easier.</p>
            <p>Whether you prefer a quick flight or a scenic train journey, here is your complete guide on <strong>how to reach Kashmir</strong>.</p>

            <h2>1. By Air (Fastest Way)</h2>
            <p>The <strong>Sheikh ul-Alam International Airport (SXR)</strong> in Srinagar is well connected to major Indian cities like Delhi, Mumbai, Bangalore, and Chandigarh.</p>
            <ul>
                <li><strong>Flight Duration:</strong> Delhi to Srinagar is approx 1 hour 30 mins.</li>
                <li><strong>Tip:</strong> Book window seats on the left side (while flying in) for stunning views of the Himalayas.</li>
            </ul>

            <h2>2. By Train (The Game Changer)</h2>
            <p>The <strong>Udhampur-Srinagar-Baramulla Rail Link (USBRL)</strong> is the engineering marvel of India. In 2026, direct trains like <strong>Vande Bharat</strong> are expected to connect Jammu/Katra directly to Srinagar.</p>
            <ul>
                <li><strong>Current Status:</strong> Trains run up to Katra/Sangaldan. You may need to take a cab for the remaining journey until full connectivity is operational.</li>
                <li><strong>Experience:</strong> Crossing the Chenab Bridge (world's highest rail bridge) is a once-in-a-lifetime experience.</li>
            </ul>

            <h2>3. By Road (Scenic Route)</h2>
            <p>The Jammu-Srinagar National Highway (NH-44) is the lifeline of the valley. The journey takes about 7-9 hours depending on traffic.</p>
            <ul>
                <li><strong>Bus:</strong> Luxury Volvo buses are available from Delhi and Jammu.</li>
                <li><strong>Self Drive:</strong> Recommended only for experienced drivers due to mountain terrain.</li>
            </ul>

            <h2>Conclusion</h2>
            <p>For most tourists, flying remains the most convenient option. However, train enthusiasts should definitely watch out for the full railway opening in 2026!</p>
        """
    }
]

# 1. Create Individual Blog Files
for blog in new_blogs:
    with open(template_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # Update Title
    soup.title.string = f"{blog['title']} | AKTASHAF KASHMIR"
    
    # Update Meta Description
    meta_desc = soup.find('meta', {'name': 'description'})
    if meta_desc:
        meta_desc['content'] = blog['description']
        
    # Update H1
    h1 = soup.find('h1', class_='blog-single-title')
    if h1:
        h1.string = blog['title']
        
    # Update Category meta
    meta_spans = soup.find('div', class_='blog-single-meta').find_all('span')
    if len(meta_spans) > 1:
        # 2nd span is category in the template structure logic (0=date, 1=cat, 2=time) - Date already removed by previous script?
        # Let's re-find based on icon class or text
        for span in meta_spans:
            if span.find('i', class_='fa-folder'):
                span.contents[2].replace_with(f" {blog['category']}") # contents[0]=i, contents[1]=space/text
                
    # Update Image - Use placeholders as we don't have these real images yet, user can upload later or we use generic
    img = soup.find('div', class_='blog-single-image').find('img')
    if img:
        img['src'] = f"../images/{blog['image']}" 
        img['onerror'] = f"this.src='https://placehold.co/1200x600/e0e0e0/333333?text={blog['category'].replace(' ','+')}'"
        img['alt'] = blog['title']

    # Update Content Body
    body = soup.find('div', class_='blog-content-body')
    if body:
        # Keep the TOC if needed, but easier to replace the specific content part
        # For simplicity, we replace the main P tags and headers ensuring we don't break structure
        # We will create a new tag content from the blog['content_intro']
        new_content_soup = BeautifulSoup(blog['content_intro'], 'html.parser')
        
        # Clear existing paragraphs and headers in body but keep valid divs if any unique ones exist? 
        # The template has specific structure. Let's just wipe the children that are p/h2/ul and append new.
        for tag in body.find_all(['p', 'h2', 'ul', 'h3', 'div'], recursive=False):
            if 'toc-box' not in tag.get('class', []):
                 tag.decompose()
        
        body.append(new_content_soup)

    # Save
    out_path = os.path.join(base_dir, "blogs", blog['filename'])
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(str(soup.prettify()))
    print(f"Created: {out_path}")


# 2. Update blogs.html Listing
listing_path = os.path.join(base_dir, "blogs.html")
with open(listing_path, 'r', encoding='utf-8') as f:
    list_soup = BeautifulSoup(f.read(), 'html.parser')

grid = list_soup.find('div', class_='blog-grid')
if grid:
    # Prepare new cards HTML
    for blog in new_blogs:
        new_card = list_soup.new_tag('article', **{'class': 'blog-card'})
        
        inner_html = f"""
        <div class="blog-image">
            <img src="images/{blog['image']}" alt="{blog['title']}" onerror="this.src='https://placehold.co/600x400/e0e0e0/333333?text={blog['shorter_title'].replace(' ', '+')}'">
            <div class="blog-category">{blog['category']}</div>
        </div>
        <div class="blog-content">
            <div class="blog-meta">
                 <!-- Date removed -->
            </div>
            <h3>
                <a href="blogs/{blog['filename']}">{blog['title']}</a>
            </h3>
            <p>{blog['description']}</p>
            <a href="blogs/{blog['filename']}" class="read-more">Read More <i class="fas fa-arrow-right"></i></a>
        </div>
        """
        new_card.append(BeautifulSoup(inner_html, 'html.parser'))
        
        # Insert at the beginning of the grid (prepend)
        grid.insert(0, new_card)

    with open(listing_path, 'w', encoding='utf-8') as f:
        f.write(str(list_soup.prettify()))
    print("Updated blogs.html with 3 new posts.")
