import random, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

W, H = 1240, 1754            # A4 page @150dpi
CELL = 24
FW, FH = 1330, 1880          # camera frame (page on desk)
FONT_PATH = r"C:\projects\stories-site\handwritten-pages\ReenieBeanie.ttf"
FONT_CYR = r"C:\projects\stories-site\handwritten-pages\Caveat.ttf"
OUT = r"C:\projects\stories-site\handwritten-pages"
random.seed(47)

P1 = [
    ("k", "1"),
    ("h", "Ex.8:  1) S   2) st   3) P   4) I   5) I   6) P"),
    ("h", "Ex.9"),
    ("n", [("1) I'm playing tennis at 10 o'clock.", 0)]),
    ("n", [("2) I'm seeing the dentist this afternoon.", 0)]),
    ("n", [("3) People will live on the moon one day.", 0)]),
    ("n", [("4) We're going to stay at the hotel.", 0)]),
    ("n", [("5) I'm going to travel around the ", 0), ("world", 1), (" ", 0), ("next year", 2), (".", 0)]),
    ("n", [("6) My mum won't let me go to the party.", 0)]),
    ("k", "2"),
    ("n", [("The Time Traveller noticed that the sun is jumping quickly across the", 0)]),
    ("n", [("sky, and trees are growing, changing, and dying in a matter of seconds as he travels", 0)]),
    ("n", [("through time.", 0)]),
    ("n", [("I think he might meet strange creatures on a new civilization because he has just", 0)]),
    ("n", [("stopped his machine in the year 802,701 and is now in a completely unknown", 0)]),
    ("n", [("future world.", 0)]),
]

P2 = [
    ("k", "1"),
    ("h", "Ex 6"),
    ("n", [("1) There used to be public telephones in the streets.", 0)]),
    ("n", [("2) Children used to play outside in the streets with their friends.", 0)]),
    ("n", [("3) Cars didn't use to have seat belts.", 0)]),
    ("n", [("4) TV didn't use to be in colour, only in black and white.", 0)]),
    ("n", [("5) People didn't use to take many photos, just on special occasions.", 0)]),
    ("n", [("6) Men used to love to go to a cinema to see a film.", 0)]),
    ("h", "Ex 9"),
    ("n", [("1) I would visit my grandma every summer.   2) I would play in the park every day after school.", 0)]),
    ("n", [("3) I would watch cartoons every morning.   4) I would eat vegetables with each meal.", 0)]),
    ("n", [("5) I would read a book before bed.   6) I would go for a long bike ride every weekend.", 0)]),
    ("k", "2"),
    ("n", [("Cause: The division of society into two classes and the complete removal of physical danger,", 0)]),
    ("n", [("difficulties, and the need to work.", 0)]),
    ("n", [("Time/Delay: Over a long period of time, the wealthy class lived in such perfect comfort", 0)]),
    ("n", [("and safety that they stopped using their minds and bodies.", 0)]),
    ("n", [("Effect: As a result, the Eloi became weak, lazy and childlike, losing their intelligence", 0)]),
    ("n", [("and strength because there were no challenges left to make them strong.", 0)]),
]

P3 = [
    ("n", [("In my opinion, basketball is popular in Russia. It's", 0)]),
    ("n", [("active", 1), (" very active kind of ", 0), ("sport", 1)]),
    ("n", [("with simple rules, so It's intresting to watch and easy to play in it.", 0)]),
    ("n", [("I don't play any sport but I do different activities like going to", 0)]),
    ("n", [("the gym. It's the most interesting for me, so I like it more than", 0)]),
    ("n", [("other kinds of sport.", 0)]),
    ("h", "True/False"),
    ("n", [("Yes, I think P.E. is a very important school subject, but I haven't enough", 0)]),
    ("n", [("time for it.", 0)]),
    ("n", [("No, I'm not taking part in any sport clubs, but ago I was in", 0)]),
    ("n", [("karate club named ", 0), ("~~~~~", 3), (' "Hammer".', 0)]),
    ("n", [("Yes, I really like going to the gym.", 0)]),
    ("n", [("Yes, sport helped my personal development. I became more confident.", 0)]),
    ("n", [("No, I'd not to become a professional sports person, because it can be", 0)]),
    ("n", [("dangerous for my health and I also dislike competitions.", 0)]),
    ("n", [("1) aim   2) hurt   3) bat   4) count   5) shots   6) exclusivity", 0)]),
    ("n", [("7) relatively   8) derive   9) versions   10) appeal", 0)]),
]

