# Job Search Scraping Tool

We're building a tool to automate the process of searching for job openings based on a user-specific job title. It scrapes data from two major job search websites, Google Jobs and Linkedin, and store the extracted information in a CSV file.

![image](https://github.com/atenbensel/Job-Search-Scraping/assets/89222426/bdfbdcff-22c6-4071-8990-60aa9a25b6c8)

![image](https://github.com/atenbensel/Job-Search-Scraping/assets/89222426/06ab667d-9c1e-42fa-b35a-33dfd6481427)

![image](https://github.com/atenbensel/Job-Search-Scraping/assets/89222426/52192623-1130-4c7f-8456-80f9e562d1b9)


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
