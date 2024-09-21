newArr = []

def bubble_sort(arr):
    n = len(arr)
    
   
    for i in range(n):
        

        for j in range(0, n-i-1):
            
           
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

def checking(line):
    arrDeString = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, 
                   "six": 6, "seven": 7, "eight": 8, "nine": 9}
    temp = []
    current,smallest, biggest = 0,0,0
    strr = ""
    for key, value in arrDeString.items():
         if key in line:
           start_idx = line.find(key)
           if start_idx != -1 : 
            temp.append((start_idx, key, value)) 
            print(start_idx)
          
           if start_idx > biggest :
               biggest = start_idx
           if start_idx < smallest :
               smallest = start_idx
    temp.sort(key=lambda x: x[0])
    for s , key , value in temp :  
        if(s == 0 or s == biggest) :
            line = line.replace(key,str(value))
       
            
    
    
    
    print(line)
    return line


def sumOfTwoNumbers (line) :
     arr = []
     for char in line :
       if(char.isdigit()) :
         arr.append(char)
         
     return arr[0] + arr[-1]

with open("dayOnePartTwoInp.txt", "r") as file:
    for line in file:
        newLine = checking(line)
        var = sumOfTwoNumbers(newLine)
        newArr.append(int(var))

summ = sum(newArr)
print(summ)
