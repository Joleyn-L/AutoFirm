# AutoFirm

AutoFirm is a lightweight IoT firmware security scanner designed for analyzing embedded device firmware and discovering potential security issues.

## Features

- Firmware extraction using Binwalk
- Firmware information detection
- Default account detection
- Telnet / SSH detection
- Hardcoded password scanning
- Web backdoor detection
- Weak cryptography detection
- CVE vulnerability matching
- HTML scan report generation
## Usage

```bash
python3 autofirm.py examples/test.bin
## Requirements

Before running AutoFirm, make sure the following dependencies are installed:

- Python 3.x
- Binwalk

Install Python dependencies:
pip install -r requirements.txt


Install Binwalk (Linux):


sudo apt install binwalk


## Installation

Clone the repository:


git clone https://github.com/yourusername/AutoFirm.git

cd AutoFirm
Install required packages:


pip install -r requirements.txt


## Usage

### Scan a firmware


python3 autofirm.py firmware.bin


The tool will automatically:

1. Extract the firmware using Binwalk
2. Locate the extracted filesystem
3. Run security scanning modules

### Scan a specific module

Scan only SSH service:


python3 autofirm.py firmware.bin --scan ssh


Scan only Telnet service:


python3 autofirm.py firmware.bin --scan telnet


Scan only default accounts:


python3 autofirm.py firmware.bin --scan passwd


Scan hardcoded passwords:


python3 autofirm.py firmware.bin --scan password


Scan all modules:


python3 autofirm.py firmware.bin --scan all


## Example

Run AutoFirm with the example firmware:


python3 autofirm.py examples/test.bin


Example output:


AutoFirm IoT Firmware Security Scanner
Analyzing firmware: test.bin

[+] Extracted firmware directory found
[!] Telnet service detected
[!] Default account detected: root
[!] Hardcoded password found


## Project Structure

AutoFirm
│
├── autofirm.py
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
│
├── examples
│   └── test.bin
│
└── scanners
    ├── passwd_scan.py
    ├── telnet_scan.py
    ├── ssh_scan.py
    ├── password_scan.py
    ├── web_backdoor_scan.py
    ├── weak_crypto_scan.py
    ├── firmware_info_scan.py
    └── cve_scan.py

## Description

AutoFirm is a simple firmware security analysis tool built for learning and experimenting with IoT firmware analysis techniques.  
It helps identify common security issues in extracted firmware filesystems.

## License

This project is licensed under the MIT License.
A simple IoT firmware security analysis tool for detecting weak passwords, backdoors and insecure services.
