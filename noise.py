from perlin_noise import PerlinNoise
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640, 480))

if __name__ == '__main__':
	octaves = 1
	seed = 0
	frequency = 0

	opts = sys.argv
	for opt in opts:
		if opt == '--octaves':
			octaves = int(opts[opts.index(opt)+1])

		if opt == '--seed':
			seed = int(opts[opts.index(opt)+1])

		if opt == '--frequency':
			frequency = float(opts[opts.index(opt)+1])

	height_map = []

	noise = PerlinNoise(octaves, seed)

	for x in range(0, 640, 10):
		for y in range(0, 480, 10):
			n = noise.noise([x * frequency, y * frequency])
			print(n * 255)
			height_map.append({
				'rect': pygame.rect.Rect(x, y, 10, 10),
				'color': [abs(n * 255) for _ in range(0, 3)],
			})

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		for i, value in enumerate(height_map):
			rect = value['rect']
			color = value['color']
			pygame.draw.rect(screen, color, rect)

		pygame.display.flip()