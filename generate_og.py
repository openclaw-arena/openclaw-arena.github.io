from PIL import Image, ImageDraw, ImageFont
import os

img = Image.new('RGB', (1200, 630), color=(13, 17, 23))
draw = ImageDraw.Draw(img)

# Try to use system font
try:
    title_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 64)
    sub_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 32)
    emoji_font = ImageFont.truetype("/System/Library/Fonts/Apple Color Emoji.ttc", 100)
except:
    title_font = ImageFont.load_default()
    sub_font = ImageFont.load_default()
    emoji_font = title_font

# Title
draw.text((600, 220), "OpenClaw Arena", fill=(230, 237, 243), font=title_font, anchor="mm")
# Subtitle
draw.text((600, 300), "Personal AI Agent Benchmark", fill=(88, 166, 255), font=sub_font, anchor="mm")
# Stats
draw.text((600, 370), "13 Models · 40 Tasks · 710 Evaluations", fill=(139, 148, 158), font=sub_font, anchor="mm")
# Attribution
draw.text((600, 440), "CUHK VNLab", fill=(139, 148, 158), font=sub_font, anchor="mm")

img.save('og-image.png')
print("OK")
