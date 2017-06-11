def radix_s_msd(L, i):
	if len(L) <= 1:
		return L

	bucket_f = []
	buckets = []
	for j in range(27):
		buckets.append([])

	for j in L:
		if i >= len(j):
			bucket_f.append(j)
		else:
			buckets[ord(j[i]) - ord('a')].append(j)

	bucket_t = []
	for j in buckets:
		bucket_t.append(radix_s_msd(j, i+1))
	buckets=bucket_t

	bucket_t = []
	for blist in buckets:
		for b in blist:
			bucket_t.append(b)

	return bucket_f + bucket_t

L = ['copper', 'explain', 'truck', 'neat', 'unite', '', 'branch', 'z', 'hum', 'humm']
L = radix_s_msd(L, 0)
print("In Alphabetical Order: ")
print L
