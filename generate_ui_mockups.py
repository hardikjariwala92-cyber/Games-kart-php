import os
from PIL import Image, ImageDraw, ImageFont

def get_f(sz=14, bld=False):
    try:
        fn = "arialbd.ttf" if bld else "arial.ttf"
        return ImageFont.truetype(fn, sz)
    except:
        return ImageFont.load_default()

def draw_window_frame(draw, title, w=1000, h=650):
    # Mac/Modern style browser frame
    draw.rectangle([0, 0, w, 40], fill='#1E1B2E')
    # Traffic lights
    draw.ellipse([15, 13, 27, 25], fill='#EF4444')
    draw.ellipse([35, 13, 47, 25], fill='#F59E0B')
    draw.ellipse([55, 13, 67, 25], fill='#10B981')
    # URL bar
    draw.rounded_rectangle([100, 8, w-100, 32], radius=6, fill='#2D2742')
    draw.text((120, 11), f"https://localhost/php/{title}", fill='#A78BFA', font=get_f(11, False))

# 1. UI Home
def create_ui_home():
    img = Image.new('RGB', (1000, 650), color='#FCF8FF')
    draw = ImageDraw.Draw(img)
    draw_window_frame(draw, "chome.php")
    
    # Navbar
    draw.rectangle([0, 40, 1000, 95], fill='#17121A')
    draw.text((30, 56), "GAMEKART", fill='#CE5CFF', font=get_f(22, True))
    draw.text((170, 62), "THE GAMER GEAR STORE", fill='#A78BFA', font=get_f(11, True))
    draw.text((420, 62), "Home   Catalog   Battlestation   Orders   Cart (3)", fill='#FFFFFF', font=get_f(13, True))
    draw.rectangle([860, 52, 970, 85], fill='#CE5CFF')
    draw.text((880, 60), "Logout", fill='#FFFFFF', font=get_f(12, True))

    # Hero Banner
    draw.rounded_rectangle([30, 115, 970, 370], radius=16, fill='#17121A', outline='#CE5CFF', width=2)
    # Paste hero banner image if exists
    if os.path.exists("images/gamekart_hero_banner.jpg"):
        try:
            h_img = Image.open("images/gamekart_hero_banner.jpg").convert("RGB").resize((440, 240))
            img.paste(h_img, (510, 122))
        except: pass
    
    draw.rectangle([50, 135, 180, 160], fill='#CE5CFF')
    draw.text((60, 140), "NEXT-GEN GEAR", fill='#FFFFFF', font=get_f(11, True))
    draw.text((50, 175), "Dominate Every Match.", fill='#FFFFFF', font=get_f(24, True))
    draw.text((50, 210), "Upgrade to Pro Esports Hardware", fill='#CE5CFF', font=get_f(22, True))
    draw.text((50, 255), "Equip RTX 40-Series GPUs, OLED 240Hz Monitors, Optical Switches & Wireless Headsets.", fill='#9CA3AF', font=get_f(11, False))
    draw.rounded_rectangle([50, 295, 210, 340], radius=8, fill='#CE5CFF')
    draw.text((75, 310), "EXPLORE CATALOG", fill='#FFFFFF', font=get_f(13, True))

    # Features Row
    draw.rounded_rectangle([30, 390, 320, 480], radius=12, fill='#FFFFFF', outline='#E5C7F7', width=1)
    draw.text((45, 410), "⚡ FAST DISPATCH", fill='#CE5CFF', font=get_f(13, True))
    draw.text((45, 435), "Same-day dispatch on gaming peripherals.", fill='#6B7280', font=get_f(11, False))

    draw.rounded_rectangle([350, 390, 640, 480], radius=12, fill='#FFFFFF', outline='#E5C7F7', width=1)
    draw.text((365, 410), "🛡️ 100% GENUINE WARRANTY", fill='#CE5CFF', font=get_f(13, True))
    draw.text((365, 435), "All hardware covered by manufacturer.", fill='#6B7280', font=get_f(11, False))

    draw.rounded_rectangle([670, 390, 970, 480], radius=12, fill='#FFFFFF', outline='#E5C7F7', width=1)
    draw.text((685, 410), "💳 DYNAMIC UPI & CARD PAY", fill='#CE5CFF', font=get_f(13, True))
    draw.text((685, 435), "Instant QR code & secure 256-bit checkout.", fill='#6B7280', font=get_f(11, False))

    # Product spotlight
    draw.text((30, 505), "FEATURED PRO HARDWARE", fill='#17121A', font=get_f(16, True))
    draw.rounded_rectangle([30, 535, 250, 635], radius=10, fill='#FFFFFF', outline='#E5C7F7')
    draw.text((45, 550), "PlayStation 5 Console", fill='#17121A', font=get_f(12, True))
    draw.text((45, 575), "₹54,990", fill='#CE5CFF', font=get_f(15, True))

    draw.rounded_rectangle([270, 535, 490, 635], radius=10, fill='#FFFFFF', outline='#E5C7F7')
    draw.text((285, 550), "NVIDIA RTX 4080 GPU", fill='#17121A', font=get_f(12, True))
    draw.text((285, 575), "₹1,19,999", fill='#CE5CFF', font=get_f(15, True))

    draw.rounded_rectangle([510, 535, 730, 635], radius=10, fill='#FFFFFF', outline='#E5C7F7')
    draw.text((525, 550), "Logitech G815 RGB", fill='#17121A', font=get_f(12, True))
    draw.text((525, 575), "₹16,995", fill='#CE5CFF', font=get_f(15, True))

    draw.rounded_rectangle([750, 535, 970, 635], radius=10, fill='#FFFFFF', outline='#E5C7F7')
    draw.text((765, 550), "Samsung Odyssey G9", fill='#17121A', font=get_f(12, True))
    draw.text((765, 575), "₹1,45,000", fill='#CE5CFF', font=get_f(15, True))

    img.save("doc_images/ui_screenshot_home.png")
    print("UI Home generated.")

