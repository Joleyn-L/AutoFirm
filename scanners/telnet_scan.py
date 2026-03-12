import os

def scan_telnet(extracted_dir):

    print("正在检测Telnet服务...")

    result = os.popen("grep -r telnet " + extracted_dir).read()

    if result:
        print("[!] 发现 Telnet 服务")
    else:
        print("[+] 未发现 Telnet")
