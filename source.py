import pygame

pygame.init()

w = 245
h = 368

drawing_window = pygame.display.set_mode((w, h))

source_image = pygame.image.load("baconater.png").convert()

drawing_window.blit(source_image, (0, 0))

# by request, the ASCII art will also appear in an external file

external_file = open("ascii_art_result.txt", "w")

for y in range(h):
	for x in range(w):
		(r, g, b, _) = drawing_window.get_at((x, y))
		luminance = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255
		if luminance > 0.875:
			next_character = "@"
		elif luminance > 0.750:
			next_character = "#"
		elif luminance > 0.625:
			next_character = "*"
		elif luminance > 0.500:
			next_character = "+"
		elif luminance > 0.375:
			next_character = "="
		elif luminance > 0.250:
			next_character = "-"
		elif luminance > 0.125:
			next_character = ":"
		else:
			next_character = "."
		print(next_character, end="")
		print(next_character, file=external_file, end="")
	print()
	print(file=external_file)

external_file.close()

# this little postcondition loop is actually used to keep the window open until the user closes it
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
