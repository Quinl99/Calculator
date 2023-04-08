print("CALCULATOR");
print("What operation fo you want to perfom today?");
print("A:Add");
print("B:Subtract");
print("C.Divide");
print("D:Multiply");


choice = input()

FirNum = input("Enter 1st Number:")
SecNum = input("Enter 2nd Number:")

if choice == 'A':
    final = str(int(FirNum) + int(SecNum));
    print("Sum:" + final);
elif choice == 'B':
    FirNum - SecNum;
    final1 = str(int(FirNum) - int(SecNum));
    print("Sum:" + final1);
elif choice == 'C':
    final2 = str(int(FirNum) / int(SecNum));
    print("Sum:" + final2);
elif choice =='D':
    final3 = str(int(FirNum) * int(SecNum));
    print("Sum:" + final3);

