"""
Author: 蛇道
2023
GPL
"""


from ascii_design.ascii_design import AsciiArtConverter
import os


def ascii_design(input_path,output_path,reduction_ratio):
    try:
        converter = AsciiArtConverter()
        # Define the input and output path of the files
        input_path = input_path
        output_path = output_path
        # Define the reduction ratio of the image
        width_ratio = reduction_ratio
        height_ratio = reduction_ratio
        # Convert and save the images
        converter.convert_and_save(input_path, output_path, width_ratio, height_ratio)
    except Exception as error:
        print("An error occurred by def ascii_design() :", error)


def set_path(max_tries=3):
    tries = 0
    while True:
        try:
            path = input("Enter input path of your images folder.\n>>> ")
            if os.path.isdir(path):
                print(f"The path you entered is: {path}")
                confirm = input("Is this correct? [Y/n]\n>>> ")
                if confirm.lower() in ['y', 'yes', '']:
                    return path
            else:
                print("\nIs not a valid directory.")
            tries += 1
            if tries == max_tries:
                print(f"You have reached the maximum number of tries ({max_tries}).")
                return None
        except Exception as error:
            print("An error occurred by def set_path() :", error)


def home():
    banner = """
                   _  _             _             _               
  __ _  ___   ___ (_)(_)         __| |  ___  ___ (_)  __ _  _ __  
 / _` |/ __| / __|| || |        / _` | / _ \/ __|| | / _` || '_ \ 
| (_| |\__ \| (__ | || |       | (_| ||  __/\__ \| || (_| || | | |
 \__,_||___/ \___||_||_| _____  \__,_| \___||___/|_| \__, ||_| |_|
                        |_____|                      |___/        
    """

    instructions = """
    ---------------------- Instructions ----------------------
    - Select the input path of the images folder. (for example, >>> /home/gnu/ascii-art/input_images)
    - Define the reduction ratio of the image (for example, >>> 9)
    ----------------------------------------------------------"""
    print(banner)
    print(instructions)


def main():
    try: 
        home()
        input_path = set_path()
        #input_path = "./input_images"
        output_path = "./output_images"
        reduction_ratio  = int(input("Define reduction ratio.\n>>> "))
        ascii_design(input_path,output_path,reduction_ratio)
    except Exception as error:
        print("An error occurred by def main() :", error)


if __name__ == '__main__':
    main()