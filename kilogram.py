"""
Pseudocode:
(Use any hashing algorithm you want)

T = array size of bucket_size
for all documents in C
    for n-gram in documents
        q = hash(n-gram) mod bucket_size
        if q mod hashing_stride = 0
          T[q] = T[q+1]

T[k] = QuickSelect(T,k)
S = structure holding B_s buckets
for documents in C
    for ngram in document
        q = hash(ngram) mod bucket_size
        if q in T[k]
           insert ngram into S

return top-k entries from S

## Hashes supported
{'sha384', 'md5', 'sha1', 'blake2s', 'shake_256', 'sha512', 'sha224', 'blake2b', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 'shake_128', 'sha256'}

"""

import math
import os
import hashlib
import QuickSelect

class KiloGram:
	"""
	Base class for KiloGram from the paper. 
	"""

        topk_hashes = list()
        _topk_structure = list()
        

        # Document list, ngram list, bucket, hashing stride
	def __init__(self, docs, ngrams, bucket, stride):
		self.docs = docs
		self.ngrams = ngrams
		self.bucket = bucket
                self.stride = stride

	def bucket_size(self):
		return len(bucket)

	def total_ngrams(self):
		return len(ngrams)

        

	def rollingHash(self):
		for doc in self.docs:
			for gram in ngrams:
				hash = hashlib.sha1(gram.encode())
                                mod_hash = hash % self.bucket_size()
                                if mod_hash % self.stride == 0:
                                        topk_hashes.append(mod_hash)

                # Quickselect T_k from T
                for doc in self.docs:
                        for gram in ngrams:
                                hash = hashlib.sha1(gram.encode())
                                mod_hash = hash % self.bucket_size()
                                if mod_hash in topk_hashes:
                                        _topk_structure.append(mod_hash)
                                        
	def topk_hashes(self):
                # Loop through and get hashes that occur the most
	        
		
		

		

