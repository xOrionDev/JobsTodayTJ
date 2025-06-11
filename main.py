import logging
import json
from telegram import Bot
from config import TELEGRAM_TOKEN, CHANNEL_ID
from parsers.vazifa import get_vacancies_from_vazifa
from utils.cleaner import filter_new_jobs
from utils.hashtags import generate_hashtags

def gather_all_jobs():
    all_jobs = []
    try:
        all_jobs += get_vacancies_from_vazifa()
    except Exception as e:
        logging.warning(f"Ошибка при парсинге: {e}")
    return all_jobs

def format_job_message(job):
    hashtags = generate_hashtags(job["title"], job["description"])
    return f"""🧩 {job['title']} — {job['location']}
📍 Формат: {job['format']}

📌 Требования:
{job['requirements']}

📝 Описание:
{job['description']}

{hashtags}
📞 Контакты: {job['contacts']}
🔗 {job['url']}

Больше вакансий на: @JobsTodayTJ"""

def send_jobs():
    all_jobs = gather_all_jobs()
    new_jobs = filter_new_jobs(all_jobs)

    logging.info(f"Найдено новых вакансий: {len(new_jobs)}")

    for job in new_jobs:
        try:
            msg = format_job_message(job)
            bot.send_message(chat_id=CHANNEL_ID, text=msg)
        except Exception as e:
            logging.error(f"Ошибка при отправке вакансии: {e}")

    with open('sent_history.json', 'r+', encoding='utf-8') as f:
        sent = json.load(f)
        sent += [job["url"] for job in new_jobs]
        f.seek(0)
        json.dump(sent, f, ensure_ascii=False, indent=2)
        f.truncate()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TELEGRAM_TOKEN)
    send_jobs()
