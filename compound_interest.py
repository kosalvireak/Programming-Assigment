Loop = True
while Loop:
    # All the input should be intergers and bigger than 1
    A = float(input("Deposit: "))
    while A <= 0:
        print("Your input should be bigger than 1. Try again!")
        A = float(input("Deposit: "))
    N = int(input("Duration of deposit in months: "))
    while N < 1 or N > 36:
        print("Your duration of the month should be smaller than 37 and bigger than 0. Try again!")
        N = int(input("Duration of deposit in months: "))
    W = float(input("Interest rate: "))
    while W <= 0 or W > 12:
        print("Your interest rate should be smaller than 12 and bigger than 0. Try again!")
        W = float(input("Interest rate: "))


    print("Month  ", "Deposit  ", "Total Deposits  ", "This Month's interest  ", "Total-Interest Earned  ",
          " Total-Value To-Date ")
    Total_dep = 0
    Total_int = 0
    sum_of_M = 0
    Month_int = 1  # First month interest = 1, next month interest = 0.01*(total value old month + new deposit this month)
    for i in range(1, N + 1, 1):
        Total_dep += A
        M = (1 + (W / 1200)) ** i  # M is the multiply part of F
        sum_of_M += M
        F = A * sum_of_M
        Total_int = F - Total_dep
        print(format(i, "2"), format(A, "12.2f"), format(Total_dep, "10.2f"), format(Month_int, "13.2f"),
              format(Total_int, "24.2f"), format(F, "25.2f"))
        Month_int = (F + A) /A
        i += 1
    userResponse = input("Do you want to do it again?(y/n): ")
    Loop = userResponse == "y"
print("Thank!")