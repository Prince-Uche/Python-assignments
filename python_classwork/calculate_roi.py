#collect input from user
#declare and initialize variables
#use variables to get the return on investment
#use the return on investment to get the roi + investmen_amount
#

investment_amount = float(input("Enter the investment amount: "))

number_of_years = int(input("Enter the number of years: "))

interest_rate = float(input("Enter the interest rate in percentage: "))

rate = interest_rate / 100

print("Years\t", "percent", "ROI")

for years in range(1, number_of_years+1):
    print(years, "\t", interest_rate, "\t", investment_amount*(years+rate))
