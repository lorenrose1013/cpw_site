import json

f = open("sched.csv", "r")
sched = f.readlines()
f.close()
#print sched
#print str(len(sched))

#make json for graph

sched_dict = {
	"name": "CPW Schedule",
	"children" : [
		{	"name": "APRIL 7th",			
			"children": []},				
		{	"name": "APRIL 8th",
			"children" : []},
		{	"name": "APRIL 9th",
			"children": []},
		{	"name": "APRIL 10th",
			"children": []}
	]
}
for j in range(4):
 	for i in range(24):
 		sched_dict["children"][j]["children"].append( {	"name": (str(i) + ":00 ") ,
 														"children" : []	} )


for event in sched:
	split = event.split(",")
	startString = split[0]
	startTime = int(split[0][6:8])
	endTime = int(split[1][6:8])
	eventName = split[2]
	startDate = 0
	if ("APR07" in startString):
		startDate = 0
	elif("APR08" in startString):
		startDate = 1 
	elif("APR09" in startString):
		startDate = 2
	else:
		startDate = 3
	sched_dict["children"][startDate]["children"][startTime]["children"].append(
		{	"name" : eventName,
			"size" : str(abs(endTime - startTime))  }
		)


json_string = json.dumps(sched_dict)
#print sched_dict
f = open("json_cpw.json", "w")
f.write(json_string)
f.close()