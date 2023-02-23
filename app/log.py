import logging
from typing import List


class Logger:
	def __init__(self, name: str, log_file: str = None, level: str = "INFO", log_console: bool = True):
		self.logger = logging.getLogger(name)
		self.logger.setLevel(level.upper())
		self.log_file = log_file
		self.log_console = log_console

		formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

		if self.log_file:
			file_handler = logging.FileHandler(log_file)
			file_handler.setFormatter(formatter)
			self.logger.addHandler(file_handler)

		if self.log_console:
			console_handler = logging.StreamHandler()
			console_handler.setFormatter(formatter)
			self.logger.addHandler(console_handler)

	def info(self, message: str):
		self.logger.info(message)

	def warning(self, message: str):
		self.logger.warning(message)

	def error(self, message: str):
		self.logger.error(message)

	def critical(self, message: str):
		self.logger.critical(message)

	def exception(self, message: str):
		self.logger.exception(message)

	def log(self, level: str, message: str):
		getattr(self.logger, level.lower())(message)

	def log_list(self, level: str, messages: List[str]):
		for message in messages:
			self.log(level, message)