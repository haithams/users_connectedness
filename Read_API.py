import mwclient								#import mwclient library
import io									#import io utf file read/write library
site = mwclient.Site('en.wikipedia.org')	#define wikipedia site as English Wikipedia

user_list = []				# empty user list
hash_list = [] 				# repeated user list	
count = 0					# counter
cohort_size = 100  			#size of user cohort		

# Get User Talk Pages
for page in site.allpages(namespace = 3): 		#iterate over all pages in namespace 3, user talk pages
	user_list.append(page.name)					#add new pages
	count += 1									#increase counter
	if count == cohort_size:    				#stop when equals to cohort size
		break


# write data to file
text_file = io.open("List100.txt", "w", encoding='utf8')

	
for user in user_list:								#iterate over user list
	page = site.Pages[user]							#get user talk page
	user_name = page.name[10:]    					#Assign user name without "User Talk:"
	print page.name[10:]			
	
	for revision in page.revisions():				#iterate over all revisions of page
		text_file.write("1, %s, %s\n" %(user_name, revision['user']))	#write line with parent-child connection
		sub_page_name = 'User talk:' + revision['user']					#get full child page name
		
		if revision['user'] not in hash_list:							# if first time loaded
			hash_list.append(revision['user'])							# build loaded user list
			sub_page = site.Pages[sub_page_name]						#get child page
			
			for sub_revision in sub_page.revisions():							#get child page revisions
				if sub_revision.has_key('userhidden') is True:   				#ignore if edit is hidden	
					continue
				text_file.write("2, %s, %s\n" %(revision['user'], sub_revision['user']))	#write line with child-grandchild connection
text_file.close()

