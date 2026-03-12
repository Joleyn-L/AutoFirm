import os

def scan_passwd(extracted_dir):

    passwd_file = extracted_dir + "/etc/passwd"

    print("正在检测默认账户...")

    if os.path.exists(passwd_file):

        with open(passwd_file, "r") as f:
            content = f.read()

        if "root:" in content:
            print("[!] 发现 root 账户")
        else:
            print("[+] 未发现默认账户")

    else:
        print("[+] 未找到 passwd 文件")
