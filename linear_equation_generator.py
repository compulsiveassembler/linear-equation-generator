

#function takes input string and splits it into a list of floats, according to where the chars are seperated by whitespace
#Example) the numbers '341234 321' are several chars but only two numbers, so we seperate them and convert them as such

def get_pairs():

    print("Enter your ordered pairs, (a,b) (c,d), in the following format: a b c d")
    print("Entering anything but signed numbers and whitespace will end program")
    print("Do not enter more than two ordered pairs (four numbers), entering more will end the program")
    print("Enter here: ", end=' ')

    input_string = input()  #ordered pairs to be converted
    ordered_pairs = []      #ordered pairs stripped from input are stored here as floats, and are passed off to be used
    whitespace_index = []   #stores the position of whitespace in input string, which seperates numbers. Also stores the first and last position in the string.

    
    whitespace_index.append(0)  #marks start position of first slice at beginning of string. This slice will range from 0 to position of first whitespace

    #loops through string, ignoring characters and indexing whitespace
    for i in range(0, len(input_string)):

        if input_string[i] == ' ':
            whitespace_index.append(i)
        else: continue
    
    whitespace_index.append(len(input_string))  #marks last index position, which allows slice from last whitespace to end of string 


    #takes slices of all characters seperated by whitespace, as all the characters between whitespace represent a single number.
    #Converts this slice of chars to a float                                            
    for k in range(0, len(whitespace_index)):
        
        #converts first number as float from start of string 0 to position of first whitespace
        if whitespace_index[k] == 0:
            try:
                ordered_pairs.append(float(input_string[0:whitespace_index[k+1]].strip()))
            except: 
                print("Invalid input!")
                quit()
            else:
                continue
            
        
        #converts last number in input_string from slice marked by last whitespace (k-1) and the last position in string (k)
        elif whitespace_index[k] == len(input_string):
            try:
                ordered_pairs.append(float(input_string[whitespace_index[k-1]:whitespace_index[k]].strip())) 
            except:
                print("Invalid input!")
                quit()
            else:
                continue
           
        elif whitespace_index[k+1] == len(input_string):
            continue

        #takes slice of string from whitespace to next whitespace, and converts it to a single float number. This accounts for 
        #everything the first and last number
        else:
            try:
                ordered_pairs.append(float(input_string[whitespace_index[k]:whitespace_index[k+1]].strip())) 
            except:
                print("Invalid input!")
                quit()
            else:
                continue
              
    #tests if quantity of numbers is valid. Quits if invalid.
    if len(ordered_pairs) != 4:
        print("Invalid number of inputs!")
        quit()
        

    return ordered_pairs



#converts ordered pairs to slope using (Y2-Y1)/(X2-X1). This result is checked for errors and rounded to 4 decimal places
#Appends the slope to the list containing the ordered pairs, so that it can be popped off and used when constructing equation

def slope_calculator():
    pairs = get_pairs()
    slope = 0.0

    try:
        slope = round((pairs[3] - pairs[1])/(pairs[2]-pairs[0]), 3)
    except ZeroDivisionError:
        print("Zero by division error, input cannot be expressed as a linear function!")
        quit()
    else:
        pairs.append(slope)
    
    return pairs
    

#takes list of slope and ordered pairs and generates a slope-intercept form equation using the point slope formula.
#For reference, the point slope formula is y-y1 = m(x-x1). Slope-intercept form is y = mx + b

def linear_equation_generator():
    
    #pulls from slope_calculator, which itself immediately pulls from get_pairs()
    #pairs_and_slope[4] == slope, the previous four elements are the numbers themselves
    pairs_and_slope = slope_calculator()

    #calculates intercept b from b = -mx1 + y1
    intercept = round(-pairs_and_slope[4]*pairs_and_slope[0] + pairs_and_slope[1], 3)
    print(f"y = {pairs_and_slope[4]}x + {intercept}")
   
   

    

#PROGRAM STARTS HERE
linear_equation_generator()

