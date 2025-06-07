from PIL import Image, ImageSequence

def remove_exact_black_background_gif(input_path, output_path):
    original = Image.open(input_path)
    frames = []

    for frame in ImageSequence.Iterator(original):
        rgba = frame.convert("RGBA")
        pixels = rgba.load()

        for y in range(rgba.height):
            for x in range(rgba.width):
                r, g, b, a = pixels[x, y]
                if (r, g, b) == (0, 0, 0):  # Exactly #000000
                    pixels[x, y] = (0, 0, 0, 0)  # Transparent

        frames.append(rgba)

    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        loop=0,
        duration=original.info.get("duration", 100),
        disposal=2
    )

# Usage
remove_exact_black_background_gif("helpy.gif", "helpy_nobg.gif")
