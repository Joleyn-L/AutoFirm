import os

def scan_web_backdoor(extracted_dir):

    print("[+] Scanning for potential web backdoors...")

    keywords = [
        b"system(",
        b"popen(",
        b"exec(",
        b"/cgi-bin/",
        b"shell_exec",
        b"cmd="
    ]

    for root, dirs, files in os.walk(extracted_dir):

        for file in files:

            filepath = os.path.join(root, file)

            try:
                with open(filepath, "rb") as f:

                    data = f.read()

                    for keyword in keywords:

                        if keyword in data:

                            print("[!] Suspicious keyword found:", keyword.decode(), "->", filepath)

            except:
                pass
