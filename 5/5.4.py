import PIL.Image as Image


colors = Image.open("./hamburg_outline.png").getcolors(maxcolors=1000)
colors.sort(key=lambda x: x[0], reverse=True)
print(colors[:5])
# not ideal but eh


green = colors[1][0]
red = colors[2][0]

graphic = (green - red) / red

data = (0.4837 - 0.5163) / 0.5163
print(graphic, data)
lie_factor = graphic / data

print(lie_factor)