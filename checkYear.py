print("=====Checking Your Program=====")
print("1.Check Leap Year")
print("2.Check total day")
print("3.    Exit       ")

menu=0
while menu!=3:
    menu=int(input("Select : "))
    if menu==1:
        year=int(input("Enter year to check: "))
        if year%4==0 and year%100!=0:
            print(str(year)+" is leap year")
        elif year%400==0:
            print(str(year)+" is leap year")
        else:
            print(str(year)+" is not leap year")
    elif menu==2:
        print("Enter month and date")
        month=int(input("Month: "))
        date=int(input("Date: "))
        if month%2!=0 :
            if month==1:
                th_day=date
            elif month<9:
                th_day=date+((month-1)/2*61)-2
            else:
                th_day=date+((month-1)/2*61)-2+1
            
        elif month%2==0:
            if month==2:
                th_day=date+31
            else:
                th_day=date+((month-2)/2*61)+31-2
        print(2019,'.',month,'.',date,' is ',th_day,"th day in 2019.")
    elif menu==3:
        print("Thanks for using program.")
