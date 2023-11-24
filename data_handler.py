import csv

def save_to_csv(data, filename, mode='w'):
  with open(filename, mode, newline='', encoding='utf-8') as file:
    fieldnames = ['Job Title', 'Company Name', 'Location', 'Job Description', 'Application Link'])
    writer = csv.DictWriter, fieldnames=fieldnames
    
    if mode == 'w':
      writer.writeheader()

    for row in data:
      writer.writerow(row)
