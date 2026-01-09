import logging

logging.basicConfig(
    filename='security.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def log_event(event, user_id):
    logging.info(f"{event} | user_id={user_id}")
