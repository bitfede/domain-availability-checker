#!/usr/bin/python3

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
resultfile = open('available-domains.txt', 'a')

count = 0
#loop thru every word in the dictionary
for word in dictionary:
    count = count + 1
    word = word.rstrip()
    domain = '{}.com'.format(word)
    whoisresult = subprocess.check_output('whois {}'.format(domain), shell=True)
    whoisresult = whoisresult.decode('utf-8').split('\n')
    domainstatus = whoisresult[0].strip('   ')
    if "No match for" in domainstatus:
        #BINGO!
        print("[!!!] DOMAIN AVAILABLE: {}".format(domain))
        resultfile.write(domain)
    else:
        #do nothing
        print("[*] DOMAIN {} NOT AVAILABLE".format(domain))

print("Finish! Total Domains Scanned: {}".format(count))
