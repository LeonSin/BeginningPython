# Listing 2-1.Indexing Example

# Print out a date, given year, month, and day as numbers

from datetime import date

months = [
	'January',
	'February',
	'March',
	'April',
	'May',
	'June',
	'July',
	'August',
	'September',
	'October',
	'November',
	'December'
]
# A list with one ending for each number form 1 to 31
while(True):
	endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
			+ ['st', 'nd', 'rd'] + 7 * ['th'] \
			+ ['st']
	
	year    = raw_input('Year: ')
	month   = raw_input('Month (1-12): ')
	day     = raw_input('Day (1-31): ')
	
	year_number = int(year)
	month_number = int(month)
	day_number = int(day)
	# To validate the date user input	
	try: 
		date(year_number, month_number, day_number)
		break;
	except ValueError:
		print 'Invalid date input'
		raw_input('please retry')
		continue;
		

# Remember to subtract 1 from month and day to get a correct index

month_name = months[month_number - 1]
ordinal = day + endings[day_number - 1]

print month_name + ' ' + ordinal + ' ' + year
