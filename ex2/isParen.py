class Parenthesized:
    def isValid(self, s):
        pastParens = []
        for i in range(len(s)):
            # pastParens = ['{', '[', '(']
            if self.isAlphanumeric(s[i]):
                continue
            #checking for three possible open parens cases ['{', '[', '(']
            if self.isOpenParen(s[i]):
                pastParens.append(s[i])
            #No more open parens, switching to close then compare for properly parenthesized               
            else:
                if len(pastParens) == 0:
                    return False
                #compare open and close
                op = pastParens.pop()
                cl = s[i]
                isValid = self.parenIsSameType(op, cl)
                if not isValid:
                    return False
        return len(pastParens) == 0

    def isOpenParen(self, p):
        if p == '(' or p == '[' or p == '{':
            return True
        return False

    def parenIsSameType(self, op, cl):
        if op == '(' and cl == ')':
            return True
        elif op == '[' and cl == ']':
            return True
        elif op == '{' and cl == '}':
            return True
        else:
            return False
    
    def isAlphanumeric(self,p):
        if p.isalnum():
            return True
        return False

p = Parenthesized()
print("")
print('empty string')
print(p.isValid(''))
print("")
print('{[()]}')
print(p.isValid('{[()]}'))
print("")
print('{]')
print(p.isValid('{]'))
print("")
print('pq')
print(p.isValid('pq'))
print("")
print('()()')
print(p.isValid('()()'))
print("")
print('{p(gh)}')
print(p.isValid('{p(gh)}'))
print("")
print('p{()}q')
print(p.isValid('p{()}q'))
print("")
print('1')
print(p.isValid('1'))
print("")
print(';')
print(p.isValid(';'))


