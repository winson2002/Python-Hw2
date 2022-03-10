import time

def calculate_time(func):
	def wrapper():
		start = time.time()
		stored = func()
		end = time.time()
		print(f'Total time {start - end}')
		return stored
	return wrapper
