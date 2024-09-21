arrDeString = ["one","two","three","four","five","six","seven","eight","nine"]
newArr = []
def sumOfTwoNumbers (line) :
     arr = []
     for char in line :
       if(char.isdigit()) :
         arr.append(char)
         
     return arr[0] + arr[-1]
       
           
    
with open("dayOneInput.txt","r") as file : 
      for line in file : 
       var = sumOfTwoNumbers(line)
       newArr.append(var)       
                   
     
summ = 0;
for test in newArr :
    summ += int(test);             
                   
     
                   
print(summ)


     
    
                   
               