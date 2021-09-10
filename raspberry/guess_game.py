from sys import flags
import time
import random
from jarvish_speak import speak
from jarvish_take_command import take_command
import inflect
p = inflect.engine()
def parse_int(textnum, numwords={}):
    # create our default word-lists
    if not numwords:

      # singles
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      # tens
      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      # larger scales
      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      # divisors
      numwords["and"] = (1, 0)

      # perform our loops and start the swap
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    # primary loop
    current = result = 0
    # loop while splitting to break into individual words
    for word in textnum.replace("-"," ").split():
        # if problem then fail-safe
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        # use the index by the multiplier
        scale, increment = numwords[word]
        current = current * scale + increment
        
        # if larger than 100 then push for a round 2
        if scale > 100:
            result += current
            current = 0

    # return the result plus the current
    return result + current
def money_left():
    c=0
    speak("Tell me your name please")
    name =take_command()
    speak("lets play"+name+"it ia a very simple money guessing game")
    speak("You have follow some of my command acoordingly")
    speak("First you have to Assume a amount of money   and further i will instruct accordingly")
    speak("so  get ready ")
    speak("now you Guess a amount of money")
    time.sleep(2)
    speak("Now Borrow Same amount from your best friend")
    digit_money=random.randint(10,100)
    str_money=p.number_to_words(digit_money)
    speak("Now i gave you " +str_money+"ruppes")
    speak("now calculate total")
    flag=True
    while(flag):
      time.sleep(4)
      speak("have calculated")
      flag=take_command()
      if(flag=="yes"):
        break
    speak("You can Throw half of your money")
    time.sleep(2)
    speak("Return the money you have taken fro your best friend")
    time.sleep(2)
    digit_result=digit_money/2
    result_str_money=p.number_to_words(digit_result)
    speak("Now you have"+result_str_money+"ruppes left")
    speak("Am i right"+name)
    am_i=take_command()
    if am_i=="yes":
      speak("thanks for playing with me  and if you want blowjob  open your mouth wide")


































