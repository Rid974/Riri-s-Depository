
import numpy_financial as npf
import numpy as np

#Intro
print("Welcome to this program which will help you in your investment decision ! \nYou'll give me informations on your investment  and i'll compute: \n\n-The Net Plus Value, \n-Internal Return rate \n-Excess Return")

# asking the duration of the study and setting it in a list
duration = input("\nWhat's the duration of our study ? ")
time_line = []
final_time_line = []
def timeline(para):
    time_line.append([i for i in range(para+1)])
    for t in time_line:
        for n in t:
           final_time_line.append(n)

timeline(int(duration))

# asking for the cost of investment 

input_investment = float(input("\nWhat will it cost ? " ))

# asking  if FCF are fixed or variable number

yorn = input("\nDoes the FCF will be the same for the entire study ? Y or N ")

# asking for the value(s) of FCF 

cfflst = []
def ask_CFF(para2):
    if para2 == "Y":
        cff0 = float(input("\nHow much will be the FCF ? "))
        cfflst.append(cff0)
        return cfflst
    else:
      print("\nWhat are the FCF for the {} years of our study ?\n(put a space between each FCF) ".format(duration))
      inputcff = input("").split(" ")
      for inputc in inputcff:
          cfflst.append(float(inputc))
      return cfflst
        
fcf1 = ask_CFF(yorn)

# asking for the discount rate

discountr = float(input("\nWhat discount rate are we using ? "))

# computing the returns on investment and commenting 

result_lst= []
def return_investment_computing(years,fixed,cost,fcf2,rate):
    npv = 0
    cumcff = []
    irr = 0
    #excess_return = 0
    #computation with only one FCF
    if fixed == "Y":
        #Npv computation
        npv += -(cost)
        for year in years[1:]:
            npv += (fcf2[0]/((1+rate)**(year)))
            cumcff.append(fcf2[0])
        #irr computation
        k = np.array(-cost)
        c = np.array(cumcff)
        z = np.concatenate((k,c),axis = None)
        irr += npf.irr(z)
    #computation with different FCF
    else:
        #Npv computation
        npv += -(cost)
        for year in years[1:]:
            npv += (fcf2[year-1]/((1+rate)**(year)))
            cumcff.append(fcf2[year-1])
         #irr computation
        k = np.array(-cost)
        c = np.array(cumcff)
        z = np.concatenate((k,c),axis = None)
        irr += npf.irr(z)

        
    result_lst.append(npv)
    result_lst.append(irr*100)
    result_lst.append((irr-rate)*100)
    return result_lst

return_investment_computing(final_time_line,yorn,input_investment,cfflst,(discountr/100))

print(("\n\n\nFor an investment of {} On a {} period, \nThe IRR for this project is {}% \nAnd with a Discount rate of {}% \nthe NPV will be {}\nAnd the Excess return {}%.").format(input_investment,duration,round(result_lst[1]),discountr,round(result_lst[0]),round(result_lst[2])))

if result_lst[0] > 0 and result_lst[1]> 0 :
    print("\nYou should pursue this project, you will make money!\n\n\n\n\n")
else:
    print("\nYou shouldn't invest in this project, you'll loose money !\n\n\n\n\n")




 