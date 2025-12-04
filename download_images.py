#!/usr/bin/env python3
"""
Image Downloader for IConSCEPT 2025 Welcome Video

The Google Sites images require browser-based downloading due to CORS/referrer restrictions.
This script provides the URLs and filenames for manual download.

Option 1: Manual Download
-------------------------
Open each URL below in your browser and save to the 'images' folder with the given filename.

Option 2: Use Selenium (automated)
----------------------------------
Install selenium and a webdriver, then run this script with --selenium flag.
"""

import os
from pathlib import Path

IMAGES_DIR = Path(__file__).parent / "images"
IMAGES_DIR.mkdir(exist_ok=True)

# Image URLs and their local filenames
IMAGES = {
    "banner.jpg": {
        "url": "https://lh3.googleusercontent.com/sitesv/AAzXCkcLaOjkAxcVHl78uoY5nRB9019OBvG6CcC71ko7EFs9o1zTXGP9J8HjHQVm86LCg4rsPxg4OUGGRNoGuMPbdW33UF_sx6a4WLTKrfbgJB818ND3eU9C-zzuC4YI4_On9g1Gx0FsRtia1kmaxUiC1vvjuDQwk0JLp159OCDbtgVpAOPNVAH6xZPv9XE=w1280",
        "desc": "IConSCEPT 2025 Conference Banner"
    },
    "nit-logo.png": {
        "url": "https://lh3.googleusercontent.com/sitesv/AAzXCkeFVup809jXqFPcssGV8f7iEJbxQbUIA8mSHl5HRzrWJCT5q4372z04i-bu5tGknFUEvcTrhWxQaU50kWHr5vLIW0CbqH1g1_O_GFsJexNUP5X2HK1BmBdNFgWkzObCLsfn0itlVgg20wY9cdVTYiv58arDPfzBO7OQon_-bZjTXbbrkkc5IpmN8N0O_OiDd1s2NOfBHwkNrCkj_iZT3j6TAWAUJNwf9ity=w1280",
        "desc": "NIT Puducherry Logo"
    },
    "ieee-logo.png": {
        "url": "https://lh3.googleusercontent.com/sitesv/AAzXCkcx3tfon9aXXZDrLd2f9SK1YObCLRfFsIow-EiIYvX1syTMZlStcMEQLY-UbK6q-AwIMeb_AnfQcmbz8TbFMa5oJnB500gQqxFDKqkvu94zX1tFlth_1Og7LZe7cnt3A__qib-aHsFNbUgpJAddAh3We_MYb3OGfavasP_C2z_lVTO8J8DtXrZ6t53UQjvsKJ-en7S7V3KcQhOIcVlHqPGYvhMOd8ibwGmtNGo=w1280",
        "desc": "IEEE Madras Section Logo"
    },
    "campus.jpg": {
        "url": "https://lh3.googleusercontent.com/sitesv/AAzXCkf5yMf15cuWVtY-3wLQftl6E0ozHrO2RH8TX9J6FyJShffcWLfYQ5tXvmbPEiCpFkvbT9RFAVnjDwu59LsDrl-NGmEtkt0ePmQfOenfLhQH5fInXPS_cNFJGaGvOzdoWgR0OAlNjEASzkBP82RowYoSWVFv3ubtEJQv3el0K1IiS2cCbscqbfyWVEDXfDLUfceW14M0jDz_C7bN0kIfVtSmzGMIaTV4i84q=w1280",
        "desc": "NIT Puducherry Campus Photo"
    },
    "speaker-frery.jpg": {
        "url": "https://lh3.googleusercontent.com/sitesv/AAzXCkdevUPGrOsIjzDnZdjrZdSInqhdkWiFvR9QXD5Tk3zZLUN_ZkBtPHwAmTkxwHQhSuFR3zKMwwsxRBy-espBHO_CdTApgPZiLnsbwOz5XUCMVWxhqv0Er4crAXhqULyC0zzQWQcAoD1TSUt9UWEZTS95gvS-aVT9kG0OSpzMK5RK7NNdgSA_25uJamD0FiEa8itWgFKjPHw0dMjpmBKmiM4Y5Yv5Yl8CfFLu=w1280",
        "desc": "Prof. Alejandro Frery (New Zealand)"
    },
    "speaker-sangaiah.jpg": {
        "url": "https://lh3.googleusercontent.com/sitesv/AAzXCkct4oik-A7cHDxSBkTHBcq0Yj37ldoea_mpMzA3f8k7zCm2xISzk-gl6EnE4dMJrAVH3MzsEOhfr9BnxoAsPZeZQW1qfglSrBIkmGs0fLN-zlhVoWklzYmozWqnHfJKE82C6kfa0ovoJ_-lN9GjwXGkITIWEdijWNWDhEhXdbVkqCyPJ2U7ATeBpJv8fq6gpoBBZGTGQTc0JlSYNnrtAVKQnW_c00c3Fo95=w1280",
        "desc": "Dr. Arun Kumar Sangaiah (Taiwan)"
    },
    "speaker-tripathi.jpg": {
        "url": "https://lh3.googleusercontent.com/sitesv/AAzXCkcgOFtEwJaS7gAtfopR4FNTEPU60Wcxf343fyjFhrds1ELY5JUvGaCOfw9dOj21HQEfoA6mdFtn5u6unVfRbb5e_1XdHalh4eOYnpeDj8LkbbEsySosZYDmc3B8C-jlrXgI-1X25OVWNK7vVah5-xHAVh0BIN8uj9VBD-iuG1LRQtlHMFkbWWZwyVs1MH039GOD2tWMwbhJDgSR5bt9CA0qKQTjwnoFfJkORu8=w1280",
        "desc": "Dr. Ravi Nath Tripathi (Japan)"
    },
    "speaker-ghosh.jpg": {
        "url": "https://lh3.googleusercontent.com/sitesv/AAzXCkdY8MMPuMK7g6f__7R47Vq6xxaYqQzFWmBN1RJju5xluvDp23ZJx1RsRfEAduhScjtFxTcy7W2sOl0bdCszP_sxsWDQk19RscGQ4q5FH7s58qohGJZBdKDNISdgkhTWX55kYWaNJQYbsMuwKrDcrsxNIzMjiVFdNSlpe3NHULrcGgHZTchVnepazK4g-6QfjlDDNzO3UKGrFLpHrHZTFIlsXdyYsXQr12Ef9po=w1280",
        "desc": "Prof. Bratin Ghosh (India)"
    }
}


