import csv

def generate_report(data):
    with open("security_report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["IP Address", "Open Port", "Vulnerability"])

        for row in data:
            writer.writerow(row)

    print("Report saved as security_report.csv")
