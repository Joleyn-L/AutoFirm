import os

def scan_firmware_info(extracted_dir):

    print("[+] Detecting firmware information...")

    cpu_arch = "Unknown"
    os_type = "Unknown"
    busybox_found = False

    for root, dirs, files in os.walk(extracted_dir):

        for file in files:

            filepath = os.path.join(root, file)

            try:
                with open(filepath, "rb") as f:

                    data = f.read()

                    if b"mips" in data.lower():
                        cpu_arch = "MIPS"

                    if b"arm" in data.lower():
                        cpu_arch = "ARM"

                    if b"linux" in data.lower():
                        os_type = "Linux"

                    if b"busybox" in data.lower():
                        busybox_found = True

            except:
                pass

    print("CPU Architecture:", cpu_arch)
    print("Operating System:", os_type)

    if busybox_found:
        print("[+] BusyBox detected")
