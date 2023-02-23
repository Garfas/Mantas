#string_module
# |reverse_string(string), paima eilutę kaip įvestį ir grąžina 
# |atvirkštinę eilutę, naudodama pjaustymo (slicing) sintaksę.
def reverse_string(string):
    return string[::-1]
# |count_vowels(string), kaip įvestį paima eilutę ir grąžina balsių
# | skaičių (tiek mažųjų, tiek didžiųjų raidžių) eilutėje, 
# |naudodama for kilpą ir if sakinį.
def count_vowels(string):
    vowels = "AaEeIiYyOoUu"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count
# |count_consonant(string), kaip įvestį paima eilutę ir grąžina priebalsių
# | skaičių (tiek mažųjų, tiek didžiųjų raidžių) eilutėje, 
# |naudodama for kilpą ir if sakinį.
def count_consonant(string):
    consonant = "BbCcDdFfGgHhJjKkLlMmNnPpRrSsTtVvZz"
    count = 0
    for char in string:
        if char in consonant:
            count += 1
    return count

