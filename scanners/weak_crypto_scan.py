import os

def scan_weak_crypto(extracted_dir):

    print("[+] Scanning for weak cryptography...")

    keywords = [
        b"md5",
        b"des",
        b"base64",
        b"sha1"
    ]

    for root, dirs, files in os.walk(extracted_dir):

        for file in files:

            filepath = os.path.join(root, file)

            try:
                with open(filepath, "rb") as f:

                    data = f.read().lower()

                    for keyword in keywords:

                        if keyword in data:

                            print("[!] Weak crypto keyword found:", keyword.decode(), "->", filepath)

            except:
                pass
