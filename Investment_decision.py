
import numpy_financial as np  
#Intro
print("Welcome to this program which will help you in your investment decision ! ""you'll give me informations on your investment  and i'll compute the ")

# asking the duration of the study and setting it in a list
duration = int(input("duration of the study ? "))
time_line = []
final_time_line = []
def timeline(para):
    time_line.append([i for i in range(para+1)])
    for t in time_line:
        for n in t:
           final_time_line.append(n)

timeline(duration)

# asking for the cost of investment 

input_investment = int(input("cost of investment ? " ))

# asking  if FCF are fixed or variable number

yorn = input("does the FCF stay the same for the entire study ? Y or N ")

# asking for the value(s) of FCF 

cfflst = []
def ask_CFF(para2):
    if para2 == "Y":
        cff0 = int(input("how much will be the FCF ? "))
        cfflst.append(cff0)
        return cfflst
    else:
      print("what are the FCF for the {} years of the study ?(put a space between each FCF) ".format(duration))
      inputcff = int(input("")).split()
      for inputc in inputcff:
          cfflst.append(int(inputc))
      return cfflst
        
fcf1 = ask_CFF(yorn)

# asking for the discount rate

discountr = int(input("What discount rate do you want to use ? (number in % please) "))

# computing the returns on investment and commenting 

result_lst= []
def return_investment_computing(years,fixed,cost,fcf2,rate):
    npv = 0
    irr = 0
    excess_return = 0
    #computation with only one FCF
    if fixed == "Y":
        #Npv computation
        npv += -(cost) 
        for year in years[1:]:
            npv += (fcf2[0]/((1+rate)**(year)))
        #irr computation
        irr += np.irr([(-cost),fcf2])

        #excess return computation
    result_lst.append(npv)
    result_lst.append(irr)
    return result_lst

return_investment_computing(final_time_line,yorn,input_investment,cfflst,(discountr/100))

print(result_lst)




 