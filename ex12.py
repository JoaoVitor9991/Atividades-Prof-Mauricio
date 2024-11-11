def eh_palindromo(s):
    s = s.replace(" ", "").lower()
    if s == s[::-1]:
        return True
    else:
        return False 
    
print(eh_palindromo("ANA"))
   