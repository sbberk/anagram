#! /usr/local/bin/python

'''For a dictionary file, finds all anagrams that are at least 4 letters long.  Only returns words that satisfy the number of anagram 
words being greater than or equal to the number of letters in the word.'''

import sys

def openDictionary(txt_file = 'dictionary.txt'):
  '''Opens dictionary file and creates a word_list array.'''
  try:
    word_file = open(txt_file, 'r')
  except IOError:
    raise IOError("Error opening the file")
    sys.exit(1)
  word_list = word_file.readlines()
  word_file.close()
  return word_list

def lowerAndSort(word):
  '''Returns a lower case, sorted version of the word for comparing to anagrams'''
  word = word.lower()
  sorted_word = ''.join(sorted(word))
  return sorted_word

def analyzeWordList(word_list):
  '''Compares words to their sorted_word and creates a dictionary to avoid duplicates.  Restricts output to words with 4 or more characters.''' 
  anagram_dict = {}
  for word in word_list:
    word = word.strip()
    if len(word) >= 4:
      sorted_word = lowerAndSort(word)
      if sorted_word not in anagram_dict:
        anagram_dict[sorted_word] = [word]
      else:
        anagram_dict[sorted_word].append(word)
  return anagram_dict

def printSolution(anagram_dict):
  '''Compare the number of anagram words to the letters and print each that passes.'''
  for sorted_word in anagram_dict:
    list_length = len(anagram_dict[sorted_word])
    word_length = len(sorted_word)
    if list_length >= word_length:
      print ','.join(anagram_dict[sorted_word])
  
def main():
  word_list = openDictionary()
  anagram_dict = analyzeWordList(word_list)
  printSolution(anagram_dict)

if __name__ == '__main__':
  main()
