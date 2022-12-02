# # Write a pythonprogram to store first year percentage of students in array. Write function
# for sorting array of floating point numbers in ascending order using
# a) Selection Sort
# b) Bubble sort and display top five scores

def fe_data():
    num = int(input("Enter Number of Students :- "))
    pt_arr = []
    print("\nEnter the Percentage of Each Student :- ")
    for i in range(num):
        x = float(input(f"{i+1}]"))
        pt_arr.append(x)

    return pt_arr,num

# Selection Sort

def sel_sort(to_sort_arr,cnt):   
    for step in range(cnt):
        min_idx = step

        for i in range(step + 1, cnt):
            if to_sort_arr[i] < to_sort_arr[min_idx]:
                min_idx = i
         
        (to_sort_arr[step], to_sort_arr[min_idx]) = (to_sort_arr[min_idx], to_sort_arr[step])
    return to_sort_arr

# Bubble sort

def bub_sort(to_bub_sort,cnt):
    
    for i in range(cnt):

        for j in range(0, cnt - i - 1):

            if to_bub_sort[j] > to_bub_sort[j + 1]:
                temp = to_bub_sort[j]
                to_bub_sort[j] = to_bub_sort[j+1]
                to_bub_sort[j+1] = temp
    
    return to_bub_sort


#main

fe_percent,cnt = fe_data()

in_ch = 'y'
while(in_ch=='y' or in_ch == "Y"):
    opt = int(input("\nWhat would you like to perform?\n\t1.Display the array\n\t2.Sort the array."
    "\n\t3.Display TOP five Scores.\n\t4.Create New Database\n\t5.Exit current program. :- "))

    if opt==1:
        print("Student Database of Percentage's :- ")
        print(fe_percent)

    elif opt==2:
        choice = int(input("\nHow would you like to sort the inserted array?\n"
                "\n\t1.Selection Sort Method\n\t2.Bubble Sort :- "))
        
        if choice == 1:
            selection_sort=sel_sort(fe_percent,cnt)
            print("The Array is Sorted Using Selection Sort Method :- \n\t",selection_sort)
        elif choice == 2:
            bubble_sort = bub_sort(fe_percent,cnt)
            print("The Array is Sorted Using Selection Sort Method :- \n\t",bubble_sort)

        else:
            print("Enter Correct Option .")

    
    elif opt == 3:
        selection_sort = sel_sort(fe_percent,cnt)
        selection_sort.reverse()
        top_five = selection_sort[0:5]
        print("\nTOP FIVE Percentages of Students :-",top_five)

    elif opt == 4:
        fe_percent,cnt = fe_data()
    
    elif opt==5:
        print("Program Terminated")
        break

    else:
        print("Enter Correct Option.")
        break

    print("\nDo you want to run this program again?(y/n)")
    in_ch = input("\t - ")