users = {}				# parent-first degree users list
sub_users = {}			# first-second degree user list
connectedness = {}		# parent users connectedness

for line in open('List100.txt', 'r').readlines():
	x = line.split(', ')							# split each line into three strings
	first_user = x[1].replace(" ", "_")				# replace spaces in usernames with "_" (to comply with gephi format)
	second_user = x[2].replace(" ", "_")			# = = 
	first_user = first_user.replace("\n", "")		# remove redundant line
	second_user = second_user.replace("\n", "")		# = =
	key = first_user+"+"+second_user				# add dict key as first_user+second_user
	
	if first_user != second_user and x[0] == '1':			# if file line contains parent-first degree pair
		if users.has_key(key):								# if parent-first degree pair already stored 		
			users[key] += 1									# increase link value
		else:
			users[key] = 1									# add new parent-first key
			
	if first_user != second_user and x[0] == '2':			# if file line contains parent-child pair
		if sub_users.has_key(key):							# if first-second degree pair already stored 
			sub_users[key] += 1								# increase link value
		else:
			sub_users[key] = 1								# add new first-second key

# Calculate user connectedness
for key, value in users.items():
	key = key.split('+')
	values_first = [u_value for u_key,u_value in users.items() if u_key.startswith(key[0])]			#search for parent-first keys that start with parent
	values_second = [u_value for u_key,u_value in sub_users.items() if u_key.startswith(key[1])]	#search for first-second keys that start with first
	connectedness[key[0]] = sum(values_first) + (0.1*sum(values_second))							# sum to get connectedness 1 for parent-first & 0.1 for first-second
	
connectedness = sorted(connectedness.items(), key=lambda x: (-x[1], x[0]))			# Sort by connectedness

# export connectedness list
con_file = open("100users_connectedness.txt", "w")
for i,j in connectedness:			# print values
	con_file.write("%s	%s\n" %(i, j))
	
con_file.close()

# Get total number of nodes
node_num = len(users)+len(sub_users)

# Save data in Gephi format
# First_node  Seconds_node   Weight
gephi_file = open("Gephi100.dl", "w")
gephi_file.write("dl\nformat = edgelist1\nn = %s\nlabels embedded:\ndata:\n" %node_num)

for key,value in users.items():
	key = key.split('+')
	gephi_file.write("%s %s %s\n" %(key[0], key[1], value))
			
for key,value in sub_users.items():
	key = key.split('+')
	gephi_file.write("%s %s %s\n" %(key[0], key[1], value))

gephi_file.close()