import json

ind_to_com_file = open('ind_to_com.csv')
com_to_can_file = open('com_to_can.csv')
out_file = open('data.json', 'w')


out_dict = {"nodes": [], "links": []}
indv_list = []

for line in ind_to_com_file:
	word = line.split('\t')
	indv = word[2]
	try:
		amt = int(word[1])
		if amt > 50000:
			if indv not in indv_list:
				indv_list.append(indv)
				
	except Exception as e:
		pass

com_list = []
for line in com_to_can_file:
	word = line.split('\t')
	com = word[2]
	try:
		amt = int(word[1])
		if amt > 50000:
			if com not in com_list:
				com_list.append(com)
	except Exception as e:
		pass

ind_to_com_file.close()
com_to_can_file.close()

ind_to_com_file = open('ind_to_com.csv')
com_to_can_file = open('com_to_can.csv')

## write nodes into dictionary
for person in indv_list:
	out_dict["nodes"].append({
			"id": person,
			"group": 1
		})

for com in com_list:
	out_dict["nodes"].append({
			"id": com,
			"group": 2
		})

out_dict["nodes"].append({
		"id": "OBAMA, BARACK",
		"group": 3
})

out_dict["nodes"].append({
		"id": "ROMNEY, MITT / RYAN, PAUL D.",
		"group": 3
})


######## CREATE LINKS ########

for line in ind_to_com_file:
	word = line.split('\t')
	indv = word[2]
	com = word[3].rstrip()
	if indv in indv_list and com in com_list:
		out_dict["links"].append({
					"source": indv,
					"target": com,
					"value": amt
					})

for line in com_to_can_file:
	word = line.split('\t')
	com = word[2]
	can = word[3].rstrip()
		
	# create links
	if com in com_list:
		out_dict["links"].append({
				"source": com,
				"target": can,
				"value": amt
		})

# LINKS
json.dump(out_dict, out_file)

ind_to_com_file.close()
com_to_can_file.close()
out_file.close()

