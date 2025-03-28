from PIL import Image, ImageDraw, ImageFont


def make_image(usd_price):

    image = Image.open("assets/neutral.png")

    txt = Image.new("RGBA", image.size, (255, 255, 255, 0))

    draw = ImageDraw.Draw(txt)

    text = usd_price

    font_path = "assets/EagleLake-Regular.ttf" 
    font = ImageFont.truetype(font_path, 62)

    position = (180, 420)

    draw.text(position, text, font=font, fill=(88, 68, 34))

    rotated_txt = txt.rotate(4, expand=True) 


    image.paste(rotated_txt, (0, 0), rotated_txt)

    image.save("assets/cache.png")

