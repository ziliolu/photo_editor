# Image Editing Script

<p align="center">
  <img src="https://img.shields.io/github/languages/top/ziliolu/photo_editor?color=#FFFFFF&style=flat-square" />
  <img src="https://img.shields.io/badge/status-finished-success?color=#FFFFFF&style=flat-square" />
  <img src="https://img.shields.io/github/last-commit/ziliolu/photo_editor?color=#FFFFFF&style=flat-square" />
</p>
This is a simple Python script that processes images from a specified directory, applies a grayscale filter, enhances contrast, and saves the edited images to an output directory.
<p align="center">
  <img src="https://github.com/ziliolu/photo_editor/blob/main/info/before_after.jpg" width="500" />
</p>

## Prerequisites

- Python 3.x
- Pillow library (`pip install Pillow`)

## Usage

1. Place the images you want to edit in the `imgs` directory.
2. Run the script (`python script_name.py`).
3. Edited images will be saved in the `edited_imgs` directory.

## Script Explanation

The script performs the following steps:

1. Imports required modules:

   - `PIL.Image`: Image processing functionalities.
   - `PIL.ImageEnhance`: Image enhancement utilities.
   - `PIL.ImageFilter`: Image filter effects.
   - `os`: Operating system interaction.

2. Defines input and output paths:

   - `path`: The directory containing input images.
   - `path_out`: The directory to save edited images.

3. Loops through each file in the input directory:

   - Opens the image using `PIL.Image.open`.
   - Converts the image to grayscale using `.convert("L")`.
   - Enhances contrast using `ImageEnhance.Contrast`.
   - Saves the edited image to the output directory with the original name plus "_edited".

## Notes

- The script currently enhances contrast by a factor of 1, which doesn't significantly alter the image.
- You can adjust the enhancement factor in the script as needed for your desired effect.

Feel free to modify the script to add more features or customize the editing process to suit your requirements.

