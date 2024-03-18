import logging

def generate_logs():
    logging.basicConfig(
        filename="../selfLearning/RajuFirstLog.log",
        level=logging.INFO,
        format='%(asctime)s -%(levelname)s -%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %p'
    )
    return logging.getLogger()