#   variables to be inputted 
annual_salary = float (input ("Enter your Annual Salary:"))
portion_saved = float (input ("Enter the percent of your salary to save, as a decimal:"))
total_cost = float (input ("Enter the cost of your dream home:"))
semi_annual_raise = float (input ("Enter the semi-annual rate, as a decimal:"))
#   variables which are defined
#   All varaibles are of the type float
portion_down_payment = 0.25*total_cost
r = 0.04
current_savings = 0
month = 0
while current_savings <= portion_down_payment :
        if month % 6 == 0 and month != 0:
            annual_salary = annual_salary * (1 + semi_annual_raise)
        monthly_salary = annual_salary/12
        current_savings = current_savings + monthly_salary*portion_saved + (current_savings*0.04)/12
        month = month + 1
print ('number of months:',  month)