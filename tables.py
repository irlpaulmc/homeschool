# Tables fun
import random
import time

def build_random_array(start, end):
	"""
	start(int), end (int)
	returns an array with randomised non-repeating
	numbers in the range between start and end
	"""
	myarray=[]
	#create linear array
	for i in range(start, end):
		myarray.append(i)

	#randomise
	for j in range(0, len(myarray)*2):
		firstrandom = random.randint(0, len(myarray)-1)
		secondrandom = random.randint(0, len(myarray)-1)
		tempvar = myarray[firstrandom]
		myarray[firstrandom] = myarray[secondrandom]
		myarray[secondrandom] = tempvar

	return myarray

inputok = False
correct = 0

#parse input
while (not inputok):
  which_table = input("Please enter which table you want to test (e.g. '-4' for minus four tables: ")
  if (which_table[0] == '-'):
      is_minus = -1
      inputok = True
  elif (which_table[0] == '+'):
      is_minus = 1
      inputok = True
  else:
      print("please choose plus or minus")
      inputok = False
  if (len(which_table) == 2):
  	number = int(which_table[1])
  elif (len(which_table) == 3):
  	number = int(which_table[1:3])
  else:
  	print("Only support numbers 1-12")
  	inputok = False

if(is_minus < 0):
	print ("Will test the minus " + str(number) + " tables")
else:
	print ("Will test the plus " + str(number) + " tables")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#randomise the questions
testarray = build_random_array(1,13)

#initialise timer
starttime = time.time()

#ask the questions
for question in range(0,12):
	answer = (testarray[question] + (is_minus * number))
	guess = int(input (str(testarray[question]) + which_table + " = "))
	if(guess == answer):
		print("*** CORRECT ***")
		correct += 1
	else:
		print("--- INCorrect ---")
	print ("====================================================================")

endtime=time.time()
print ("GAME OVER")
print ("Score: " + str(correct) + "/12")
print ("elapsed time = " + str(round(endtime-starttime)) + " seconds.")
