a = [1,5,2,5,5,6,7]
b = [5,5,6,7,1,5,2]
first_element_idx = None


if len(a) != len(b):
    print("Not circularly identical!")

for i in range(len(a)):
    if b[0] == a[i] and b[1] == a[i+1]:
        first_element_idx = i
        
comparison_results = []


for i in range(first_element_idx, len(a)):
    comparison_result = a[i]==b[i - first_element_idx]
    comparison_results.append(comparison_result)

for i in range(first_element_idx): 
    comparison_result = a[i]==b[len(b) - first_element_idx + i]
    comparison_results.append(comparison_result)

if sum(comparison_results) == len(a):
    print("Is circularly identical!")
else:
    print("Not circularly identical!")
    