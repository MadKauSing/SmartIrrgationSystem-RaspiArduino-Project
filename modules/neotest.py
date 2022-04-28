import board
import neopixel
pixels = neopixel.NeoPixel(board.D12, 30)

while True:
    pixels.fill((0, 255, 0))

