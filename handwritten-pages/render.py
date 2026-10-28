import random, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

W, H = 1240, 1754
CELL = 24
FONT_PATH = r"C:\projects\stories-site\handwritten-pages\Caveat.ttf"
OUT = r"C:\projects\stories-site\handwritten-pages"
random.seed(11)

# token styles: 0 normal, 1 strikethrough, 2 small raised insertion
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
    ("n", [("1) Я часто замечал   2) I would play in the park every day after school.   3) Я часто замечал", 0)]),
    ("n", [("4) I would eat vegetables with each meal.   5) Я часто замечал", 0)]),
    ("n", [("б) I would go for a long bike ride every weekend.", 0)]),
    ("k", "2"),
    ("n", [("Cause: The division of society into two classes and the complete removal of physical danger, difficulties,", 0)]),
    ("n", [("and the need to work.", 0)]),
    ("n", [("Time/Delay: Over a long period of time, the wealthy class lived in such perfect comfort and safety that", 0)]),
    ("n", [("they stopped using their minds and bodies.", 0)]),
    ("n", [("Effect: As a result, the Eloi became weak, lazy and childlike, losing their intelligence and strength", 0)]),
    ("n", [("because there were no challenges left to make them strong.", 0)]),
]

P3 = [
    ("n", [("In my opinion, basketball is popular in Russia. It's a very active kind of", 0)]),
    ("n", [("sport with simple rules, so It's interesting to watch and easy to play in it.", 0)]),
    ("n", [("I don't play any sport but I do different activities like going to", 0)]),
    ("n", [("the gym. It's the most interesting for me, so I like it more than", 0)]),
    ("n", [("other kinds of sport.", 0)]),
    ("h", "True/False"),
    ("n", [("Yes, I think P.E. is a very important school subject, but I haven't enough", 0)]),
    ("n", [("time for it.", 0)]),
    ("n", [("No, I'm not taking part in any sport clubs, but ago I was in", 0)]),
    ("n", [('karate club named "Hammer".', 0)]),
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
    ("n", [('students interrupted to correct it. This made even confident speakers reluctant to', 0)]),
    ("n", [('participate."', 0)]),
    ("n", [('2) C; evidence: "Whenever someone made a grammar or pronunciation mistake, other', 0)]),
    ("n", [('students interrupted to correct it."', 0)]),
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

def paper():
    im = Image.new("RGB", (W, H), (247, 245, 238))
    d = ImageDraw.Draw(im)
    for x in range(0, W, CELL):
        d.line([(x, 0), (x, H)], fill=(206, 214, 227), width=1)
    for y in range(0, H, CELL):
        d.line([(0, y), (W, y)], fill=(206, 214, 227), width=1)
    # binder holes
    for hy in (int(H * 0.30), int(H * 0.62)):
        d.ellipse([38 - 3, hy - 16 + 4, 38 + 16 - 3, hy + 16 + 4], fill=(105, 95, 80))
        d.ellipse([38, hy - 16, 38 + 16, hy + 16], fill=(52, 46, 40))
    return im, d

def draw_line(d, tokens, f, f_small, x, y, col):
    cx = x
    for txt, st in tokens:
        if st == 2:
            d.text((cx, y - 26 + random.randint(-2, 2)), txt, font=f_small, fill=col)
            cx += d.textlength(txt + " ", font=f_small)
        else:
            # word-by-word jitter
            for w in txt.split(" "):
                if w == "":
                    cx += d.textlength(" ", font=f); continue
                wy = y + random.randint(-2, 2)
                d.text((cx, wy), w, font=f, fill=col)
                ww = d.textlength(w, font=f)
                if st == 1:
                    d.line([(cx - 2, wy + f.size * 0.55), (cx + ww + 2, wy + f.size * 0.52)], fill=col, width=3)
                cx += ww + d.textlength(" ", font=f)

def render(lines, idx):
    im, d = paper()
    f_main = ImageFont.truetype(FONT_PATH, 38)
    f_head = ImageFont.truetype(FONT_PATH, 44)
    f_small = ImageFont.truetype(FONT_PATH, 26)
    n = len(lines)
    sp = min(56, (H - 200) // max(1, n))
    y = 90
    for kind, content in lines:
        col = (random.randint(24, 42), random.randint(46, 64), random.randint(135, 165))
        x = 96 + random.randint(0, 16)
        if kind == "k":
            s = 26
            d.line([(x, y + s * 0.5), (x + s * 0.4, y + s)], fill=col, width=3)
            d.line([(x + s * 0.4, y + s), (x + s, y - 2)], fill=col, width=3)
            d.text((x + s + 10, y - 6), content, font=ImageFont.truetype(FONT_PATH, 42), fill=col)
            y += 44
        else:
            f = f_head if kind == "h" else f_main
            toks = content if isinstance(content, list) else [(content, 0)]
            draw_line(d, toks, f, f_small, x, y, col)
            y += sp + (6 if kind == "h" else 0)
    return im

def lamp(im):
    # radial warm light from upper-left lamp, multiply falloff
    lw, lh = W // 20, H // 20
    cx, cy = 0.40 * lw, 0.16 * lh
    lm = Image.new("L", (lw, lh))
    px = []
    for j in range(lh):
        for i in range(lw):
            dist = math.hypot(i - cx, (j - cy) * 0.85) / lh
            v = 1.06 - 0.62 * (dist ** 1.55)
            px.append(max(102, min(255, int(v * 255))))
    lm.putdata(px)
    lm = lm.resize((W, H), Image.BILINEAR)
    black = Image.new("RGB", (W, H), (8, 6, 4))
    im = Image.composite(im, black, lm)
    # warm lamp tint
    r, g, b = im.split()
    r = r.point(lambda v: min(255, int(v * 1.14 + 10)))
    g = g.point(lambda v: int(v * 1.00))
    b = b.point(lambda v: int(v * 0.76))
    im = Image.merge("RGB", (r, g, b))
    im = ImageEnhance.Color(im).enhance(1.07)
    # photo noise + slight blur
    noise = Image.effect_noise((W, H), 13).convert("RGB")
    im = Image.blend(im, noise, 0.035)
    im = im.filter(ImageFilter.GaussianBlur(0.45))
    # soft vignette
    return im

pages = [P1, P2, P3, P4]
for i, lines in enumerate(pages, 1):
    im = render(lines, i)
    im = lamp(im)
    out = OUT + "\\page%d.jpg" % i
    im.save(out, quality=90)
    print("saved", out)
print("DONE")
