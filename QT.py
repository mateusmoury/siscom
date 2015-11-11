from queue import Queue
import sys

sys.setrecursionlimit(1000000)

class QT:
	#tags: list of strings containing tags id's
	def __init__(self, tags):
		self.tags = [{'tag': t, 'active': True} for t in tags]
		self.tags_bits_sum = {} 
		self.reader_bits_sum = 0 
		self.steps = 0 
		self.num_tags_to_identify = len(tags)
		for t in tags:
			self.tags_bits_sum[t] = 0


	def query(self, prefix):
		result = {
			'count': 0,
			'tag': "",
		}
		count = 0 
		prefix_len = len(prefix)
		for t in self.tags:
			if t['active']:
				self.reader_bits_sum += prefix_len
				if t['tag'].startswith(prefix):
					self.tags_bits_sum[t['tag']] += len(t['tag'])
					result['tag'] = t['tag']
					result['count']+=1
		return result
	
	def execute(self, Q, M):
		if Q.empty() or len(M) == self.num_tags_to_identify:
			return M
		prefix = Q.get()
		self.steps+=1
		queryResult = self.query(prefix)
		if queryResult['count'] == 1:
			tag = queryResult['tag']
			self.tags[self.tags.index({'tag':tag, 'active': True})]['active'] = False
			M.append(tag)
		elif queryResult['count'] > 1:
			Q.put(prefix+"0")
			Q.put(prefix+"1")
		return self.execute(Q,M)	
	
	#Return results, a dictionary containing:
	#	tags_results: Contains all identified tags and how many bits were exchanged to execute their respective identification
	#	bits_sum: Sum of all bits exchanged, same as iterate over tags_results and sum all bits exchanged
	#	bits_sum_average: bits_sum divided by the number of tags identified
	def run(self):
		results = { 'bits_sum': 0, 'bits_sum_average': 0.0 }	
		Q = Queue()
		Q.put("0")
		Q.put("1")
		M = []
		M = self.execute(Q, [])
		bits_sum = 0
		
		for tag in M:
			bits_sum += self.tags_bits_sum[tag]
			#results['tags_results'].append({'tag': tag, 'bits_sum': self.tags_bits_sum[tag]})
		results['bits_sum'] = bits_sum
		results['bits_sum_average'] = float(bits_sum)/float(self.num_tags_to_identify)
		results['reader_bits_sum'] = self.reader_bits_sum
		results['steps'] = self.steps
		return results




############################ TEST #############################3

if __name__ == '__main__':

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
			"001"
		]


	qt = QT(tags)

	ans = qt.run()

	print ("Identificadas:")
	print (ans)

	

	
	

			
		
	



