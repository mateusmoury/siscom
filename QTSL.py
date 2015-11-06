from queue import Queue
import sys

sys.setrecursionlimit(1000000)


class QTSL:
	#tags: list of strings containing tags id's
	#K = max prefix length (tags length)
	def __init__(self, tags, K=-1):
		self.tags = [{'tag': t, 'active': True} for t in tags]
		self.tags_bits_sum = {} 
		for t in tags:
			self.tags_bits_sum[t] = 0
		if K==-1 and tags.__len__()==0:
			self.K = 0
		elif K==-1:
			self.K = tags[0].__len__()
		else:
			self.K = K
			
	def shortQuery(self, prefix):
		count = 0
		for t in self.tags:
			if t['active'] and t['tag'].startswith(prefix):
				self.tags_bits_sum[t['tag']] += 1
				count+=1
		return count
	
		
	def longQuery(self, prefix):
		tagResult = ""
		for t in self.tags:
			if t['active'] and t['tag'].startswith(prefix):
					self.tags_bits_sum[t['tag']] += t['tag'].__len__()				
					tagResult = t['tag']
		return tagResult
	
	def execute(self, Q, M):
		if Q.empty():
			return M
		prefix = Q.get()
		shortQueryResult = self.shortQuery(prefix)
		if shortQueryResult == 1:
			tag = self.longQuery(prefix)
			self.tags[self.tags.index({'tag':tag, 'active': True})]['active'] = False
			M.append(tag)
		elif shortQueryResult > 1:
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
		bits_sum = 0
		for tag in M:
			bits_sum += self.tags_bits_sum[tag]
			results['tags_results'].append({'tag': tag, 'bits_sum': self.tags_bits_sum[tag]})
		results['bits_sum'] = bits_sum
		results['bits_sum_average'] = float(bits_sum)/float(M.__len__())
		return results







############################ TEST #############################3



if True:
	tags = [
		"010011",
		"100001",
		"010110",
		"011000",
		"000100",
		"010101",											
		"100000",
		"000010",
		"000011",
		"000001",
		"000011",
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


qt = QTSL(tags)

ans = qt.run()

print ("Identificadas:")
print (ans)

	

	
	

			
		
	




