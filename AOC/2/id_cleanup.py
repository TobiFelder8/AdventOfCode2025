with open("input_2.txt", "r", encoding="utf-8") as f:
    content = f.read()

ranges = [s.strip() for s in content.split(',') if s.strip()]
invalid_numbers = []

for rg in ranges:
    start, end = rg.split('-')
    start = int(start)
    end = int(end)

    print("Start:", start, end)

    number = start
    while number <= end:
        s = str(number)
        if len(s) % 2 == 0 and s[:len(s)//2] == s[len(s)//2:]:
            invalid_numbers.append(number)
        else:
            L=0
            digits=0
            while L < len(s)//2:
                sdigit = str(digits)
                if str(number)[L] == sdigit[0]:
                    if number[L:L+len(sdigit)] == digits and number % len(sdigit) == 0 and str(number).count(digits) == number / digits:
                        invalid_numbers.append(number)
                L+=1
        number += 1  

    print("Finished:", start, end)

print(invalid_numbers)
print(sum(invalid_numbers))