# 2. UI Cart & Payment
def create_ui_cart():
    img = Image.new('RGB', (1000, 650), color='#FCF8FF')
    draw = ImageDraw.Draw(img)
    draw_window_frame(draw, "cart.php")

    # Navbar
    draw.rectangle([0, 40, 1000, 95], fill='#17121A')
    draw.text((30, 56), "GAMEKART", fill='#CE5CFF', font=get_f(22, True))
    draw.text((420, 62), "Home   Catalog   Battlestation   Orders   Cart (Active)", fill='#FFFFFF', font=get_f(13, True))

    # Title
    draw.text((30, 110), "Your Gaming Shopping Cart & Settlement", fill='#17121A', font=get_f(20, True))

    # Left: Cart items table
    draw.rounded_rectangle([30, 150, 580, 530], radius=12, fill='#FFFFFF', outline='#E5C7F7', width=2)
    draw.rectangle([30, 150, 580, 190], fill='#F6EBFF')
    draw.text((45, 162), "Product Details", fill='#2E073F', font=get_f(12, True))
    draw.text((300, 162), "Price", fill='#2E073F', font=get_f(12, True))
    draw.text((390, 162), "Qty", fill='#2E073F', font=get_f(12, True))
    draw.text((470, 162), "Subtotal", fill='#2E073F', font=get_f(12, True))

    # Item 1
    draw.text((45, 205), "PlayStation 5 Console Edition", fill='#17121A', font=get_f(12, True))
    draw.text((45, 225), "Next-gen 4K 120Hz Ultra HD gaming", fill='#6B7280', font=get_f(10, False))
    draw.text((300, 215), "₹54,990", fill='#CE5CFF', font=get_f(13, True))
    draw.rectangle([390, 205, 430, 235], outline='#CBD5E1', fill='#FFFFFF')
    draw.text((405, 212), "1", fill='#17121A', font=get_f(12, True))
    draw.text((470, 215), "₹54,990", fill='#17121A', font=get_f(13, True))
    draw.line([(45, 250), (565, 250)], fill='#F3E8FF', width=1)

    # Item 2
    draw.text((45, 265), "Logitech G815 Lightsync RGB", fill='#17121A', font=get_f(12, True))
    draw.text((45, 285), "Low Profile Mechanical Gaming Keyboard", fill='#6B7280', font=get_f(10, False))
    draw.text((300, 275), "₹16,995", fill='#CE5CFF', font=get_f(13, True))
    draw.rectangle([390, 265, 430, 295], outline='#CBD5E1', fill='#FFFFFF')
    draw.text((405, 272), "1", fill='#17121A', font=get_f(12, True))
    draw.text((470, 275), "₹16,995", fill='#17121A', font=get_f(13, True))
    draw.line([(45, 310), (565, 310)], fill='#F3E8FF', width=1)

    # Item 3
    draw.text((45, 325), "Razer BlackShark V2 Pro Wireless", fill='#17121A', font=get_f(12, True))
    draw.text((45, 345), "Spatial THX Audio Esports Headset", fill='#6B7280', font=get_f(10, False))
    draw.text((300, 335), "₹18,499", fill='#CE5CFF', font=get_f(13, True))
    draw.rectangle([390, 325, 430, 355], outline='#CBD5E1', fill='#FFFFFF')
    draw.text((405, 332), "1", fill='#17121A', font=get_f(12, True))
    draw.text((470, 335), "₹18,499", fill='#17121A', font=get_f(13, True))

    draw.rounded_rectangle([45, 470, 200, 510], radius=6, fill='#F6EBFF')
    draw.text((60, 483), "← Continue Shopping", fill='#7A1CAC', font=get_f(11, True))
    draw.rounded_rectangle([420, 470, 565, 510], radius=6, fill='#CE5CFF')
    draw.text((440, 483), "Update Cart", fill='#FFFFFF', font=get_f(11, True))

    # Right: Payment Summary & Dynamic UPI QR
    draw.rounded_rectangle([610, 150, 970, 620], radius=14, fill='#FFFFFF', outline='#CE5CFF', width=2)
    draw.text((630, 170), "Order Summary & Live Payment", fill='#2E073F', font=get_f(15, True))
    draw.text((630, 205), "Total Units: 3 items", fill='#6B7280', font=get_f(12, False))
    draw.text((630, 225), "Express Shipping: FREE", fill='#10B981', font=get_f(12, True))
    draw.line([(630, 250), (950, 250)], fill='#F3E8FF', width=1)
    draw.text((630, 260), "Grand Total:  ₹90,484", fill='#7A1CAC', font=get_f(18, True))

    # Payment Method Box
    draw.rounded_rectangle([630, 300, 950, 600], radius=10, fill='#F6EBFF', outline='#AD49E1', width=1)
    draw.text((645, 315), "⚡ Select Payment Option: [ UPI (Instant QR) ]", fill='#2E073F', font=get_f(11, True))
    
    # QR Box
    draw.rounded_rectangle([645, 345, 785, 485], radius=8, fill='#FFFFFF', outline='#CBD5E1', width=2)
    # Simple QR pattern preview
    draw.rectangle([660, 360, 690, 390], fill='#000000')
    draw.rectangle([665, 365, 685, 385], fill='#FFFFFF')
    draw.rectangle([670, 370, 680, 380], fill='#000000')

    draw.rectangle([740, 360, 770, 390], fill='#000000')
    draw.rectangle([745, 365, 765, 385], fill='#FFFFFF')
    draw.rectangle([750, 370, 760, 380], fill='#000000')

    draw.rectangle([660, 440, 690, 470], fill='#000000')
    draw.rectangle([665, 445, 685, 465], fill='#FFFFFF')
    draw.rectangle([670, 450, 680, 460], fill='#000000')

    draw.text((795, 355), "Merchant UPI ID:", fill='#6B7280', font=get_f(10, False))
    draw.text((795, 370), "9825904828@fam", fill='#2E073F', font=get_f(11, True))
    draw.text((795, 395), "Payable Amount:", fill='#6B7280', font=get_f(10, False))
    draw.text((795, 410), "₹90,484", fill='#CE5CFF', font=get_f(16, True))

    draw.rounded_rectangle([645, 500, 935, 545], radius=8, fill='#CE5CFF')
    draw.text((730, 515), "✓ I Have Paid", fill='#FFFFFF', font=get_f(13, True))

    draw.text((660, 560), "🔒 256-Bit SSL Encrypted Gaming Checkout", fill='#059669', font=get_f(10, True))

    img.save("doc_images/ui_screenshot_cart.png")
    print("UI Cart generated.")

