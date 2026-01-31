import subprocess

TARGET = "127.0.0.1"
REPORT_FILE = "reports/scan_report.txt"

print(f"[+] Scanning target: {TARGET}")

result = subprocess.run(
    ["nmap", "-sS", TARGET], #SYN scan (stealth scan) through nmap to TARGET IP
    capture_output=True,   #Captures Nmap output instead of printing it
    text=True              #coverts output into readable text 
)

open_ports = []            #this list stores 22/tcp open ssh, 80/tcp open http

for line in result.stdout.split("\n"):         #Breaks Nmap output into lines
    if "/tcp" in line and "open" in line:       #This means:Ignore closed ports ignore udp only care about opepn tcp servies
        open_ports.append(line.strip())         #removes extra spaces

with open(REPORT_FILE, "w") as report:          #opens report file in thhe  write mode, Automatically closes file after use
    report.write(f"Target: {TARGET}\n\n")
    report.write("Open Ports Detected:\n")

    if not open_ports:                         #prevents empty report. show clean logic
        report.write("No open ports found.\n")
    else:
        for port in open_ports:
            report.write(f"- {port}\n")

    report.write("\nOverall Risk Level: MEDIUM\n")
    report.write("Recommendation:\n")
    report.write("- Review exposed services\n")
    report.write("- Close unused ports\n")

print("[+] Scan completed. Check reports/scan_report.txt")
