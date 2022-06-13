#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("welcome to the tip calcualtor.")
bill_amount=float(input("what is the amount of bill?: $"))
tip_percent=int(input("What percent tip you like to give? 10,12, or 15? "))
people=int(input("How many people to split the bill? "))
amount_each=bill_amount*(1+tip_percent/100)/people
round_amount=round(amount_each,2) #this will round the value to 2 decimal places 
round_amount="{:.2f}".format(amount_each) #this will add a zero to second place if the round number is at first place
print(f"Each person sholud pay: {round_amount}")