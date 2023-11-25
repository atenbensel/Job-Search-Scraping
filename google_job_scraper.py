import csv
import requests
import bs4 import BeautifulSoup
from data_handler import save_to_csv

def scrape_google_jobs():
  base_url = "https://wwww.google.com/search?q="
  job_title = "software engineer" # replace with user input

  search_url = f"{base_url}{job_title}+jobs"

  response = requests.get(search_url)

  if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    job_postings = soup.find.all('div', class_='tcoLwb') # need to update based on the actual HTML structure
  
    job_data = []
    for job_posting in job_posting:
      job_title = job_posting.find('div', class_='BjJfJf').text.strip()
      company_name = job_posting.find('span', class_='f3kIre').text.strip()
      location = job_posting.find('span', class_='BjJfJf').text.strip()
      job_description = job_posting.find('span', class_='f3kIre').text.strip()
      application_link = job_posting.find('a", class_='BVG0Nb')['href']

      job_data.append({
        'Job Title':job_title,
        'Company Name': company_name,
        'Location': location,
        'Job Description': job_description,
        'Application Link': application_link,
      })

      save_to_csv(job_data, 'job_data.csv', 'a')

    else:
      print(f"Error: Unable to fetch Google Jobs apage. Status code: {response.status_code}")

scrape_google_jobs
                                            
