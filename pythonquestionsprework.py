python
Question #1

def hello_name(user_name):
    print("hello_USERNAME!")

    #function calls
    hello_name("USERNAME")

    Question #2
    
    def first_odd():
        for i in range(1, 101):
            if i % 2 == 1:
                print(i)

    Question #3
     
    def max_num_in_list(a_list):
        numbers = [1,100]

        min = numbers[0]
        max = numbers[0]

        fori in range(len(numbers)):
        if numbers[i] > max:
            max = numbers[i]
        elif numbers[i] < min:
            min = numbers[i]

            print("Min:",min)
            print("Max:",max)
            
    Question #4
    
    def is_leap_year(a_year)
    year=int(input("Enter the year:"))
    if (year%400==0) and (year%100==0):
            print(year,"is leap year")

    elif (year%4==0) and (year%100 !=0):
            print(year,"is leap year")

        else:
            print(year,"is not leap year")

        Question #5
        
        def is_consecutive(a_list):
            lst = [2, 3, 1, 4, 5]
            sorted_list = sorted(lst)
            is_consecutive = all(sorted_lst[i] == sorted_lst[i - 1] + 1 for i in range(1, len(sorted_lst)))
            print(is_consecutive)