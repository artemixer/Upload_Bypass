#!/usr/bin/env python3

import os
from .alerts import *
from urllib.parse import urlparse
from .config import magic_bytes


def results(url, file_name, content_type, upload_location, magic_byte, output_folder, allowed_extension, current_time):
    domain = get_domain_name(url)

    if not output_folder:
        if not os.path.exists(f'{os.getcwd()}/{domain}'):
            os.system(f'mkdir {os.getcwd()}/{domain}')

        # Save the results to results.txt
        f = open(f"{os.getcwd()}/{domain}/results.txt", "a")
        success(f"Results saved in {os.getcwd()}/{domain}/results.txt")

    else:
        f = open(output_folder, "a")

    if not magic_byte:
        f.write("-------------------------------------------------------------------------------------------\n")
        f.write(
            f"File uploaded successfully with Extension: {file_name}\nContent-Type: {content_type}\nUpload Location: {upload_location}\nDate & Time: {current_time}\n")
        f.close()
    else:
        f.write("-------------------------------------------------------------------------------------------\n")
        f.write(
            f"File uploaded successfully with Extension: {file_name}\nContent-Type: {content_type}\nUpload Location: {upload_location}\nMagic Bytes: {magic_bytes[allowed_extension]}\nDate & Time: {current_time}\n\n")
        f.close()


def get_domain_name(url):
    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc
    return domain_name
