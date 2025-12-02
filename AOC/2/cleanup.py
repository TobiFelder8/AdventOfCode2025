with open("input_2.txt", "r", encoding="utf-8") as f:
    content = f.read()

ranges = [s.strip() for s in content.split(',') if s.strip()]
invalid_numbers = set()

def is_invalid(num: int) -> bool:
    s = str(num)
    n = len(s)

    for k in range(1, n // 2 + 1):
        if n % k != 0:
            continue
        pattern = s[:k]
        if pattern * (n // k) == s:
            return True
    return False


for rg in ranges:
    start, end = rg.split('-')
    start = int(start)
    end = int(end)

    print("Start:", start, end)

    number = start
    while number <= end:
        if is_invalid(number):
            invalid_numbers.add(number)
        number += 1

    print("Finished:", start, end)

print("Anzahl invalider IDs:", len(invalid_numbers))
print("Summe:", sum(invalid_numbers))
