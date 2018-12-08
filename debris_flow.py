grid_start = ["F", "C"]
grid_element = []
time_interval = []
floodplain_discharge = []

original_inflow = open('INFLOW.DAT', 'r')

number = 0
for line in original_inflow:
	if grid_start[0] in line or grid_start[1] in line:
		number += 1
		grid_element.append([line])
		print grid_element[number - 1]
		print len(grid_element)
	elif len(grid_element) == 0:
		inflow_start = line
	else:
		temp_line = line.split()
		for x in range(len(temp_line)):
			if x == 1:
				if len(time_interval) == 0:
					#print temp_line[x]
					time_interval.append([temp_line[x]])
				else:
					#print len(time_interval[number - 1])
					time_interval[number - 1].append([temp_line[x]])
			elif x == 2:
				if len(floodplain_discharge) == 0:
					#print temp_line[x]
					floodplain_discharge.append([temp_line[x]])
				else:
					#print temp_line[x]
					floodplain_discharge[number - 1].append([temp_line[x]])

print len(grid_element)
print len(time_interval)
print len(floodplain_discharge)
print number
raw_input("Press ENTER key to continue.")
