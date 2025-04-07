import os

def save_results(results, output_file='results.csv'):
    desktop_path = os.path.join(os.path.expanduser("~"), "mon_scanner_ip")
    output_path = os.path.join(desktop_path, output_file)

    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['IP', 'Status'])
        for row in results:
            writer.writerow(row)

    print(f"✅ Fichier enregistré : {output_path}")
