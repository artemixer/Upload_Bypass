#!/usr/bin/env python3

from .ansi_colors import *
from lib.file_upload import get_terminal_size


# Print all modules
def list_all_modules():
    
    print("\033c", end="")

    # \033[1m is for a bold text
    # \033[0m for a reset
    # \033[1m\033[4m is for a bold and underline text

    terminal_width = get_terminal_size()
    print("_" * terminal_width)
    print(f"\033[1m\nextension_shuffle\033[0m:\n\nDifferent extensions allowed by the back-end engine (ex: php3,php3,phar).")
    print("_" * terminal_width)
    print(f"\033[1m\ndouble_extension\033[0m:\n\nDoubling the back-end extensions (ex: filename.php.php).")
    print("_" * terminal_width)
    print(f"\033[1m\nforward_double_extension\033[0m:\n\nAllowed extension concatenated with the back-end extension (ex: filename.jpeg.php).")
    print("_" * terminal_width)
    print(f"\033[1m\nreverse_double_extension\033[0m:\n\nBack-end extension concatenated with the allowed extension (ex: filename.php.jpeg).\n{red}\033[1mWarning\033[0m{reset} - it might result with a false-positive!")
    print("_" * terminal_width)
    print(f"\033[1m\nnull_byte_cutoff\033[0m:\n\nAdding null bytes which ultimately should cut the rest of the extension (ex: filename.php%00.jpeg the result will be filename.php).\n{red}\033[1mWarning\033[0m{reset} - it might result with a false-positive!")
    print("_" * terminal_width)
    print(f"\033[1m\nname_overflow_cutoff\033[0m:\n\nOverflowing the exceeding limit to cut the allowed extension (ex: Linux limit is 255 chars, A*251.php.jpeg = A*255.php - total 255 chars).")
    print("_" * terminal_width)
    print(f"\033[1m\nhtaccess_overwrite\033[0m:\n\nOver-writing the .htaccess rules to allow arbitrary file extension in the current directory and its sub-directories.")
    print("_" * terminal_width)
    print(f"\033[1m\nsvg_xxe\033[0m:\n\nUploading SVG with XML-External-Entity that reads the passwd file system.")
    print("_" * terminal_width)
    print(f"\033[1m\nsvg_xss\033[0m:\n\nUploading SVG with Cross-Site Scripting that executes an alert popup.")
    print("_" * terminal_width)
    exit(1)
