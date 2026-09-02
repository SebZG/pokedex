# Pokedex Image Converter

This script converts JPG/JPEG images from one folder into PNG files in another folder.

## What it does

The program:
- checks that the source folder exists
- verifies that the source path is a directory
- creates the destination folder if it does not exist
- opens each image in the source folder
- saves a PNG copy in the destination folder using the same filename (without the original extension)
- prints a completion message when done

## Requirements

Install the Pillow library:

```bash
pip3 install Pillow
```

## Usage

```bash
python3 JPGtoPNGconverter.py SOURCE_FOLDER DESTINATION_FOLDER
```

Example:

```bash
python3 JPGtoPNGconverter.py POKEDEX/ NEW/
```

### Parameters
- `SOURCE_FOLDER`: folder containing the JPG files to convert
- `DESTINATION_FOLDER`: folder where the PNG files will be saved

If `DESTINATION_FOLDER` does not exist, the script will create it automatically.

## Notes

- The script converts each file using its original base name, so `pikachu.jpg` becomes `pikachu.png`.
- The source folder must be a real directory.
- The script tries to process each file individually and prints an error if one image fails to open or save.

## Example

If your source folder contains:

```text
POKEDEX/
  001.jpg
  002.jpg
  003.jpeg
```

Running:

```bash
python3 JPGtoPNGconverter.py POKEDEX/ NEW/
```

will create:

```text
NEW/
  001.png
  002.png
  003.png
```

## Troubleshooting

- If you see `Error: Source directory '...' does not exist.`, check the folder path.
- If you see `Error: '...' is not a directory.`, make sure you passed a folder, not a file.
- If a file fails to convert, the script will print the error for that image but continue with the rest.
