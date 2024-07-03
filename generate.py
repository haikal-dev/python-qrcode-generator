#!/usr/bin/env python3

import qrcode
import argparse

def generate_qr(url, output_file="qrcode.png"):
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the image file
    img.save(output_file)

    print(f"QR code generated and saved as {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a QR code from a URL.')
    parser.add_argument('url', type=str, help='The URL to encode in the QR code.')
    parser.add_argument('--output', type=str, default='qrcode.png', help='The output file name (default: qrcode.png).')

    args = parser.parse_args()

    generate_qr(args.url, args.output)
