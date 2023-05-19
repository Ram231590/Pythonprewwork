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
        return max(a_list)
    print(max_num_in_list([1,2,3,4,5,6,7]))

        
    Question #4
    def is_leap_year(a_year):
            if a_year % 400 == 0:
                return True
            
            else:
                return False
            print(is_leap_year(2000))
 
  
    Question #5
    
    def is_consecutive(a_list):
        return sorted(a_list) == list(range(min(a_list), max(a_list) + 1))
    print(is_consecutive([0, 1, 2, 3, 4, 5]))
        
            

            
            
            


        
