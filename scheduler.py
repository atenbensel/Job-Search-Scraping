from google_jobs_scraper import scrape_google_jobs
from linkedin_jobs_scraper import scrape_linkedin_jobs

def job_scraping_job():
  print("Running job scraping...")
  scrape_google_jobs()
  scrape_linkedin_jobs()

def schedule_job_scraping():
  scheduler = BlockingScheduler()
  # schedule to run every day at midnight?
  scheduler.add_job(job_scraping_job, 'cron', hour=0)
  print("Job search refresh scheduled at midnight.")
  scheduler.start()
