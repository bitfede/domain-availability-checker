#!/usr/local/bin/python3

##
# AUTHOR: Federico D.
# DATE: December 2018
# PURPOSE: Domain availability checker
##

#dependencies
import requests
import subprocess

#open the dictionary
dictionary = open('google-10000-english.txt', 'r')

count = 0
#loop thru every word in the dictionary
for word in dictionary:
    word = word.rstrip()
    count = count + 1
    whoisresult = subprocess.check_output('whois {}.com'.format(word), shell=True)
    whoisresult = whoisresult.decode('ascii').split('\n')
    print(whoisresult[0].strip('   '))
    if (count == 50):
        exit(0)
