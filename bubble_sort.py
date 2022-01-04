#specify the array
array=[9,2,0,3,1,7,6]
length=len(array)-1 	#get the length of the array
print(array)

for j in range(0,length):
	for i in range(0,length):
		if array[i]>array[i+1]:
			array[i],array[i+1]=array[i+1],array[i]
	length=length-1
print(array)