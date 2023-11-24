# Job Search Scraping Tool

We're building a tool to automate the process of searching for job openings based on a user-specific job title. It scrapes data from two major job search websites, Google Jobs and Linkedin, and store the extracted information in a CSV file.

## Installation

**Install Python 3**: Download and install the latest version of Python 3 <br>
**Install Dependencies**: Install the required Python libraries using pip:<br>
```
  pip install beautifulsoup4 requests apscheduler
```

## Usage

To run the job search scraping tool, open the terminal window and navigate to the open project directory. <br>
Run the following command to start the tool: <br>

## File Structure

```
├── frontend
│   ├── frontend.html
│   ├── frontend.css
│   └── frontend.js
├── google_jobs_scraper.py
├── linkedin_jobs_scraper.py
├── main.py
├── data_handler.py
├── scheduler.py
└── job_data.csv
```