P4 = [
    ("k", "2"),
    ("n", [("An important turning point occurs when the Time Traveller realizes that the Eloi, the", 0)]),
    ("n", [("people of the future are not highly intelligent beings as he expected, but rather have", 0)]),
    ("n", [("the intelligence level of young children.", 0)]),
    ("n", [("This changes the situation because his hopes of finding a highly advanced future", 0)]),
    ("n", [("civilization are shattered, and he begins to feel sad and thinks that he built", 0)]),
    ("n", [('his Time Machine for no reason at all.', 0)]),
    ("n", [('The text supports this because the narrator states: "But one of them had asked me', 0)]),
    ("n", [('a very simple question, which showed him to be on the level of intelligence of one of our five-', 0)]),
    ("n", [('year-old children. He asked me, in fact, if I had come from the sun in a thunderstorm."', 0)]),
    ("n", [('1) B; evidence: "Whenever someone made a grammar or pronunciation mistake, other', 0)]),
    ("n", [("students", 1), (' interrupted to correct it. This made even confident speakers reluctant to', 0)]),
    ("n", [('participate."', 0)]),
    ("n", [('2) C; evidence: "Whenever someone made a grammar or pronunciation mistake, other', 0)]),
    ("n", [("students", 1), (' interrupted to correct it."', 0)]),
    ("n", [('3) B; evidence: "We didn\'t stop caring about accuracy. We simply stopped letting mistakes', 0)]),
    ("n", [('prevent us from getting started."', 0)]),
    ("n", [('4) C; evidence: "Students would record their ideas first and discuss possible improvements', 0)]),
    ("n", [('afterwards."', 0)]),
    ("n", [("Explanation (3): why it's a distractor. This is incorrect because the text explicitly", 0)]),
    ("n", [('says the opposite: "We didn\'t stop caring about accuracy."', 0)]),
    ("n", [("Yes, making mistakes is a crucial part of learning English. When you make a mistake and", 0)]),
    ("n", [("get corrected you remember the correct rule much better for future. Moreover if you", 0)]),
    ("n", [("are afraid of making mistakes you will never feel confident enough to actually speak, so", 0)]),
    ("n", [("accepting mistakes helps you practice more freely.", 0)]),
]

_fcache = {}
def get_font(path, size):
    key = (path, size)
    if key not in _fcache:
        _fcache[key] = ImageFont.truetype(path, size)
    return _fcache[key]

def has_cyr(s):
    return any(0x0400 <= ord(c) <= 0x04FF for c in s)

def paper():
    im = Image.new("RGB", (W, H), (255, 255, 253))
    d = ImageDraw.Draw(im)
    for x in range(0, W, CELL):
        d.line([(x, 0), (x, H)], fill=(199, 209, 224), width=1)
    for y in range(0, H, CELL):
        d.line([(0, y), (W, y)], fill=(199, 209, 224), width=1)
    for hy in (int(H * 0.28), int(H * 0.60)):
        d.ellipse([35, hy - 15 + 4, 53, hy + 15 + 4], fill=(60, 50, 40))
        d.ellipse([38, hy - 15, 54, hy + 15], fill=(38, 33, 28))
    return im, d

def ink():
    v = random.randint(0, 12)
    return (24 + v, 23 + v, 28 + v)

