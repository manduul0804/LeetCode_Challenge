height = [1,8,6,2,5,4,8,3,7]

if (len(height) == 0):
    print("The list is empty")
elif (len(height) == 2):
    size = height[0] if height[0] <= height[1] else height[1]
for i in height:
    print(i)