def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result


students = [[1, 'Jean castro', 'V'],[2,'Lula Powell','V'],[3,'Brain Howell','VI'],[4,'Lynne foster','VI'],[5,'bob','VI']]

print("\nOriginal list of lists:")
print(students)
print("\n coverted list to dictionary")
print(test(students))