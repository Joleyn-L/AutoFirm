import sys
import os

def banner():

    print("""
     ___        __        ______
    / _ | ___  / /_____ _/ __/ /  ___  ____
   / __ |/ _ \/  '_/ _ `/ _// _ \/ _ \/ __/
  /_/ |_/_//_/_/\_\\_,_/___/_//_/\___/_/

      AutoFirm - IoT Firmware Security Scanner
    """)

def generate_html_report(firmware, extracted):

    html_content = f"""
    <html>
    <head>
        <title>AutoFirm Scan Report</title>
        <style>
            body {{ font-family: Arial; background-color:#f5f5f5; }}
            h1 {{ color:#333; }}
            .box {{ background:white; padding:20px; margin:20px; border-radius:8px; }}
        </style>
    </head>

    <body>

    <h1>AutoFirm Firmware Security Report</h1>

    <div class="box">
    <h2>Firmware Information</h2>
    <p><b>Firmware File:</b> {firmware}</p>
    <p><b>Extracted Directory:</b> {extracted}</p>
    </div>

    <div class="box">
    <h2>Scan Modules</h2>
    <ul>
    <li>Firmware Info Detection</li>
    <li>Default Account Detection</li>
    <li>Telnet Detection</li>
    <li>SSH Detection</li>
    <li>Hardcoded Password Detection</li>
    <li>Web Backdoor Detection</li>
    <li>Weak Crypto Detection</li>
    <li>CVE Matching</li>
    </ul>
    </div>

    </body>
    </html>
    """

    with open("report.html","w") as f:
        f.write(html_content)

    print("[+] HTML报告生成: report.html")
from scanners.passwd_scan import scan_passwd
from scanners.telnet_scan import scan_telnet
from scanners.ssh_scan import scan_ssh
from scanners.password_scan import scan_passwords
from scanners.web_backdoor_scan import scan_web_backdoor
from scanners.weak_crypto_scan import scan_weak_crypto
from scanners.firmware_info_scan import scan_firmware_info
from scanners.cve_scan import scan_cve

def scan_firmware(extracted_dir):

    print("[+] 开始扫描固件文件系统...")

    keywords = ["telnet", "password", "admin", "root", "ssh"]

    for root, dirs, files in os.walk(extracted_dir):

        for file in files:

            filepath = os.path.join(root, file)

            try:
                with open(filepath, "rb") as f:
                    data = f.read().lower()

                    for keyword in keywords:
                        if keyword.encode() in data:
                            print("[!] 发现关键字:", keyword, "->", filepath)

            except:
                pass


def find_extracted_dir():
    for item in os.listdir():
        if item.endswith(".extracted"):
            return item
    return None


def main():
   
    banner()

    if len(sys.argv) < 2:
        print("Usage: python3 autofirm.py firmware.bin [--scan all|ssh|telnet|passwd|password]")
        sys.exit()

    firmware = sys.argv[1]

    scan_type = "all"

    if len(sys.argv) >= 4 and sys.argv[2] == "--scan":
        scan_type = sys.argv[3]

    print("AutoFirm IoT 固件安全检测工具")
    print("开始分析固件:", firmware)

    os.system("binwalk -e " + firmware)

    extracted = find_extracted_dir()

    if extracted:

        print("[+] 找到解压目录:", extracted)
        report_file = open("report.txt", "w")
        report_file.write("AutoFirm Scan Report\n")
        report_file.write("====================\n")
        report_file.write("Firmware: " + firmware + "\n")
        report_file.write("Extracted Dir: " + extracted + "\n\n")
        
        if scan_type == "all" or scan_type == "passwd":
            scan_firmware_info(extracted)
            scan_passwd(extracted)

        if scan_type == "all" or scan_type == "telnet":
            scan_telnet(extracted)

        if scan_type == "all" or scan_type == "ssh":
            scan_ssh(extracted)

        if scan_type == "all":
            scan_firmware(extracted)
            scan_web_backdoor(extracted)
            scan_weak_crypto(extracted)
            scan_cve(extracted)
        if scan_type == "all" or scan_type == "password":
            scan_passwords(extracted)

        report_file.write("Scan finished.\n")
        report_file.close()

        print("\n[+] 扫描完成，报告已生成: report.txt")
        generate_html_report(firmware, extracted)
    else:
        print("[!] 未找到解压目录")
    
if __name__ == "__main__":
    main()
