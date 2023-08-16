print("this program is used to generate an array with a specif length generate an array") 
print("of a specific length filled with integer numbers increased by one from start.")
def gen_arr(length, start):
    gen_arr=[]
    element= start
    for i in range(length):
        gen_arr.append(element)
        element += 1
    return(gen_arr)
        
length= int(input("Enter the length of the array: "))
start= int(input("Enter the starting number in the array: "))

gened_arr = gen_arr(length, start)
print("Generated array: ", gened_arr)