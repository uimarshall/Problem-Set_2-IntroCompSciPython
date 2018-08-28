# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 00:13:46 2018

@author: CyberCloned

"""


import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist = load_words()

# =============================================================================
# for word in wordlist:
#     
#     if word[1] == "t" and word[len(word)-1] == "t":
#     
#         print(word)
# =============================================================================
        
#==============================================================================
        
def strip_spaces(word):
    
    stripped_word = ""
    
    for letter in word:
        
        new_letter = letter.strip()
        
        stripped_word = stripped_word + new_letter
    
    return stripped_word

#==============================================================================

def match_with_gaps(my_word, other_word):
    
    #Call the function that strips off spaces from the guessed word
    stripped_my_word = strip_spaces(my_word)
    print(my_word)
    
    #If the lenght of the other_word isn't equal to the stripped word, 
    #the words cannot be same
    if len(stripped_my_word) != len(other_word):
        
        return False
    
    else:
        
        #Set the counter to count how many indexed letters in the stripped 
        #my_word are equal to those in other_word
        counter = 0
        
        for i, letter in enumerate(stripped_my_word):
            
            if letter == "_":
                
                pass
            
            else:
                
                if other_word.index(letter) == i:
                    
                    counter += 1
                    
    if counter == len(set(stripped_my_word)) - 1:
        
        return True
    
#==============================================================================
    
# =============================================================================
def show_possible_matches(my_word):
     
    stripped_my_word = strip_spaces(my_word)
     
    index_list = []
     
    letter_list = []
     
    for index, letter in enumerate(stripped_my_word):
        print(stripped_my_word)
        
        if letter == "_":
             
            pass
         
        else:
                     
            index_list.append(index)
             
            letter_list.append(letter)
            
    print(index_list, letter_list)        

    for word in wordlist:
        
        if len(word) == len(stripped_my_word):
            
            word_to_list = list(word)
            
            #Loop thru the index list and append all the letters in
            #word_to_list to a new list
            word_letter_list = []
            
            for i in index_list:
                
                word_letter_list.append(word_to_list[i])
                
            #print(word_letter_list)
                
             #Compare the letter_list from stripped_my_word and 
             #the word_letter_list from the word from wordlist    
            if ((letter_list > word_letter_list) - (letter_list < word_letter_list)) == 0:
                
                print(word)
                
            #else:
                
                #print("No matches found!")
                
     
                
# =============================================================================
        
def capture_word():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    
    for word in wordlist:
        
        return word
# =============================================================================
            
"""def show_possible_matches(my_word):
    
    for word in wordlist:
        
        if match_with_gaps(my_word, word) == False:
            
            print (word)
            
        else:
            
            print("No word matches found")"""
                    
#my_word = "z_ go_ e"

my_word = "h_ li_ opt_ _ "

my_word = "app_ _"
 
#my_word = "t_ _tl_ "
                   
show_possible_matches(my_word)