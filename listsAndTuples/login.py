# Listing 2-4.Sequence Membership Example

# Check a user name and PIN code

database = [
	['albert', '1234'],
	['debelt', '4244'],
	['smith',  '1123'],
	['jones',  '8888']
]

username = raw_input('User name: ')
pin = raw_input('PIN code: ')
if [username, pin] in database: 
	print 'Access granted'
	raw_input()
else:
	print 'Access denied'
