"""
Author: 蛇道
2023
GPL
"""


from PIL import Image, ImageDraw, ImageFont
import os


ASCII_CHARS = [' ', '.', ':', ';', ',', '*', 'o', '8', '#', '&', '%', '@', '$', '=', '+', '^']

class AsciiArtConverter:
    def __init__(self):
        self.ASCII_CHARS_LEN = len(ASCII_CHARS)
        self.FONT_SIZE = 10
        self.FONT = ImageFont.truetype("./resources/Arial.ttf", self.FONT_SIZE)

    def convert_image_to_ascii(self, image, width_ratio, height_ratio):
        width, height = image.size
        new_width, new_height = int(width / width_ratio), int(height / height_ratio)
        image = image.resize((new_width, new_height))
        pixels = image.load()
        ascii_image = []
        for y in range(image.size[1]):
            row = []
            for x in range(image.size[0]):
                pixel = pixels[x, y]
                brightness = int(sum(pixel) / 3)
                ascii_char = ASCII_CHARS[min(brightness * self.ASCII_CHARS_LEN // 255, self.ASCII_CHARS_LEN - 1)]
                row.append(ascii_char)
            ascii_image.append(row)
        return ascii_image

    def save_ascii_image(self, ascii_image, file_name):
        ascii_image_height = len(ascii_image)
        ascii_image_width = len(ascii_image[0])
        image = Image.new("RGBA", (ascii_image_width * self.FONT_SIZE, ascii_image_height * self.FONT_SIZE), (0, 0, 0, 255))
        draw = ImageDraw.Draw(image)
        for y, row in enumerate(ascii_image):
            for x, char in enumerate(row):
                draw.text((x * self.FONT_SIZE, y * self.FONT_SIZE), char, font=self.FONT, fill=(255, 255, 255, 255))
        image.save(file_name)

    def convert_and_save(self, input_path, output_path, width_ratio, height_ratio):
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        extensions = [".jpg", ".jpeg", ".png"]
        for file in os.listdir(input_path):
            for ext in extensions:
                if file.endswith(ext):
                    input_file = os.path.join(input_path, file)
                    output_file = os.path.join(output_path, os.path.splitext(file)[0] + ".png")

                    img = Image.open(input_file)
                    ascii_image = self.convert_image_to_ascii(img, width_ratio, height_ratio)
                    self.save_ascii_image(ascii_image, output_file)

                    print(f"File converted and saved to: {output_file}")
