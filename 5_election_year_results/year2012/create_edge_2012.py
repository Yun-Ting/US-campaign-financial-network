import csv

f = open("2012_data.csv")

count = 0
edge_list = []

for line in f:
	if count == 0:
		pass
	else:
		line = line.rstrip()
		words = line.split('\t')
		
		from_name = words[0]
		to_name = words[1]
		amt = words[5]
		edge_list.append([from_name, to_name, int(float(amt)/ 400000)] )
	count += 1


for i in edge_list:
	print (i)


with open('edges.csv', 'w', newline = '\n') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["from_name", "to_name", "amt"])
	for i in edge_list:
		writer.writerow(i)