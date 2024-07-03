# QR Code Generator

This repository contains a simple Python script to generate a QR code from a URL.

## Prerequisites

Make sure you have Python installed on your system. You will also need to install the required libraries.

## Installation

First, clone this repository to your local machine:

```bash
git clone https://github.com/haikal-dev/python-qrcode-generator.git
cd qrcode-generator
```

Next, install the required Python libraries:

```bash
pip install qrcode
pip install pillow
```

## Usage

You can generate a QR code by running the script with the URL as a command-line argument. You can also specify the output file name using the --output option.

```bash
python generate_qr.py <url> [--output <output_file>]
```

## Examples

Generate a QR code for https://example.com and save it as qrcode.png (default):

```bash
python generate_qr.py https://example.com
```

## License

This project is licensed under the MIT License
