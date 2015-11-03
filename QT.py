from queue import Queue


class QT:
	def __init__(self, all_tags, max_prefix_length=10):
		self.all_tags = all_tags
		self.max_prefix_length = max_prefix_length

	def colide(self, prefix):
		result = {
			'count': 0,
			'tag': ""
		}
		count = 0 
		for t in self.all_tags:
			if t.startswith(prefix):
				result['tag'] = t
				result['count']+=1
				if result['count'] > 1:
					return result
		return result
		
	def execute(self, Q, M):
		if Q.empty():
			return M
		prefix = Q.get()
		result = self.colide(prefix)
		if result['count'] == 1:
			M.append(result['tag'])
		elif result['count'] > 1:
			if prefix.__len__()+1 <= self.max_prefix_length:
				Q.put(prefix+"0")
				Q.put(prefix+"1")
		return self.execute(Q,M)	

	def run(self):
		if self.max_prefix_length == 0:
			return []
		Q = Queue()
		Q.put("0")
		Q.put("1")
		M = []
		return self.execute(Q, M)







############################ TEST #############################3

tags = ["0", "101", "1", "0111", "1110", "1001", "0000", "111111", "111110", "111100"]
		
qt = QT(tags,10)

ans = qt.run()

print ("Identificadas:")
print (ans)
for t in ans:
	print (t)
	

	
	

			
		
	




