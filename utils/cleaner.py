import json
import os

def filter_new_jobs(jobs):
    if not os.path.exists('sent_history.json'):
        with open('sent_history.json', 'w') as f:
            json.dump([], f)

    with open('sent_history.json', 'r', encoding='utf-8') as f:
        sent_links = json.load(f)

    new_jobs = [job for job in jobs if job["url"] not in sent_links]
    return new_jobs