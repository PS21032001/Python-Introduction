#finding the count of vowels
vowels = 'aeiou'
take_string = str(input("Input the sentence or word you need to scan."))
take_string = take_string.casefold()
count = {}.fromkeys(vowels, 0)

for char in take_string:
    if char in count:
        count[char] += 1

print (count)
