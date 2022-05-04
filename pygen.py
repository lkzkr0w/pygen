#!/usr/bin/env python3

import itertools
import sys
    
def make_wordlist(base_list):
    long_word = ''
    while len(base_list) > 0:
        long_word += base_list.pop()
    print(long_word)                        #debug print

    # test_wordlist = list(itertools.permutations(long_word))
    # print(test_wordlist)                    #debug print
    
def main():
    keywords = sys.argv[1]
    keywords_list = keywords.split(',')
    print(keywords_list)                    #debug print

    for i in range(0,10):
        keywords_list.append(str(i))
    print(keywords_list)                    #debug print
    
    make_wordlist(keywords_list)

main()
