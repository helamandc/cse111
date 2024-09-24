"""
Write a Python program named sentences.py that generates simple English sentences

Author: Helaman Del Castillo
Date: September 24, 2024
Title: Sentences
"""
#This module will help generate a random word
import random

def main():
  """Display 6 sentences based on the Quantity and Verb tense below.
  Please note of the definition below for quantity:
  single = 1
  plural = 2
  """
  #This variable will store the characteristics mentioned in the requirements
  characteristics = [[1,"past"],[1,"present"],[1,"future"],[2,"past"],[2,"present"],[2,"future"]]
  i = 0
  while i < 6:
   make_sentence(characteristics[i][0],characteristics[i][1])
   i += 1
#This function will create the sentence using all the other user-defined functions
def make_sentence(quantity, tense):
  """Build and return a sentence with three words:
  a determiner, a noun, and a verb. The grammatical
  quantity of the determiner and noun will match the
  number in the quantity parameter. The grammatical
  quantity and tense of the verb will match the number
  and tense in the quantity and tense parameters.
  """
  #Extra requirement: I have called the get_prepositional_phrase function twice in my make_sentence function. This will add another set of phrase in the sentence.
  print(f"{get_determiner(quantity)} {get_noun(quantity)} {get_prepositional_phrase(quantity)} {get_verb(quantity, tense)} {get_prepositional_phrase(quantity)}.")
#This function will randomly choose a determiner
def get_determiner(quantity):
  """Return a randomly chosen determiner. A determiner is
  a word like "the", "a", "one", "some", "many".
  If quantity is 1, this function will return either "a",
  "one", or "the". Otherwise this function will return
  either "some", "many", or "the".
  Parameter
      quantity: an integer.
          If quantity is 1, this function will return a
          determiner for a single noun. Otherwise this
          function will return a determiner for a plural
          noun.
  Return: a randomly chosen determiner.
  """
  if quantity == 1:
      words = ["a", "one", "the"]
  else:
      words = ["some", "many", "the"]
  # Randomly choose and return a determiner.
  word = random.choice(words)
  return word.capitalize()
#This function will randomly choose a noun
def get_noun(quantity):
  """Return a randomly chosen noun.
  If quantity is 1, this function will
  return one of these ten single nouns:
      "bird", "boy", "car", "cat", "child",
      "dog", "girl", "man", "rabbit", "woman"
  Otherwise, this function will return one of
  these ten plural nouns:
      "birds", "boys", "cars", "cats", "children",
      "dogs", "girls", "men", "rabbits", "women"
  Parameter
      quantity: an integer that determines if
          the returned noun is single or plural.
  Return: a randomly chosen noun.
    """
  if quantity == 1:
      words = ["bird", "boy", "car", "cat", "child",
      "dog", "girl", "man", "rabbit", "woman"]
  else:
      words = ["birds", "boys", "cars", "cats", "children",
      "dogs", "girls", "men", "rabbits", "women"]
  # Randomly choose and return a determiner.
  word = random.choice(words)
  return word
#This function will randomly choose a verb that matches with the requested quantity and verb tense
def get_verb(quantity, tense):
  """Return a randomly chosen verb. If tense is "past",
  this function will return one of these ten verbs:
      "drank", "ate", "grew", "laughed", "thought",
      "ran", "slept", "talked", "walked", "wrote"
  If tense is "present" and quantity is 1, this
  function will return one of these ten verbs:
      "drinks", "eats", "grows", "laughs", "thinks",
      "runs", "sleeps", "talks", "walks", "writes"
  If tense is "present" and quantity is NOT 1,
  this function will return one of these ten verbs:
      "drink", "eat", "grow", "laugh", "think",
      "run", "sleep", "talk", "walk", "write"
  If tense is "future", this function will return one of
  these ten verbs:
      "will drink", "will eat", "will grow", "will laugh",
      "will think", "will run", "will sleep", "will talk",
      "will walk", "will write"
  Parameters
      quantity: an integer that determines if the
          returned verb is single or plural.
      tense: a string that determines the verb conjugation,
          either "past", "present" or "future".
  Return: a randomly chosen verb.
  """
  if tense.lower() == "past":
      words = ["drank", "ate", "grew", "laughed", "thought",
      "ran", "slept", "talked", "walked", "wrote"]
  elif tense.lower() == "present" and quantity == 1:
      words = ["drinks", "eats", "grows", "laughs", "thinks",
      "runs", "sleeps", "talks", "walks", "writes"]
  elif tense.lower() == "present" and quantity > 1:
      words = ["drink", "eat", "grow", "laugh", "think",
      "run", "sleep", "talk", "walk", "write"]
  else:
      words = ["will drink", "will eat", "will grow", "will laugh",
      "will think", "will run", "will sleep", "will talk",
      "will walk", "will write"]
  # Randomly choose and return a determiner.
  word = random.choice(words)
  return word
#This function will randomly choose a preposition
def get_preposition():
  """Return a randomly chosen preposition
  from this list of prepositions:
      "about", "above", "across", "after", "along",
      "around", "at", "before", "behind", "below",
      "beyond", "by", "despite", "except", "for",
      "from", "in", "into", "near", "of",
      "off", "on", "onto", "out", "over",
      "past", "to", "under", "with", "without"
  Return: a randomly chosen preposition.
  """
  words = ["about", "above", "across", "after", "along",
      "around", "at", "before", "behind", "below",
      "beyond", "by", "despite", "except", "for",
      "from", "in", "into", "near", "of",
      "off", "on", "onto", "out", "over",
      "past", "to", "under", "with", "without"]
  # Randomly choose and return a determiner.
  word = random.choice(words)
  return word
#This function will generate a random prepositional phrase
def get_prepositional_phrase(quantity):
  """Build and return a prepositional phrase composed
  of three words: a preposition, a determiner, and a
  noun by calling the get_preposition, get_determiner, 
  and get_noun functions.
  Parameter
      quantity: an integer that determines if the
          determiner and noun in the prepositional
          phrase returned from this function should
          be single or plural.
  Return: a prepositional phrase.
  """
  preposition = get_preposition()
  determiner = get_determiner(quantity).lower()
  noun = get_noun(quantity)
  phrase = f"{preposition} {determiner} {noun}"
  return phrase

main()    





