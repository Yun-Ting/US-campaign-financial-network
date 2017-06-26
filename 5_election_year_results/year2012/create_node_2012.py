import csv

f = open("2012_data.csv")
node_dict = {}
count = 0
for line in f:
	if count == 0:
		pass
	else:
		line = line.rstrip()
		words = line.split('\t')
		
		from_name = words[0]
		to_name = words[1]
		from_aff = words[2]
		to_aff = words[3]
		
		if from_name not in node_dict and to_name in node_dict:
			node_dict[from_name] = from_aff
		elif to_name not in node_dict and from_name in node_dict:
			node_dict[to_name] = to_aff
		elif to_name not in node_dict and from_name not in node_dict:
			node_dict[to_name] = to_aff
			node_dict[from_name] = from_aff
	count += 1

for k, v in node_dict.items():
	print (k, '\t' ,v)

print (len(node_dict))

with open('nodes.csv', 'w', newline = '\n') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["id", "aff", "type"])
	for k, v in node_dict.items():
		writer.writerow([k, v])