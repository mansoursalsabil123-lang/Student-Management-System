grades = [12, 15, 8, 10, 17]
max=grades[0]
min=grades[0]
sum=0
for i in range (0,len(grades)):
    if grades[i]>max:
        max=grades[i]
    elif grades[i]<min:
        min=grades[i]
    sum=sum+grades[i]
print("highest grade : ",max)
print("lowest grade : ",min)
print("average",sum/len(grades))

