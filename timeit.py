import time

def calculate_time(func):
	def wrapper(func):
		start = time.time()
		func()
		end = time.time()
		print(f'Total time {start - end}')
	return wrapper
