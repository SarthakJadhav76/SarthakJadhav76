#Write a python program to store First Year Percentage of student in array .
#Write a function for sorting array of floating points numbers in ascending order 
# using quick sort and display top five scores.



def fe_data():
    num = int(input("Enter Number of Students :- "))
    pt_arr = []
    print("\nEnter the Percentage of Each Student :- ")
    for i in range(num):
        x = float(input(f"\t{i+1}] "))
        pt_arr.append(x)

    return pt_arr,num

def quick_sort(to_sort,start,end):
    if(start<end):
        m = divide_arr(to_sort,start,end)
        quick_sort(to_sort,start,m-1)
        quick_sort(to_sort,m+1,end)

    return to_sort

    

def divide_arr(to_sort,start,end):
    pivot = to_sort[start]
    p = start + 1
    q = end
    flag = False
    while(not flag):
        while(p<=q and to_sort[p] <= pivot):
            p += 1
        while(p<=q and to_sort[q]>=pivot):
            q = q-1

        if(q<p):
            flag = True
        else:
            temp = to_sort[p]
            to_sort[p] = to_sort[q]
            to_sort[q] = temp

    temp = to_sort[start]
    to_sort[start] = to_sort[q]
    to_sort[q] = temp

    return q

#main

fe_percent,cnt = fe_data()

in_ch = 'y'
while(in_ch=='y' or in_ch == "Y"):
    opt = int(input("\nWhat would you like to perform?\n\t1.Display the array\n\t2.Sort the array using"
    " Quick Sort.\n\t3.Display TOP five Scores.\n\t4.Create New Database\n\t5.Exit current program. :- "))

    if opt==1:
        print("\nStudent Database of Percentage's :- ")
        print(fe_percent)

    elif opt==2:
        print("\nThe Unsorted array is :- \n\t",fe_percent)
        sorted_arr = quick_sort(fe_percent,0,cnt-1)
        print("\nThe Sorted Array is :- \n\t",sorted_arr)
        
    elif opt == 3:
        sorted_array = quick_sort(fe_percent,0,cnt-1)
        sorted_array.reverse()
        if cnt<5:
            top_students = sorted_array
            print("\nTOP  Percentages in First Year Engineering :-",top_students)
        else:
            top_five = sorted_array[0:5]
            print("\nTOP FIVE Percentages in First Year Engineering :-",top_five)


    elif opt == 4:
        fe_percent,cnt = fe_data()
    
    elif opt==5:
      print("...Program Successfully Terminated...")
      in_ch == 'n'
      break

    else:
        print("!!! Wrong Input !!!")
        break
    
    if in_ch != 'n':
      print("\nDo you want to run this program again?(y/n)")
      in_ch = input("\t - ")
      
