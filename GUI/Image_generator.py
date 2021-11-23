from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', size=(400,120), color=(0,0,0))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype("ARIAL.woff", 60)
font1 = ImageFont.truetype("ARIAL.woff", 70)

draw.rectangle(([(15,15),(385,105)]), fill=(255,255,255))

draw.text((30, 30),"Maze",(255,0,0),font=font)
draw.text((180, 25),"Solver",(0,255,0),font=font1)

img.show()
img.save('logo.png')
