def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
            return count

def count_consonants(s):
    count =  0
    for ch in s:
       if ch.isalpha() and ch not in "aeiouAEIOU":
           count += 1
           return count
        
        
def vowel_consonant_ratio(vowels,consonants):
    if consonants == 0:
        return "Undefined (no consonants)"
        return vowels / consonants

#main prog
string = input("Enter a string: ")
c = count_consonants(string)
v = count_vowels(string)

print("Vowels:",v)
print("Consonants:",c)
print("Ratio:",vowel_consonant_ratio(v,c))


        
    