# 3. UI Admin Dashboard
def create_ui_admin():
    img = Image.new('RGB', (1000, 650), color='#17121A')
    draw = ImageDraw.Draw(img)
    draw_window_frame(draw, "dashboard.php")

    # Admin Sidebar
    draw.rectangle([0, 40, 220, 650], fill='#201726')
    draw.text((25, 60), "GAMEKART", fill='#CE5CFF', font=get_f(18, True))
    draw.text((25, 82), "ADMIN CONTROL CENTER", fill='#9CA3AF', font=get_f(9, True))
    
    links = [("📊 Overview", True), ("🎮 Manage Products", False), ("📦 Orders Central", False), ("👥 Users Directory", False), ("📂 Categories", False), ("⚙️ Settings", False)]
    y_l = 125
    for l_text, act in links:
        if act:
            draw.rounded_rectangle([15, y_l-5, 205, y_l+30], radius=6, fill='#CE5CFF')
            draw.text((25, y_l+2), l_text, fill='#FFFFFF', font=get_f(12, True))
        else:
            draw.text((25, y_l+2), l_text, fill='#CBD5E1', font=get_f(12, False))
        y_l += 45

    # Main Area
    draw.text((250, 65), "Admin Mission Control", fill='#FFFFFF', font=get_f(22, True))
    draw.text((250, 95), "Real-time store metrics, order processing, and product catalog", fill='#9CA3AF', font=get_f(11, False))

    # Metric Cards
    # Card 1
    draw.rounded_rectangle([250, 130, 410, 220], radius=12, fill='#251C2D', outline='#CE5CFF', width=1)
    draw.text((270, 145), "TOTAL REVENUE", fill='#9CA3AF', font=get_f(10, True))
    draw.text((270, 168), "₹4,82,450", fill='#FFFFFF', font=get_f(18, True))
    draw.text((270, 196), "↑ +18.4% this week", fill='#10B981', font=get_f(10, True))

    # Card 2
    draw.rounded_rectangle([430, 130, 590, 220], radius=12, fill='#251C2D', outline='#AD49E1', width=1)
    draw.text((450, 145), "TOTAL ORDERS", fill='#9CA3AF', font=get_f(10, True))
    draw.text((450, 168), "28 Orders", fill='#FFFFFF', font=get_f(18, True))
    draw.text((450, 196), "All Dispatched", fill='#10B981', font=get_f(10, True))

    # Card 3
    draw.rounded_rectangle([610, 130, 770, 220], radius=12, fill='#251C2D', outline='#7A1CAC', width=1)
    draw.text((630, 145), "HARDWARE IN STOCK", fill='#9CA3AF', font=get_f(10, True))
    draw.text((630, 168), "10 Items", fill='#FFFFFF', font=get_f(18, True))
    draw.text((630, 196), "Catalog Synced", fill='#A78BFA', font=get_f(10, True))

    # Card 4
    draw.rounded_rectangle([790, 130, 950, 220], radius=12, fill='#251C2D', outline='#4A0E6E', width=1)
    draw.text((810, 145), "ACTIVE USERS", fill='#9CA3AF', font=get_f(10, True))
    draw.text((810, 168), "14 Gamers", fill='#FFFFFF', font=get_f(18, True))
    draw.text((810, 196), "Online Verified", fill='#10B981', font=get_f(10, True))

    # Inventory Table Preview
    draw.rounded_rectangle([250, 250, 950, 610], radius=12, fill='#251C2D', outline='#3B2D46', width=1)
    draw.text((270, 270), "Live Product Inventory & Stock Control", fill='#FFFFFF', font=get_f(15, True))

    draw.rectangle([270, 305, 930, 340], fill='#31243B')
    draw.text((285, 317), "ID", fill='#CE5CFF', font=get_f(11, True))
    draw.text((330, 317), "Product Name", fill='#CE5CFF', font=get_f(11, True))
    draw.text((610, 317), "Price", fill='#CE5CFF', font=get_f(11, True))
    draw.text((710, 317), "MRP", fill='#CE5CFF', font=get_f(11, True))
    draw.text((810, 317), "Actions", fill='#CE5CFF', font=get_f(11, True))

    items = [
        ("01", "PlayStation 5 Console Edition", "₹54,990", "₹59,990"),
        ("02", "NVIDIA GeForce RTX 4080 GPU", "₹1,19,999", "₹1,35,000"),
        ("03", "Logitech G815 Lightsync Mechanical", "₹16,995", "₹19,995"),
        ("04", "Samsung Odyssey G9 49\" 240Hz", "₹1,45,000", "₹1,69,990"),
        ("05", "Razer BlackShark V2 Pro Wireless", "₹18,499", "₹22,999"),
        ("06", "Secretlab TITAN Evo 2024 Chair", "₹42,500", "₹49,990")
    ]
    y_row = 350
    for pid, ptitle, pr, mrp in items:
        draw.text((285, y_row+3), pid, fill='#9CA3AF', font=get_f(11, False))
        draw.text((330, y_row+3), ptitle, fill='#FFFFFF', font=get_f(11, True))
        draw.text((610, y_row+3), pr, fill='#CE5CFF', font=get_f(11, True))
        draw.text((710, y_row+3), mrp, fill='#6B7280', font=get_f(11, False))
        draw.rounded_rectangle([805, y_row, 855, y_row+24], radius=4, fill='#3B82F6')
        draw.text((818, y_row+4), "Edit", fill='#FFFFFF', font=get_f(10, True))
        draw.rounded_rectangle([865, y_row, 920, y_row+24], radius=4, fill='#EF4444')
        draw.text((875, y_row+4), "Delete", fill='#FFFFFF', font=get_f(10, True))
        draw.line([(270, y_row+32), (930, y_row+32)], fill='#31243B', width=1)
        y_row += 38

    img.save("doc_images/ui_screenshot_admin.png")
    print("UI Admin generated.")

create_ui_home()
create_ui_cart()
create_ui_admin()
