from queue import Queue


class QT:
	#tags: list of strings containing tags id's
	#K = max prefix length (tags length)
	def __init__(self, tags, K=-1):
		self.tags = [{'tag': t, 'active': True} for t in tags]
		self.K = K
		
	def colide(self, prefix):
		result = {
			'count': 0,
			'tag': "",
			'bits_sum': 0
		}
		prefix_len = prefix.__len__()
		count = 0 
		for t in self.tags:
			if t['active'] and t['tag'].startswith(prefix):
				result['tag'] = t['tag']
				result['count']+=1
				result['bits_sum'] += prefix_len
				if result['count'] > 1:
					return result
		return result
	
	def execute(self, Q, M):
		if Q.empty():
			return M
		prefix = Q.get()
		result = self.colide(prefix)
		if result['count'] == 1:
			tag = result['tag']
			self.tags[self.tags.index({'tag':tag, 'active': True})]['active'] = False
			M.append({'tag': tag, 'bits_sum': result['bits_sum'] })
		elif result['count'] > 1:
			if prefix.__len__()+1 <= self.K:
				Q.put(prefix+"0")
				Q.put(prefix+"1")
		return self.execute(Q,M)	
	
	#Return results, a dictionary containing:
	#	tags_results: Contains all identified tags and how many bits were exchanged to execute their respective identification
	#	bits_sum: Sum of all bits exchanged, same as iterate over tags_results and sum all bits exchanged
	#	bits_sum_average: bits_sum divided by the number of tags identified
	def run(self):
		results = {'tags_results':[], 'bits_sum': 0, 'bits_sum_average': 0.0 }	
		if self.K == 0:
			return results
		Q = Queue()
		Q.put("0")
		Q.put("1")
		M = []
		M = self.execute(Q, [])
		results['tags_results'] = M
		bits_sum = 0
		for tag_result in M:
			bits_sum += tag_result['bits_sum']
		results['bits_sum'] = bits_sum
		results['bits_sum_average'] = float(bits_sum)/float(M.__len__())
		return results







############################ TEST #############################3


tags = [
	"101001",
	"110100",
	"011001",
	"111010",
	"111100",
	"111101"		
]


qt = QT(tags,6)

ans = qt.run()

print ("Identificadas:")
print (ans)

	

	
	

			
		
	