def draw_word(page, x, y, word, f, ang, col):
    pad = 12
    tw = int(f.getlength(word)) + pad * 2 + 6
    th = int(f.size * 2.0) + pad
    tile = Image.new("RGBA", (tw, th), (0, 0, 0, 0))
    td = ImageDraw.Draw(tile)
    td.text((pad, pad // 2), word, font=f, fill=col + (random.randint(198, 245),))
    tile = tile.rotate(ang, resample=Image.BICUBIC, expand=True)
    page.paste(tile, (int(x) - pad, int(y) - pad), tile)
    return f.getlength(word)

def scribble(page, x, y, wdt, h, col):
    dd = ImageDraw.Draw(page)
    for k in range(3):
        yy = y + h * 0.45 + k * 4 + random.randint(-2, 2)
        dd.line([(x - 4, yy), (x + wdt + 4, yy + random.randint(-4, 4))], fill=col, width=3)
    dd.line([(x - 2, y + h * 0.2), (x + wdt + 2, y + h * 0.85)], fill=col, width=2)

def render(lines, base, head):
    page, d0 = paper()
    f_small = get_font(FONT_PATH, 30)
    n = len(lines)
    sp = min(56, (H - 220) // max(1, n))
    y = 100.0
    avail = W - 150
    for kind, content in lines:
        x = 62 + random.randint(0, 34)
        drift = random.uniform(-2.5, 2.5)
        if kind == "k":
            col = ink(); s = 28
            d0.line([(x, y + s * 0.5), (x + s * 0.4, y + s)], fill=col, width=3)
            d0.line([(x + s * 0.4, y + s), (x + s, y - 3)], fill=col, width=3)
            draw_word(page, x + s + 12, y - 8, content, get_font(FONT_PATH, head), random.uniform(-2.5, 2.5), col)
            y += 46
            continue
        bs = head if kind == "h" else base
        toks = content if isinstance(content, list) else [(content, 0)]
        # flatten to words
        words = []
        for txt, st in toks:
            if st == 3:
                words.append((txt, 3)); continue
            for w in txt.split(" "):
                if w != "":
                    words.append((w, st))
        # measure & autofit
        total = 0.0
        mb = get_font(FONT_PATH, bs)
        for w, st in words:
            if st == 3: total += 96 + 10
            elif st == 2: total += f_small.getlength(w) + 8
            else: total += mb.getlength(w) + 7
        size = int(bs * min(1.0, avail / max(total, 1.0)))
        size = max(32, min(bs, size))
        f = get_font(FONT_PATH, size)
        fc = get_font(FONT_CYR, size)
        for w, st in words:
            col = ink()
            if st == 3:
                scribble(page, x, y - f.size * 0.4, random.randint(80, 105), f.size, col)
                x += 100
                continue
            if st == 2:
                ww = draw_word(page, x, y - 28, w, get_font(FONT_PATH, 28), random.uniform(-4, 4), col)
                x += ww + 6
                continue
            use = fc if has_cyr(w) else f
            ww = draw_word(page, x, y + drift + random.uniform(-3, 3), w, use, random.uniform(-7, 7), col)
            if st == 1:
                hy = y + drift + f.size * 0.40
                ImageDraw.Draw(page).line([(x - 4, hy), (x + ww + 4, hy + random.randint(-3, 3))], fill=col, width=3)
                ImageDraw.Draw(page).line([(x - 4, hy + 5), (x + ww + 4, hy + 3)], fill=col, width=2)
            x += ww + random.randint(2, 22)
            drift = max(-8.0, min(8.0, drift + random.uniform(-2.0, 2.0)))
        y += sp + (7 if kind == "h" else 0)
    return page

def lamp_light(im, cx_f, cy_f, strength, floor):
    lw, lh = W // 20, H // 20
    cx, cy = cx_f * lw, cy_f * lh
    lm = Image.new("L", (lw, lh))
    px = []
    for j in range(lh):
        for i in range(lw):
            dist = math.hypot(i - cx, (j - cy) * 0.9) / lh
            v = 1.0 - strength * (dist ** 1.45)
            px.append(max(floor, min(255, int(v * 255))))
    lm.putdata(px)
    lm = lm.resize(im.size, Image.BILINEAR)
    black = Image.new("RGB", im.size, (5, 4, 3))
    return Image.composite(im, black, lm)

def warm(im, rg, bb, add):
    r, g, b = im.split()
    r = r.point(lambda v: min(255, int(v * rg + add)))
    b = b.point(lambda v: int(v * bb))
    return Image.merge("RGB", (r, g, b))

pages = [P1, P2, P3, P4]
for i, lines in enumerate(pages, 1):
    page = render(lines, 46, 52)
    grain = Image.effect_noise((W, H), 9).convert("RGB")
    page = Image.blend(page, grain, 0.015)
    page = lamp_light(page, 0.42, 0.16, 0.28, 158)          # paper stays white
    # camera frame
    frame = Image.new("RGB", (FW, FH), (22, 17, 12))
    fd = ImageDraw.Draw(frame)
    for rr in range(900, 0, -40):
        a = int(60 * (1 - rr / 900.0))
        fd.ellipse([FW * 0.45 - rr, -350 - rr // 2, FW * 0.45 + rr, 550 + rr // 2], fill=(42 + a, 30 + a // 2, 18 + a // 3))
    ang = random.uniform(-1.8, 1.8)
    page_r = page.rotate(ang, resample=Image.BICUBIC, expand=True)
    sc = (FW * 0.955) / page_r.size[0]
    page_r = page_r.resize((int(page_r.size[0] * sc), int(page_r.size[1] * sc)), Image.LANCZOS)
    px = (FW - page_r.size[0]) // 2 + random.randint(-10, 10)
    py = (FH - page_r.size[1]) // 2 + random.randint(-10, 10)
    sh = Image.new("L", (FW, FH), 0)
    sd = ImageDraw.Draw(sh)
    sd.rectangle([px + 12, py + 16, px + page_r.size[0] + 12, py + page_r.size[1] + 16], fill=150)
    sh = sh.filter(ImageFilter.GaussianBlur(22))
    frame.paste(Image.new("RGB", (FW, FH), (0, 0, 0)), (0, 0), sh)
    frame.paste(page_r, (px, py))
    # frame-level light: darker photo, strong vignette
    fw2, fh2 = FW // 20, FH // 20
    lm = Image.new("L", (fw2, fh2))
    px2 = []
    ccx, ccy = 0.45 * fw2, 0.32 * fh2
    for j in range(fh2):
        for i2 in range(fw2):
            dist = math.hypot(i2 - ccx, (j - ccy) * 0.8) / fh2
            v = 0.96 - 0.50 * (dist ** 1.6)
            px2.append(max(52, min(255, int(v * 255))))
    lm.putdata(px2)
    lm = lm.resize((FW, FH), Image.BILINEAR)
    dark = Image.new("RGB", (FW, FH), (6, 5, 4))
    frame = Image.composite(frame, dark, lm)
    frame = ImageEnhance.Brightness(frame).enhance(0.94)
    cn = Image.effect_noise((FW, FH), 16).convert("RGB")
    frame = Image.blend(frame, cn, 0.045)
    frame = frame.filter(ImageFilter.GaussianBlur(0.55))
    out = OUT + "\\photo%d.jpg" % i
    frame.save(out, quality=88)
    print("saved", out)
print("DONE")
