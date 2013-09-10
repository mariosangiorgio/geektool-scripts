from datetime import date
import sys

def parse_events(event_file):
	events = []
	for event_line in event_file:
		events.append(parse_event(event_line))
	return sorted(events, key = lambda (event_date, message) : event_date)

def parse_event(event_line):
	# Parses a line representing an event in the form of YYYY-MM-DD MESSAGE
	event_data = event_line.find(' ')	
	event_date = map(int,event_line[:event_data].split('-'))
	message = event_line[event_data:].strip()
	return (date(event_date[0],event_date[1],event_date[2]), message)
	
def pretty_print(event_date, message):
	time_delta = event_date - date.today()
	days_remaining = time_delta.days
	if(days_remaining > 0):
		if days_remaining == 1:
			plural = ' '	# Using a whitespace to have a better alignment
		else:
			plural = 's'
		print "%4.d day%s to %s" % (days_remaining, plural, message)
	else:
		print "Countdown to %s is over" % (message)

event_filename = sys.argv[1]
event_file = open(event_filename)	
for (event_date, message) in parse_events(event_file):
	pretty_print(event_date, message)