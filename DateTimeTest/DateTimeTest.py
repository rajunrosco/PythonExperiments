
import datetime

def Practice_Datetime():
	
	birthday = datetime.date(1970, 1, 26)
	
	today = datetime.date.today()
	delaydays = 42
	delay = datetime.timedelta( days=delaydays )
	
	newdate = today + delay
	result = newdate.strftime("%A %B %d %Y")
	if newdate.strftime("%A").lower() == "friday":
		print("TGIF!")
	
	print(result)
	print("Birthday = "+birthday.strftime("%A, %B, %d, %Y"))
	print("Birthday = "+birthday.strftime("%m/%d/%Y"))
	delta = newdate - birthday
	
	print(delta.days)


	#String to DateTime Object:
	datetime_str = '09/19/18 13:55:26'

	datetime_object = datetime.datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

	print(type(datetime_object))
	print(datetime_object)  # printed in default format

	weirdtime_str = "A_Weird_20201106_135525"
	weirdtime_object = datetime.datetime.strptime(weirdtime_str, 'A_Weird_%Y%m%d_%H%M%S')
	print(weirdtime_object)
		
def main():
	Practice_Datetime()
	
if __name__ == '__main__':
  main()
