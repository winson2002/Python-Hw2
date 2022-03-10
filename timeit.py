import time

def calculate_time(func):
	def wrapper():
		start = time.time()
		func()
		end = time.time()
		total = end - start
		return f"Total time {total}"
	return wrapper
