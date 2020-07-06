# -*- coding: utf-8 -*-
# Example: Scrolling text on display if the string length is major than columns in display.
# Created by Dídac García.

# Import necessary libraries for communication and display use
import lcddriver
import time

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = lcddriver.lcd()

# Main body of code

def long_string(display, text = '', num_line = 1, num_cols = 20):
	""" 
	Parameters: (driver, string to print, number of line to print, number of columns of your display)
	Return: This function send to display your scrolling string.
	"""
	if(len(text) > num_cols):
		display.lcd_display_string(text[:num_cols],num_line)
		time.sleep(1)
		for i in range(len(text) - num_cols + 1):
			text_to_print = text[i:i+num_cols]
			display.lcd_display_string(text_to_print,num_line)
			time.sleep(0.2)
		time.sleep(1)
	else:
		display.lcd_display_string(text,num_line)
sleep.time(1)

while True:
	
	long_string(display, "Hello World!", 1)
	# An example of infinite scrolling text
	long_string(display, "Hello friend! This is a looooooooooong text!" + "      ", 2)

#	display.lcd_clear()
