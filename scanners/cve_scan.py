import os

def scan_cve(extracted_dir):

    print("[+] Checking for known CVEs...")

    cve_database = {
        b"busybox": "CVE-2011-5325",
        b"dropbear": "CVE-2016-7407",
        b"openssl": "CVE-2014-0160 (Heartbleed)"
    }

    for root, dirs, files in os.walk(extracted_dir):

        for file in files:

            filepath = os.path.join(root, file)

            try:
                with open(filepath, "rb") as f:

                    data = f.read().lower()

                    for keyword, cve in cve_database.items():

                        if keyword in data:

                            print("[!] {} detected → Possible vulnerability: {}".format(keyword.decode(), cve))

            except:
                pass
