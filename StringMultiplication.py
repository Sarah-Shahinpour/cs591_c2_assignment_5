class StringMultiplication():

    def __init__(self): return
    
    #Reference: https://www.geeksforgeeks.org/write-your-own-atoi/
    def stringToInt(self, num):
        result = 0
        for i in range(len(num)):
            result = result * 10 + (ord(num[i]) - ord('0')) #get the ASCII value of the current digit, and then subtract the 0 ASCII value from it to get the integer representation 
        return result
    
    def intToString(self, num):
        reversedStringRep = ""
        stringRep = ""
        while num != 0:
            reversedStringRep += str(num % 10)
            num = num // 10
        for i in range(len(reversedStringRep)-1, -1, -1):
            stringRep += reversedStringRep[i]
        return stringRep

    def multiply(self,num1str, num2str):
        if type(num1str)!=str or type(num2str)!=str:
            return "Strings only accepted"
        num1 = self.stringToInt(num1str)
        num2 = self.stringToInt(num2str)
        product = num1 * num2
        return self.intToString(product)
