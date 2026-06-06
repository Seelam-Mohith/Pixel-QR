# Pixel-QR

Pixel-QR is a lightweight Flask-based web application that allows users to generate and download QR codes instantly. The application converts any URL or text input into a high-quality QR code image that can be viewed and downloaded directly from the browser.

## Overview

Pixel-QR provides a simple and efficient solution for creating QR codes without requiring external services. Users can generate QR codes for websites, social media profiles, documents, or any text-based content through an intuitive web interface.

The application also includes basic visitor IP logging functionality for monitoring website traffic.

## Features

* Generate QR codes from URLs or text
* High error-correction support for reliable scanning
* Instant QR code preview
* Download generated QR codes as PNG images
* Session-based QR code storage
* Visitor IP detection and logging
* Responsive web interface

## Technology Stack

### Backend

* Flask
* Python

### Libraries

* qrcode[pil]
* Pillow (PIL)

### Frontend

* HTML
* CSS
* Jinja2 Templates

## Project Structure

```text
Pixel-QR/
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/Seelam-Mohith/Pixel-QR.git
cd Pixel-QR
```

### Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

or install manually:

```bash
pip install Flask qrcode[pil] Pillow
```

## Running the Application

Start the Flask server:

```bash
python app.py
```

The application will be available at:

```text
http://localhost:10000
```

or the port specified in the `PORT` environment variable.

## Usage

1. Open the application in your browser.
2. Enter a URL or text.
3. Generate the QR code.
4. Preview the generated QR code.
5. Download the QR code as a PNG image.


## Future Enhancements

* Custom QR code colors
* Logo embedding inside QR codes
* QR code history
* User authentication
* Multiple image formats (PNG, JPG, SVG)
* Analytics dashboard

## Author

**Seelam Mohith**

GitHub: https://github.com/Seelam-Mohith

