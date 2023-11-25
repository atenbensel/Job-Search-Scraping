import csv
import requests
import bs4 import BeautifulSoup
from data_handler import save_to_csv

def scrape_google_jobs:
# google scraping jobs logic here

  job_data = []

  job_data.append({
    'Job Title':'Software Engineer',
  })

  save_to_csv(job_data, 'job_data.csv', 'a')
