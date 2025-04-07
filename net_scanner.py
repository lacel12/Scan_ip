# net_scanner.py
import argparse
import csv
import ipaddress
import platform
import subprocess
import asyncio

def ping(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    try:
        output = subprocess.check_output(["ping", param, "1", str(ip)], stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def scan_range(ip_range):
    net = ipaddress.ip_network(ip_range, strict=False)
    results = []
    for ip in net.hosts():
        active = ping(ip)
        results.append((str(ip), 'Active' if active else 'Inactive'))
    return results

def scan_file(file_path):
    results = []
    with open(file_path) as f:
        for line in f:
            ip = line.strip()
            if ip:
                active = ping(ip)
                results.append((ip, 'Active' if active else 'Inactive'))
    return results

def save_results(results, output_file='results.csv'):
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['IP', 'Status'])
        for row in results:
            writer.writerow(row)

def main():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')

    scan_cmd = subparser.add_parser('scan')
    scan_cmd.add_argument('--range', help="Plage d'adresses IP à scanner (ex: 192.168.1.0/24)")
    scan_cmd.add_argument('--file', help="Fichier contenant les IP à scanner")

    args = parser.parse_args()

    if args.command == 'scan':
        if args.range:
            results = scan_range(args.range)
        elif args.file:
            results = scan_file(args.file)
        else:
            print("Erreur : spécifiez --range ou --file")
            return

        save_results(results)
        for ip, status in results:
            print(f"{ip} - {status}")

if __name__ == '__main__':
    main()
