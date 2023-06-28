from flask import Flask, render_template, request, send_file
import os
import xml.etree.ElementTree as ET
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle file upload
        file = request.files['file']
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Analyze the .nessus file and generate the CSV file
        host_data = analyze_nessus_file(file_path)
        csv_file_path = generate_csv(host_data, file.filename)

        # Provide the CSV file for download
        return send_file(csv_file_path, as_attachment=True)

    return render_template('index.html')

def analyze_nessus_file(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    host_data = {}

    for report in root.findall(".//Report"):
        for host in report.findall(".//ReportHost"):
            ip_address = host.get("name")
            host_data[ip_address] = set()

            for item in host.findall(".//ReportItem"):
                port = item.get("port")
                protocol = item.get("protocol")
                service = item.get("svc_name")
                host_data[ip_address].add((port, protocol, service))

    return host_data

def generate_csv(host_data, filename):
    csv_filename = os.path.splitext(filename)[0] + ".csv"
    csv_path = os.path.join(app.config['UPLOAD_FOLDER'], csv_filename)

    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Host', 'Port', 'Protocol', 'Service'])

        for host, data in host_data.items():
            for port, protocol, service in data:
                writer.writerow([host, port, protocol, service])

    return csv_path

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = 'uploads'
    app.run(debug=True)
