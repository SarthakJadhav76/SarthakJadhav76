# a) Write a pythonprogram to store roll numbers of student in array who attended
# training program in random order. Write function for searching whether particular
# student attended training program or not, using Linear search and Sentinel search.

# b) Write a python program to store roll numbers of student array who attended training
# program in sorted order. Write function for searching whether particular student
# attended training program or not, using Binary search and Fibonacci search

def crt_database():
    tp_data = []

    print("*** Student Database of Training Program ***")
    count = int(input("Enter Total Number of Students:-  "))
    print("\nEnter Roll Number of Students who attended the training program .")
    for i in range(count):
        x = int(input(f"{i+1}]"))
        tp_data.append(x)
    return tp_data,count
    print("\n**** Attendees Database Created Successfully **** \n")

def lnrsearch(trn_attendees,cnt):
    result = 0
    srch = int(input("Search in Database.\n\tEnter Roll Number to search :- "))

    for j in range(len(trn_attendees)):
        if(trn_attendees[j] == srch):
            result = 1
    if result==1:
        print(f"Student [{srch}] attended the Training Program.")
    else:
        print(f"Student [{srch}] DID NOT attend the Training Program.")

def sentinelsearch(trn_attendees,cnt):
    srch = int(input("Search in Database.\n\tEnter Roll Number to search :- "))

    last = trn_attendees[cnt - 1]
    trn_attendees[cnt - 1] = srch
    i = 0
    while(trn_attendees[i] != srch):
        i += 1

    trn_attendees[cnt - 1] = last
    if((i<cnt - 1) or (trn_attendees[cnt-1]== srch)):
        print(f"Student [{srch}] attended the Training Program .")
    else:
        print(f"Student [{srch}] DID NOT attend the Training Program .")


def binarysrch(trn_attendees,srch,first,last):
    

    trn_attendees.sort()

    while first <= last:
        mid = (first + last) // 2

        if trn_attendees[mid] == srch:
            print(f"Student [{srch}] attended the Training Program .")
            break
        elif trn_attendees[mid] < srch:
            first = mid + 1
        else:
            last = mid - 1
    else:
        print(f"Student [{srch}] DID NOT attend the Training Program .")

def fib_srch(trn_attendees,srch,cnt):
    n=cnt
    fibn_2=0
    fibn_1=1
    fibn=fibn_1+fibn_2
    while(fibn<=n):
        fibn_2=fibn_1
        fibn_1=fibn
        fibn=fibn_1+fibn_2

    offset=-1
    while(fibn_1!=0):
        i=min((offset+fibn_2),n-1)
        if(srch>trn_attendees[i]):
            fibn=fibn_1
            fibn_1=fibn_2
            fibn_2=fibn-fibn_1
            offset=i
        elif(srch<trn_attendees[i]):
            fibn=fibn_2
            fibn_1=fibn_1-fibn_2
            fibn_2=fibn-fibn_1
        elif(srch==trn_attendees[i]):
            print(f"Student [{srch}] attended the Training Program .")
            break
    else:
        print(f"Student [{srch}] DID NOT attend the Training Program .")
    


    

#main


trn_attendees,cnt = crt_database()

in_ch = 'y'
while(in_ch=='y' or in_ch == "Y"):
    opt = int(input("\nWhat would you like to perform?\n\t1.Display the Array\n\t2.Search the Roll Number.\n\t3.Enter New Database of Students.\n\t4.Exit.\n\t:- "))
    if(opt==1):
        print(trn_attendees)

    elif(opt==2):

        print("Choose method you want to use for search:- ")
        choose = int(input("\n\t1.Linear Search\n\t2.Sentinel Search\n\t3.Binary Search\n\t4.Fibonnaci Search :-"))
        if choose==1:
            lnrsearch(trn_attendees,cnt)
        elif choose == 2:
            sentinelsearch(trn_attendees,cnt)
        elif(choose==3):
            srch = int(input("Search in Database.\n\tEnter Roll Number to search :- "))
            first = 0
            last = cnt - 1
            binarysrch(trn_attendees,srch,first,last)
        elif(choose == 4):
            srch = int(input("Search in Database.\n\tEnter Roll Number to search :- "))
            fib_srch(trn_attendees,srch,cnt)
            
    elif(opt == 3):
        trn_attendees,cnt = crt_database()

    elif(opt == 4):
        print(" Program Finished ")
        break
    else:
        print("Enter Correct Input!")
        break
    
    print("\nDo you want to run this program again?(y/n)")
    in_ch = input("\t - ")





