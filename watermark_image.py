from PIL import Image, ImageDraw, ImageFont

def watermark_img(path):
    #Opening Image
    img = Image.open(path + "/"+"img.jpg") 

    draw = ImageDraw.Draw(img) 

    text = "Shreyash Mhashilkar"
    font = ImageFont.truetype('arial.ttf', 400)

    textwidth, textheight = draw.textsize(text, font)
    width, height = img.size 
    x=width/2-textwidth/2
    y=height-textheight-300

    draw.text((x, y), text, font=font) 

    #Saving the new image
    img.save(path +"\\"+"watermark_img.jpg")

if __name__=="__main__":
    path = r"" #add path of image that need to be watermark
    watermark_img(path)