import os

def scan_passwords(extracted_dir):

    print("正在检测硬编码密码...")

    keywords = ["password=", "passwd=", "admin:admin", "root:root", "123456"]

    for root, dirs, files in os.walk(extracted_dir):

        for file in files:

            filepath = os.path.join(root, file)

            try:
                with open(filepath, "rb") as f:
                    data = f.read().lower()

                    for keyword in keywords:
                        if keyword.encode() in data:
                            print("[!] 发现可能的硬编码密码:", keyword, "->", filepath)

            except:
                pass
