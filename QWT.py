from queue import Queue
from math import exp
import sys
 
sys.setrecursionlimit(1000000)
 
 
 
class QWT (object):

	def __init__(self, tags, BETHA=0.5, TAGS_LEN=96):
		self.tags = [{'tag': t, 'active': True} for t in tags]
		self.num_tags_to_identify = len(tags)
		self.BETHA = BETHA
		self.TAGS_LEN = TAGS_LEN
		self.num_tags_to_identify = len(self.tags)


	def reset(self):
		aux = self.tags
		self.tags = [{'tag': t['tag'], 'active': True} for t in aux]
		self.bits_sum = 0
		self.reader_bits_sum = 0
		self.count_tags_to_identify = 0
		self.steps = 0		
		self.go_on_slots = 0		
	
 
	def F(self, L):
		return self.TAGS_LEN*(1 - exp(-self.BETHA*L) )

	def next_ws(self, last_ws, last_L, last_T, L, first):
		if first:
			return 1
		if last_T==1 and last_L < L:
			return self.F(L)
		if last_T!=1 and last_L < L:
			return last_ws
		return 1
       
	def query(self,prefix, ws):
		result = {
		        'count': 0,
		        'ws_bits': ""
		}
		self.reader_bits_sum += len(prefix)
		for t in self.tags:
			if t['active']:
				if t['tag'].startswith(prefix):
					result['count']+=1
					result['ws_bits'] = t['tag'][ws:]
					self.bits_sum += ws
		return result

	def go_on(self, prefix):
		prefix_len = len(prefix)
		tag = ""
		for t in self.tags:
			if t['active']:
				self.go_on_slots += 1					
				self.reader_bits_sum += prefix_len
				if t['tag'].startswith(prefix):
					self.bits_sum += len(t['tag'])
					tag = t['tag']
		return tag
       
	def call(self, prefix, last_ws, last_L, last_T, first = False):
		if self.count_tags_to_identify >= self.num_tags_to_identify:
			return {}
		self.steps += 1
		L = len(prefix)
		ws = self.next_ws(last_ws, last_L, last_T, L, first)
		query_result = self.query(prefix, ws)
		last_result = {'ws': ws, 'L': L, 'count': query_result['count'] }
		if query_result['count'] == 1:
			tag_identified = 0 # initialized with garbage
			if L+ws < self.TAGS_LEN:
				tag_identified = self.go_on(prefix + query_result['ws_bits'])
			else:
				tag_identified = prefix+query_result['ws_bits']
			self.count_tags_to_identify += 1
		elif query_result['count'] > 1:
			last_result = self.call(prefix+'0', ws, L, query_result['count'])
			if self.count_tags_to_identify < self.num_tags_to_identify:			
				last_result = self.call(prefix+'1', last_result['ws'], last_result['L'], last_result['count'])
		return last_result 
		
		
	#Return results, a dictionary containing:
	#	tags_results: Contains all identified tags and how many bits were exchanged to execute their respective identification
	#	bits_sum: Sum of all bits exchanged, same as iterate over tags_results and sum all bits exchanged
	#	bits_sum_average: bits_sum divided by the number of tags identified
	#   reader_bits_sum: bits sended by the reader to identify all tags
	#
	#   steps: number of steps computed to identify all tags
	#   go_on_slots: number of go_on slots sended by the reader     
	def run(self):
		self.reset()
		last_result = self.call('0', -1, -1, -1, True )
		self.call('1', last_result['ws'], last_result['L'], last_result['count'])
		return {'bits_sum': self.bits_sum, 'reader_bits_sum': self.reader_bits_sum, 'steps': self.steps, 'go_on_slots': self.go_on_slots} 








############################################ TEST #############33
if __name__ == '__main__':
	tags = [] 
	if True:        
		if True:
			tags = [
				"010011",
				"100001",
				"010110",
				"011000",
				"010101",											
				"100000",
				"000010",
				"000011",
				"000001",
				"000101",
				"000100",
				"000110",
				"000111",			
			]	
		else:
			tags = [
				"000",
				"001",
				"010",
				"011",
				"100",
				"101",		
			]
	else:
		with open('teste', 'r') as f:
			for line in f:
				line = line[:-1]
				tags.append(line)
	
	#print(tags)	
	if True:
		boy = QWT(tags, 0.5, len(tags[0]) )	
		ans = boy.run()
		print("-----------------\n"+str(ans))
	
