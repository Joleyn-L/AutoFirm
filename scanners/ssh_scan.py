import os

def scan_ssh(extracted_dir):

    print("正在检测SSH服务...")

    result = os.popen("grep -r dropbear " + extracted_dir).read()

    if result:
        print("[!] 发现 Dropbear SSH 服务")
    else:
        print("[+] 未发现 SSH")
