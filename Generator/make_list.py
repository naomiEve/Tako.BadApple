from PIL import Image
from time import sleep
from bitarray import bitarray
import os

output = "private static readonly List<byte[]> _frames = new (){"

def print_frame(image):
	global output
	frame = image.load()
	a = bitarray()
	for y in range(im.size[1]):
		for x in range(im.size[0]):
			if frame[x, y] == 0:
				a.append(0)
				continue

			r, g, b = frame[x, y]
			luma = r + g + b
			if luma < 300:
				a.append(0)
			else:
				a.append(1)
	a = str(list(a.tobytes()))
	output += f"""
	{a.replace("]", "}").replace("[", "new byte[] {")},"""

with Image.open("badapple.gif") as im:
	try:
		while True:
			print_frame(im)
			im.seek(im.tell() + 1)

	except EOFError:
		output += "\n};"
		pass

	open("apple.cs", "w").write(output)