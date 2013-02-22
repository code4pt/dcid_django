def trim_3digits(n):
	""" Shorts a number to 3 digits and an optional letter. Letters are added
	to represent multiples of a thousand: K for 1000, M for 1000000, ... 
	Examples: 123456 => 123K; 7654321 => 7M """
	number = str(n)
	n_digits = len(number)
	ten_times = 0
	while(n_digits > 3):
		n_digits -= 3
		ten_times += 1
	if(ten_times == 0):
		return number
	elif(ten_times == 1):
		return number[:n_digits] + "K"
	elif(ten_times == 2):
		return number[:n_digits] + "M"
	else:
		return number