def print_manual_instructions():
    """Print instructions for manual download."""
    print("=" * 70)
    print("IConSCEPT 2025 - Image Download Instructions")
    print("=" * 70)
    print(f"\nSave all images to: {IMAGES_DIR}\n")
    print("-" * 70)

    for filename, info in IMAGES.items():
        print(f"\n{info['desc']}")
        print(f"  Filename: {filename}")
        print(f"  URL: {info['url']}")

    print("\n" + "-" * 70)
    print("\nInstructions:")
    print("1. Open each URL in your browser")
    print("2. Right-click the image and select 'Save Image As...'")
    print(f"3. Save to: {IMAGES_DIR}")
    print("4. Use the exact filename shown above")
    print("\n" + "=" * 70)


def download_with_selenium():
    """Download images using Selenium (requires installation)."""
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        import base64
        import time

        print("Starting Selenium download...")

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        driver = webdriver.Chrome(options=options)

        for filename, info in IMAGES.items():
            try:
                print(f"Downloading {filename}...")
                driver.get(info['url'])
                time.sleep(2)

                # Get image as base64
                canvas = driver.execute_script("""
                    var img = document.querySelector('img') || document.body;
                    var canvas = document.createElement('canvas');
                    canvas.width = img.naturalWidth || img.offsetWidth;
                    canvas.height = img.naturalHeight || img.offsetHeight;
                    var ctx = canvas.getContext('2d');
                    ctx.drawImage(img, 0, 0);
                    return canvas.toDataURL('image/png').substring(22);
                """)

                if canvas:
                    filepath = IMAGES_DIR / filename
                    with open(filepath, 'wb') as f:
                        f.write(base64.b64decode(canvas))
                    print(f"  Saved: {filepath}")

            except Exception as e:
                print(f"  Failed: {e}")

        driver.quit()
        print("\nDownload complete!")

    except ImportError:
        print("Selenium not installed. Run: pip install selenium")
        print("Also requires Chrome/ChromeDriver installed.")
        print_manual_instructions()


if __name__ == "__main__":
    import sys

    if "--selenium" in sys.argv:
        download_with_selenium()
    else:
        print_manual_instructions()
