import requests
from bs4 import BeautifulSoup

#This follows a real python tutorial

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'lxml')
#print(soup.prettify())
result = soup.find(id ="ResultsContainer")
job_card = result.find_all("div", class_ = "card-content")
#for job in job_card:
#    job_title = job.find("h2", class_= "title is-5")
#    job_subtitle = job.find("h3", class_ = "subtitle is-6 company") #I could also use class_ = "company" and it will work 
#    location = job.find("p", class_ = "location")
#    posted_time = job.find("p", class_ = "is-small has-text-grey")
#    time_tag = posted_time.time #same as posted_time.find("time")
#    job_time = time_tag["datetime"]

#   print(job_title.text.strip())
#    print(job_subtitle.text.strip())
#    print(location.text.strip())
#    print(job_time)
#    print()

#Say I need only python related jobs
python_jobs = result.find_all("h2", string =  lambda text: "python" in text.lower())#This will return all jobs with python in their name
print(python_jobs)

python_jobs_cards = [elements.parent.parent.parent for elements in python_jobs]
print("Python related jobs")
for job in python_jobs_cards:
    job_title = job.find("h2", class_= "title is-5")
    job_subtitle = job.find("h3", class_ = "subtitle is-6 company") #I could also use class_ = "company" and it will work 
    location = job.find("p", class_ = "location")
    job_links = job.find_all("a")[1]["href"]
    posted_time = job.find("p", class_ = "is-small has-text-grey")
    time_tag = posted_time.time #same as posted_time.find("time")
    job_time = time_tag["datetime"]

    print(job_title.text.strip())
    print(job_subtitle.text.strip())
    print(location.text.strip())
    print(job_time)
    print("Apply here: "+job_links)
    print()
