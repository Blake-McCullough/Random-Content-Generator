#Made By Blake McCullough
#Discord - Spoiled_Kitten#4911
#Github - https://github.com/Blake-McCullough/
#Email - privblakemccullough@protonmail.com
import random
import os 
import sys
import time
import requests
import json
import datetime
def randomlistgenerator():

  #for finding all words list
  with open('words.txt') as f:
    wordslist = f.read().splitlines()


  maxchoice = len(wordslist)
  options = int(input("How many fields to fill?\n"))

  choices = []
  levelstoclear = 13
  finishedlist = []
  i = 0
  e=0
  while i < options:
    i=i+1
    choice = int(input('Option:'+str(i)+'\nSelect an option, \n1 - Integers \n2- Strings\n3 - Dates\n4 - Street Addresses\n5 - Number\n6 - Post Code\n7 - State\n8 - Names\n9 - Time\n10 - Min-MaxTempature\n'))
  
    if choice == 1:
      choices.append('Int')
      delete_last_line(levelstoclear)
    elif choice == 2:
      choices.append('String')
      delete_last_line(levelstoclear)
    elif choice == 3:
      choices.append('Date')
      delete_last_line(levelstoclear)
    elif choice == 4:
      choices.append('Street_Address')
      delete_last_line(levelstoclear)
    elif choice == 5:
      choices.append('Phone_Number')
      delete_last_line(levelstoclear)
    elif choice == 6:
      choices.append('Post_Code')
      delete_last_line(levelstoclear)
    elif choice == 7:
      choices.append('State')
      delete_last_line(levelstoclear)
    elif choice == 8:
      choices.append('Name')
      delete_last_line(levelstoclear)
    elif choice == 9:
      choices.append('Time')
      delete_last_line(levelstoclear)
    elif choice == 10:
      choices.append('MinMaxTemp')
      delete_last_line(levelstoclear)
    else: 
      i = i-1
      delete_last_line(levelstoclear)
      print('error')
      

    
  print(choices)

  rows = int(input('How many times do you wish to generate a field?\n'))
  while e<rows:
    d = 0
    nearlyfinishedlist = []
    while d < options:
      
      if choices[d]=='Int':
        nearlyfinishedlist.append(random.randint(0,200))
      elif choices[d]=='String':
        nearlyfinishedlist.append(wordslist[random.randint(1,maxchoice)])
      elif choices[d] =='Date':
        nearlyfinishedlist.append(random_date("1/1/2008", "2/1/9999", random.random()))
      elif choices[d] == 'Street_Address':
        nearlyfinishedlist.append(get_address(wordslist,maxchoice))
      elif choices[d] =='Phone_Number':
        nearlyfinishedlist.append(random.randint(1000000000,999999999999))
      elif choices[d] == 'Post_Code':
        nearlyfinishedlist.append(random.randint(1000,9999))
      elif choices[d] == 'State':
        nearlyfinishedlist.append(get_state())
      elif choices[d] == 'Name':
        nearlyfinishedlist.append(get_name())
      elif choices[d] == 'MinMaxTemp':
        min = random.randint(0,50)
        max = random.randint(min,100)
        nearlyfinishedlist.append(min)
        nearlyfinishedlist.append(max)
      elif choices[d] == 'Time':
        nearlyfinishedlist.append(str(random.randint(1,12))+':'+str(random.randint(0,5))+str(random.randint(0,9)))
      d = d+1
    e = e+1
    finishedlist.append(nearlyfinishedlist)
  output = {'results':finishedlist,'Layout':choices}
  print(output)

  with open('results.json', 'w') as f:
    json.dump(output, f)
  print('SUCCESS!')


    
def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    time = datetime.datetime.strptime(str_time_prop(start, end, '%d/%m/%Y', prop), "%d/%m/%Y").strftime("%Y-%m-%d")
    return time
    
def get_address(wordslist,maxchoice):
  with open('streetendings.txt') as f:
    streetendingoptions = f.read().splitlines()
  streetendingscount = len(streetendingoptions)
  streetname = str(random.randint(1,100)) + ' '+wordslist[random.randint(1,maxchoice)]+' '+streetendingoptions[random.randint(1,streetendingscount)]
  return streetname



#last line deletion
def delete_last_line(count):
    i = 0
    while count > i:
      "Use this function to delete the last line in the STDOUT"
  
      #cursor up one line
      sys.stdout.write('\x1b[1A')
  
      #delete last line
      sys.stdout.write('\x1b[2K')
      i=i+1

def get_state():
  
  states = ["WA", "SA", "NT", "ACT", "TAS", "QLD", "NSW", "VIC"]
  state = states[random.randint(0,8)]
  return state
def get_name():
  with open('names.txt') as f:
    nameoptions = f.read().splitlines()
  namecount = len(nameoptions)
  name = nameoptions[random.randint(0,namecount)]
  return name

  
if __name__ == '__main__':
  randomlistgenerator()
