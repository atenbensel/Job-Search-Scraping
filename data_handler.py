import csv

def save_job_data_to_csv(job_data):
  with open('job_data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['job_title', 'company_name', 'location', 'description', 'application_link'])
    write.write
