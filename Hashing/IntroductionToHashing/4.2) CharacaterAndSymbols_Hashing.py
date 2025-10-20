s = "@#$%&*AABBBCCCDabcdabcd11223455666"
q = [
    "@",
    "&",
    "#",
    "$",
    "%",
    "A",
    "B",
    "C",
    "D",
    "a",
    "b",
    "c",
    "d",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
]

hash_list = [0] * 128

for char in s:
    ascii_value = ord(char)
    hash_list[ascii_value] += 1
for x in q:
    ascii_value = ord(x)
    print(f"Frequency of {x}: ", hash_list[ascii_value])
