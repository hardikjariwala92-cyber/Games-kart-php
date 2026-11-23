import os
import sys
from PIL import Image, ImageDraw, ImageFont
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

os.makedirs('doc_images', exist_ok=True)

# -------------------------------------------------------------
# 1. HELPER FUNCTIONS TO GENERATE DIAGRAMS WITH PIL
# -------------------------------------------------------------
def get_font(size=14, bold=False):
    # Try system fonts, fallback to default
    try:
        font_name = "arialbd.ttf" if bold else "arial.ttf"
        return ImageFont.truetype(font_name, size)
    except:
        return ImageFont.load_default()

def draw_rounded_rect(draw, box, radius, fill, outline, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def generate_flowchart():
    img = Image.new('RGB', (1000, 1300), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    f_title = get_font(20, True)
    f_bold = get_font(13, True)
    f_reg = get_font(11, False)
    f_small = get_font(10, False)

    # Header
    draw.rectangle([0, 0, 1000, 60], fill='#7A1CAC')
    draw.text((320, 18), "GAMEKART - SYSTEM FLOWCHART", fill='#FFFFFF', font=f_title)

    # Start
    draw_rounded_rect(draw, [400, 80, 600, 130], 25, '#2E073F', '#CE5CFF', 3)
    draw.text((455, 95), "START / LOAD", fill='#FFFFFF', font=f_bold)

    # Arrow down
    draw.line([(500, 130), (500, 160)], fill='#7A1CAC', width=3)
    draw.polygon([(495, 155), (505, 155), (500, 165)], fill='#7A1CAC')

    # Home / Portal Gateway
    draw_rounded_rect(draw, [350, 165, 650, 220], 10, '#F6EBFF', '#AD49E1', 2)
    draw.text((390, 183), "Browse Products / Portal Gateway", fill='#2E073F', font=f_bold)

    # Arrow down
    draw.line([(500, 220), (500, 255)], fill='#7A1CAC', width=3)
    draw.polygon([(495, 250), (505, 250), (500, 260)], fill='#7A1CAC')

    # Decision: User Authenticated?
    # Diamond: (500, 260), (620, 320), (500, 380), (380, 320)
    draw.polygon([(500, 260), (620, 320), (500, 380), (380, 320)], fill='#EBD3F8', outline='#7A1CAC')
    draw.text((435, 305), "User Logged In?", fill='#2E073F', font=f_bold)

    # NO branch -> Login / Register
    draw.line([(380, 320), (220, 320), (220, 360)], fill='#CE5CFF', width=3)
    draw.polygon([(215, 355), (225, 355), (220, 365)], fill='#CE5CFF')
    draw.text((290, 300), "NO", fill='#E11D48', font=f_bold)

    draw_rounded_rect(draw, [120, 365, 320, 420], 8, '#FFFFFF', '#7A1CAC', 2)
    draw.text((150, 383), "Register / Login (clogin.php)", fill='#2E073F', font=f_bold)

    # Return from login
    draw.line([(220, 420), (220, 450), (450, 450), (450, 465)], fill='#7A1CAC', width=2)
    draw.polygon([(445, 460), (455, 460), (450, 470)], fill='#7A1CAC')

    # YES branch
    draw.line([(500, 380), (500, 470)], fill='#10B981', width=3)
    draw.polygon([(495, 465), (505, 465), (500, 475)], fill='#10B981')
    draw.text((510, 410), "YES", fill='#10B981', font=f_bold)

    # Product Catalog & Add to Cart
    draw_rounded_rect(draw, [350, 475, 650, 530], 10, '#F6EBFF', '#AD49E1', 2)
    draw.text((380, 493), "Select Gear & Add to Cart (tblcart)", fill='#2E073F', font=f_bold)

    # Arrow down
    draw.line([(500, 530), (500, 565)], fill='#7A1CAC', width=3)
    draw.polygon([(495, 560), (505, 560), (500, 570)], fill='#7A1CAC')

    # View Cart & Review Quantities
    draw_rounded_rect(draw, [350, 570, 650, 625], 10, '#FFFFFF', '#7A1CAC', 2)
    draw.text((385, 588), "View Shopping Cart (cart.php)", fill='#2E073F', font=f_bold)

    # Arrow down
    draw.line([(500, 625), (500, 660)], fill='#7A1CAC', width=3)
    draw.polygon([(495, 655), (505, 655), (500, 665)], fill='#7A1CAC')

    # Decision: Select Payment Method
    draw.polygon([(500, 665), (630, 725), (500, 785), (370, 725)], fill='#EBD3F8', outline='#7A1CAC')
    draw.text((420, 715), "Select Payment Mode", fill='#2E073F', font=f_bold)

    # 3 branches: UPI (Left), Card (Middle), COD (Right)
    # UPI
    draw.line([(370, 725), (200, 725), (200, 810)], fill='#7A1CAC', width=2)
    draw.polygon([(195, 805), (205, 805), (200, 815)], fill='#7A1CAC')
    draw.text((250, 705), "UPI / QR", fill='#7A1CAC', font=f_bold)
    draw_rounded_rect(draw, [100, 815, 300, 880], 8, '#FCF8FF', '#AD49E1', 2)
    draw.text((120, 830), "Generate UPI QR Code", fill='#2E073F', font=f_bold)
    draw.text((125, 850), "upi://pay?pa=...&am=...", fill='#6B7280', font=f_small)

    # Card
    draw.line([(500, 785), (500, 815)], fill='#7A1CAC', width=2)
    draw.polygon([(495, 810), (505, 810), (500, 820)], fill='#7A1CAC')
    draw.text((510, 792), "Debit/Credit", fill='#7A1CAC', font=f_bold)
    draw_rounded_rect(draw, [400, 820, 600, 880], 8, '#FCF8FF', '#AD49E1', 2)
    draw.text((425, 835), "Enter Card & CVV", fill='#2E073F', font=f_bold)
    draw.text((435, 855), "Client-side Validation", fill='#6B7280', font=f_small)

    # COD
    draw.line([(630, 725), (800, 725), (800, 815)], fill='#7A1CAC', width=2)
    draw.polygon([(795, 810), (805, 810), (800, 820)], fill='#7A1CAC')
    draw.text((690, 705), "Cash on Delivery", fill='#7A1CAC', font=f_bold)
    draw_rounded_rect(draw, [700, 820, 900, 880], 8, '#FCF8FF', '#AD49E1', 2)
    draw.text((735, 835), "Select COD Mode", fill='#2E073F', font=f_bold)
    draw.text((730, 855), "Pay on Doorstep Delivery", fill='#6B7280', font=f_small)

    # Merge to Place Order / Database Transaction
    draw.line([(200, 880), (200, 920), (500, 920)], fill='#7A1CAC', width=2)
    draw.line([(500, 880), (500, 920)], fill='#7A1CAC', width=2)
    draw.line([(800, 880), (800, 920), (500, 920)], fill='#7A1CAC', width=2)
    draw.line([(500, 920), (500, 950)], fill='#7A1CAC', width=3)
    draw.polygon([(495, 945), (505, 945), (500, 955)], fill='#7A1CAC')

    # Place Order Handler (placeorder.php)
    draw_rounded_rect(draw, [320, 955, 680, 1025], 10, '#EBD3F8', '#7A1CAC', 2)
    draw.text((360, 970), "Execute Checkout (placeorder.php)", fill='#2E073F', font=f_bold)
    draw.text((345, 995), "INSERT into tblorder & tblorderdetails | Clear tblcart", fill='#4A0E6E', font=f_small)

    # Arrow down
    draw.line([(500, 1025), (500, 1060)], fill='#7A1CAC', width=3)
    draw.polygon([(495, 1055), (505, 1055), (500, 1065)], fill='#7A1CAC')

    # Confirmation & Orders View
    draw_rounded_rect(draw, [340, 1065, 660, 1125], 10, '#F6EBFF', '#10B981', 2)
    draw.text((365, 1083), "Order Confirmation & Receipt (orders.php)", fill='#065F46', font=f_bold)
    draw.text((390, 1103), "View Live UPI QR & Tracking", fill='#6B7280', font=f_small)

    # Arrow down
    draw.line([(500, 1125), (500, 1160)], fill='#7A1CAC', width=3)
    draw.polygon([(495, 1155), (505, 1155), (500, 1165)], fill='#7A1CAC')

    # Stop
    draw_rounded_rect(draw, [400, 1165, 600, 1215], 25, '#2E073F', '#CE5CFF', 3)
    draw.text((475, 1182), "END", fill='#FFFFFF', font=f_bold)

    img.save('doc_images/flowchart_system.png')
    print("Flowchart generated.")

def generate_dfd():
    # DFD Level 0 & Level 1
    img = Image.new('RGB', (1000, 600), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    f_title = get_font(18, True)
    f_bold = get_font(12, True)
    f_reg = get_font(10, False)

    # Header
    draw.rectangle([0, 0, 1000, 50], fill='#2E073F')
    draw.text((320, 15), "DATA FLOW DIAGRAM (DFD LEVEL 0 - CONTEXT LEVEL)", fill='#FFFFFF', font=f_title)

    # Central Process Bubble (0.0)
    draw.ellipse([380, 180, 620, 420], fill='#F6EBFF', outline='#7A1CAC', width=3)
    draw.text((470, 270), "0.0", fill='#7A1CAC', font=f_bold)
    draw.text((415, 295), "GAMEKART E-COMMERCE", fill='#2E073F', font=f_bold)
    draw.text((435, 320), "SYSTEM PORTAL", fill='#2E073F', font=f_bold)

    # Entity: Customer (Left)
    draw_rounded_rect(draw, [50, 240, 230, 360], 8, '#2E073F', '#CE5CFF', 2)
    draw.text((95, 290), "CUSTOMER / USER", fill='#FFFFFF', font=f_bold)

    # Entity: Administrator (Right)
    draw_rounded_rect(draw, [770, 240, 950, 360], 8, '#2E073F', '#CE5CFF', 2)
    draw.text((810, 290), "ADMINISTRATOR", fill='#FFFFFF', font=f_bold)

    # Entity: Payment Gateway / UPI Server (Top)
    draw_rounded_rect(draw, [400, 70, 600, 130], 8, '#7A1CAC', '#AD49E1', 2)
    draw.text((420, 92), "UPI QR / PAYMENT SERVER", fill='#FFFFFF', font=f_bold)

    # Entity: Database Data Store (Bottom)
    draw.rectangle([400, 470, 600, 540], fill='#FFFFFF', outline='#7A1CAC', width=2)
    draw.line([(400, 470), (400, 540)], fill='#7A1CAC', width=4)
    draw.line([(600, 470), (600, 540)], fill='#7A1CAC', width=4)
    draw.text((435, 495), "D1: MySQL (kmart)", fill='#2E073F', font=f_bold)

    # Arrows Customer <-> System
    draw.line([(230, 270), (380, 270)], fill='#7A1CAC', width=2)
    draw.polygon([(375, 265), (385, 270), (375, 275)], fill='#7A1CAC')
    draw.text((245, 250), "Registration / Orders / Cart", fill='#2E073F', font=f_reg)

    draw.line([(380, 330), (230, 330)], fill='#AD49E1', width=2)
    draw.polygon([(235, 325), (225, 330), (235, 335)], fill='#AD49E1')
    draw.text((240, 335), "Product Catalog / Invoices", fill='#7A1CAC', font=f_reg)

    # Arrows System <-> Admin
    draw.line([(770, 270), (620, 270)], fill='#7A1CAC', width=2)
    draw.polygon([(625, 265), (615, 270), (625, 275)], fill='#7A1CAC')
    draw.text((635, 250), "Product CRUD / Order Dispatch", fill='#2E073F', font=f_reg)

    draw.line([(620, 330), (770, 330)], fill='#AD49E1', width=2)
    draw.polygon([(765, 325), (775, 330), (765, 335)], fill='#AD49E1')
    draw.text((640, 335), "Reports / Analytics / Users", fill='#7A1CAC', font=f_reg)

    # Arrows System <-> UPI
    draw.line([(470, 180), (470, 130)], fill='#10B981', width=2)
    draw.polygon([(465, 135), (470, 125), (475, 135)], fill='#10B981')
    draw.text((370, 150), "QR Payload", fill='#065F46', font=f_reg)

    draw.line([(530, 130), (530, 180)], fill='#10B981', width=2)
    draw.polygon([(525, 175), (530, 185), (535, 175)], fill='#10B981')
    draw.text((540, 150), "Payment Status", fill='#065F46', font=f_reg)

    # Arrows System <-> DB
    draw.line([(470, 420), (470, 470)], fill='#7A1CAC', width=2)
    draw.polygon([(465, 465), (470, 475), (475, 465)], fill='#7A1CAC')
    draw.text((385, 440), "Write / SQL Insert", fill='#7A1CAC', font=f_reg)

    draw.line([(530, 470), (530, 420)], fill='#7A1CAC', width=2)
    draw.polygon([(525, 425), (530, 415), (535, 425)], fill='#7A1CAC')
    draw.text((540, 440), "Fetch / Query Res", fill='#7A1CAC', font=f_reg)

    img.save('doc_images/dfd_level0.png')
    print("DFD generated.")

def generate_er_diagram():
    img = Image.new('RGB', (1000, 750), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    f_title = get_font(18, True)
    f_bold = get_font(12, True)
    f_reg = get_font(10, False)
    f_pk = get_font(10, True)

    # Header
    draw.rectangle([0, 0, 1000, 50], fill='#7A1CAC')
    draw.text((340, 15), "ENTITY-RELATIONSHIP (E-R) DIAGRAM", fill='#FFFFFF', font=f_title)

    def draw_entity(x, y, title, attrs):
        w, h = 180, 30 + len(attrs)*22
        # Title bar
        draw.rectangle([x, y, x+w, y+30], fill='#2E073F', outline='#7A1CAC', width=2)
        draw.text((x+12, y+7), title, fill='#FFFFFF', font=f_bold)
        # Body
        draw.rectangle([x, y+30, x+w, y+h], fill='#FCF8FF', outline='#7A1CAC', width=2)
        curr_y = y + 36
        for attr, is_pk, is_fk in attrs:
            prefix = "[PK] " if is_pk else ("[FK] " if is_fk else "")
            color = '#AD49E1' if is_pk else ('#E11D48' if is_fk else '#1F2937')
            draw.text((x+10, curr_y), prefix + attr, fill=color, font=f_pk if (is_pk or is_fk) else f_reg)
            curr_y += 22
        return (x, y, w, h)

    # 1. tbluser
    e_user = draw_entity(60, 100, "tbluser (Users)", [
        ("userid", True, False),
        ("uname", False, False),
        ("email", False, False),
        ("pass", False, False),
        ("mobile", False, False),
        ("role", False, False)
    ])

    # 2. tblcat
    e_cat = draw_entity(60, 370, "tblcat (Category)", [
        ("catid", True, False),
        ("catname", False, False)
    ])

    # 3. tblpro
    e_pro = draw_entity(410, 350, "tblpro (Products)", [
        ("productid", True, False),
        ("catid", False, True),
        ("title", False, False),
        ("price", False, False),
        ("mrp", False, False),
        ("des", False, False),
        ("img", False, False)
    ])

    # 4. tblcart
    e_cart = draw_entity(410, 100, "tblcart (Cart)", [
        ("cartid", True, False),
        ("userid", False, True),
        ("productid", False, True),
        ("qty", False, False)
    ])

    # 5. tblorder
    e_order = draw_entity(760, 100, "tblorder (Orders)", [
        ("orderid", True, False),
        ("userid", False, True),
        ("orderdate", False, False),
        ("totalamout", False, False)
    ])

    # 6. tblorderdetails
    e_orderdet = draw_entity(760, 350, "tblorderdetails", [
        ("orderdetailid", True, False),
        ("orderid", False, True),
        ("productid", False, True),
        ("qty", False, False),
        ("price", False, False),
        ("subtotal", False, False)
    ])

    # Draw Relation Lines with Diamond symbols
    def draw_rel(x1, y1, x2, y2, label):
        draw.line([(x1, y1), (x2, y2)], fill='#7A1CAC', width=2)
        mx, my = (x1+x2)//2, (y1+y2)//2
        draw.polygon([(mx, my-12), (mx+22, my), (mx, my+12), (mx-22, my)], fill='#EBD3F8', outline='#7A1CAC')
        draw.text((mx-14, my-6), label, fill='#2E073F', font=get_font(9, True))

    # user -> cart (1:N)
    draw_rel(240, 160, 410, 160, "1:N")
    # user -> order (1:N)
    draw.line([(240, 130), (760, 130)], fill='#7A1CAC', width=2)
    draw.polygon([(500, 118), (522, 130), (500, 142), (478, 130)], fill='#EBD3F8', outline='#7A1CAC')
    draw.text((486, 124), "1:N", fill='#2E073F', font=get_font(9, True))

    # cat -> pro (1:N)
    draw_rel(240, 430, 410, 430, "1:N")
    # pro -> cart (1:N)
    draw_rel(500, 350, 500, 260, "1:N")
    # order -> orderdetails (1:N)
    draw_rel(850, 250, 850, 350, "1:N")
    # pro -> orderdetails (1:N)
    draw_rel(590, 430, 760, 430, "1:N")

    # Legend at bottom
    draw_rounded_rect(draw, [60, 630, 940, 710], 8, '#F6EBFF', '#AD49E1', 1)
    draw.text((80, 645), "E-R Schema Legend:", fill='#2E073F', font=f_bold)
    draw.text((80, 672), "[PK] Primary Key (Unique Identifier)", fill='#AD49E1', font=f_bold)
    draw.text((380, 672), "[FK] Foreign Key (Referential Integrity)", fill='#E11D48', font=f_bold)
    draw.text((680, 672), "Diamonds represent 1:N Cardinality", fill='#7A1CAC', font=f_bold)

    img.save('doc_images/er_diagram.png')
    print("ER Diagram generated.")

def generate_usecase_diagram():
    img = Image.new('RGB', (1000, 700), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    f_title = get_font(18, True)
    f_bold = get_font(11, True)
    f_reg = get_font(10, False)

    # Header
    draw.rectangle([0, 0, 1000, 50], fill='#2E073F')
    draw.text((360, 15), "UML USE CASE DIAGRAM", fill='#FFFFFF', font=f_title)

    # System boundary
    draw_rounded_rect(draw, [250, 70, 750, 660], 12, '#FCF8FF', '#7A1CAC', 2)
    draw.text((380, 85), "GameKart Online E-Commerce System", fill='#7A1CAC', font=f_bold)

    # Actor 1: Customer (Left)
    draw.ellipse([85, 230, 135, 280], fill='#EBD3F8', outline='#2E073F', width=2) # Head
    draw.line([(110, 280), (110, 360)], fill='#2E073F', width=3) # Body
    draw.line([(70, 310), (150, 310)], fill='#2E073F', width=3) # Arms
    draw.line([(110, 360), (80, 430)], fill='#2E073F', width=3) # Left Leg
    draw.line([(110, 360), (140, 430)], fill='#2E073F', width=3) # Right Leg
    draw.text((75, 445), "CUSTOMER", fill='#2E073F', font=f_bold)

    # Actor 2: Administrator (Right)
    draw.ellipse([865, 230, 915, 280], fill='#EBD3F8', outline='#2E073F', width=2) # Head
    draw.line([(890, 280), (890, 360)], fill='#2E073F', width=3) # Body
    draw.line([(850, 310), (930, 310)], fill='#2E073F', width=3) # Arms
    draw.line([(890, 360), (860, 430)], fill='#2E073F', width=3) # Left Leg
    draw.line([(890, 360), (920, 430)], fill='#2E073F', width=3) # Right Leg
    draw.text((850, 445), "ADMINISTRATOR", fill='#2E073F', font=f_bold)

    # Use Cases (Bubbles in Center)
    usecases = [
        ("Register & Login Account", 120),
        ("Browse Gaming Catalog & Search", 185),
        ("Add Products to Shopping Cart", 250),
        ("Checkout via Dynamic UPI QR / Card", 315),
        ("Track My Orders & Invoices", 380),
        ("Manage Product Catalog (CRUD)", 445),
        ("Process & Dispatch Orders", 510),
        ("View Analytics & User Management", 575),
    ]

    for uc_text, uc_y in usecases:
        draw.ellipse([340, uc_y, 660, uc_y+48], fill='#FFFFFF', outline='#AD49E1', width=2)
        draw.text((375, uc_y+16), uc_text, fill='#2E073F', font=f_bold)

    # Lines Customer -> Use Cases (1..5)
    for i in range(5):
        uy = usecases[i][1] + 24
        draw.line([(150, 330), (340, uy)], fill='#7A1CAC', width=2)

    # Lines Admin -> Use Cases (0, 1, 5, 6, 7)
    for i in [0, 1, 5, 6, 7]:
        uy = usecases[i][1] + 24
        draw.line([(850, 330), (660, uy)], fill='#AD49E1', width=2)

    img.save('doc_images/usecase_diagram.png')
    print("Use Case Diagram generated.")

# Execute diagram generators
generate_flowchart()
generate_dfd()
generate_er_diagram()
generate_usecase_diagram()

print("All diagram assets generated successfully in doc_images/!")
