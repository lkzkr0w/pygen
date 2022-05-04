#!/usr/bin/env python3

import itertools
import sys
    
def make_wordlist(base_list):
    #TODO
    

def main():
    keywords = sys.argv[1]
    keywords_list = keywords.split(',')
    print(keywords_list)                    #debug print

    for i in range(0,10):
        keywords_list.append(str(i))
    print(keywords_list)                    #debug print
    
    make_wordlist(keywords_list)

main()
