

Disk Usage:
Used: {disk.used / (1024**3):.2f} GB
Free: {disk.free / (1024**3):.2f} GB
Percent: {disk.percent} %
import psutil
from datetime import datetime

# CPU Usage
cpu = psutil.cpu_percent(interval=1)

# Memory Usage
memory = psutil.virtual_memory()

# Disk Usage
disk = psutil.disk_usage("c:\\")

# Running Processes
processes = []

for process in psutil.process_iter(['pid', 'name']):
    processes.append(process.info)

# Current Time
time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

output = f"""
===================================
System Report
Time: {time}
===================================

CPU Usage:
{cpu} %

Memory Usage:
Used: {memory.used / (1024**3):.2f} GB
Available: {memory.available / (1024**3):.2f} GB
Percent: {memory.percent} %
Running Processes:
"""

for p in processes[:20]:
    output += f"PID: {p['pid']}   Name: {p['name']}\n"

print(output)

# Save to log file
with open("system.log", "a") as file:
    file.write(output)
    file.write("\n")