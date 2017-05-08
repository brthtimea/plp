import logger
import log_config
import json

with open('log_config.json') as json_data_file:
    data = json.load(json_data_file)

logger = logger.Logger('Event Logger')
print(logger.name)

def log_debug():
	logger.setLevel(data["logging"]["debug"]["level"])
	logger.debug(data["logging"]["debug"]["path"], data["logging"]["debug"]["msg"])

log_debug()

def log_info():
	logger.setLevel(data["logging"]["info"]["level"])
	logger.info(data["logging"]["info"]["path"], data["logging"]["info"]["msg"])

log_info()

def log_warning():
	logger.setLevel(data["logging"]["warning"]["level"])
	logger.warning(data["logging"]["warning"]["path"], data["logging"]["warning"]["msg"])

log_warning()

def log_error():
	logger.setLevel(data["logging"]["error"]["level"])
	logger.error(data["logging"]["error"]["path"], data["logging"]["error"]["msg"])

log_error()

def log_critical():
	logger.setLevel(data["logging"]["critical"]["level"])
	logger.critical(data["logging"]["critical"]["path"], data["logging"]["critical"]["msg"])

log_critical()


def log_generic():
	logger.generic_log(data["logging"]["debug"]["level"], "Generic message from logger test")
	#logger.format_log('%(asctime)s - %(message)s')
	
log_generic()
