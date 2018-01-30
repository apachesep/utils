'''
for Google App Engine Standard Env
from google.appengine.api import urlfetch
'''

def cookie(data):
	cookies = ''
	for x in range(0,len(data.split(', ')),2):
		tir1 = data.split(', ')[x]
		tir2 = tir1.split('; ',1)[0]
		cookies += tir2+'; '
	cookies = cookies[:-2]
	return cookies
