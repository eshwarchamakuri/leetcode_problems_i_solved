class Solution:
    def interpret(self, command: str) -> str:
        s=""
        for i in range(len(command)-1):
            if command[i]=='(' and command[i+1]==')':
                s+='o'
            elif command[i].isalpha():
                s+=command[i]
        if command[len(command)-1].isalpha():
            s+=command[len(command)-1]
        return s