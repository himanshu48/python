# Knuth-Morris-Pratt 

class KMP:
	def create_prefix_list(self, pattern):
		prefix = [0]
		for i in range(1, len(pattern)):
			j = prefix[i - 1]
			while j > 0 and pattern[j] != pattern[i]:
				j = prefix[j - 1]
			prefix.append(j + 1 if pattern[j] == pattern[i] else j)
		return prefix
        
	def search(self, text, pattern):
		prefix, res, j = self.create_prefix_list(pattern), [], 0
        
		for i in range(len(text)):
			while j > 0 and text[i] != pattern[j]:
				j = prefix[j - 1]
			if text[i] == pattern[j]:
				j += 1
			if j == len(pattern):
				res.append(i - (j - 1))
				j = prefix[j - 1]
            
		return res



def test():
    p1 = "aa"
    t1 = "aaaaaaaa"

    kmp = KMP()
    assert(kmp.search(t1, p1) == [0, 1, 2, 3, 4, 5, 6])

    p2 = "abc"
    t2 = "abdabeabfabc"

    assert(kmp.search(t2, p2) == [9])

    p3 = "aab"
    t3 = "aaabaacbaab"

    assert(kmp.search(t3, p3) == [1, 8])

    print("all test pass")

test()
