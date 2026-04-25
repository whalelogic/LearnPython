
results = []

def sum(a: int, b: int) -> int:
    return a + b


def sum_all(*numbers: int) -> int:
    sum = 0
    for n in numbers:
        sum += n
    return sum


def sum_list(nums: list[int]) -> int:
    s = 0
    for i in nums:
        s += i
    return s


print(f"Sum all (1-5): {sum_all(1, 2, 3, 4, 5)}")
print(f"Sum all (1-10): {sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")

print(f"Sum (4, 3): {sum(4, 3)}")

temp_list = [1, 3, 5, 7, 9]

print(f"Sum list ([6-10]): {sum_list([6, 7, 8, 9, 10])}")
print(f"Sum list slice: {sum_list(temp_list[0:3])}")
print()

for i in range(len(temp_list)):
    index = i
    print(f"Index: {i} Value: {temp_list[i]}")
    results.append(temp_list[i])

print(f"Results list: {results}")


for o in temp_list:
    print(f"Value: {o}")

r = [r ** r for r in results if r % 2 == 1]
print(f"Powers list: {r}")

print(f"9**9 value: {9**9}")

