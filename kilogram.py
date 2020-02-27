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
import binascii
from quickselect import QuickSelect

class KiloGram:
        """
        Base class for KiloGram from the paper. 
        """
        _bucket_size = (2**31) - 19
        # Dictionary / hash table for hash / n-gram
        _topk_hashes = list()
        topk_hash_table = dict()

        # Document list, ngram list, bucket, hashing stride
        # stride = n/4 - i.e 2-gram = 2/4
        # bucket size = 2^31 - 19 = largest prime for array size  allowed
        def __init__(self, docs, ngrams, bucket=None, stride=None):
            self.docs = docs
            self.ngrams = ngrams
            self.bucket = bucket
            self.stride = stride

        def rollingHash(self):
            ''' 
            Using CRC32 in binascii
            '''
            hashes = list()
            for doc in self.docs:
                for gram in self.ngrams:
                    #print(gram)
                    # Must be bytes like object
                    curr_hash = binascii.crc32(str.encode(gram))
                    #print(curr_hash)
                    # Bucket size is 2^31 -19 = 2147483629
                    mod_hash = curr_hash % self._bucket_size
                    #print(mod_hash)
                    #print(len(gram))
                    self._stride = math.ceil(len(gram) / 4)
                    if mod_hash % self._stride == 0:
                        hashes.append(mod_hash)

            # Quickselect T_k from T
            # Get topk hashes and append to list
            qs = QuickSelect()
            #print(len(hashes))
            #print(hashes)
            
            # Top 5 hashes
            for i in range(5):
                if i == 0:
                    continue
                else:
                    self._topk_hashes.append(qs.kFindMost(hashes,i))
                
            for doc in self.docs:
                for gram in self.ngrams:
                    # Must be bytes like object
                    curr_hash = binascii.crc32(str.encode(gram))
                    # Bucket size is 2^31 -19 = 2147483629
                    mod_hash = curr_hash % self._bucket_size
                    if mod_hash in self._topk_hashes:
                        self.topk_hash_table[mod_hash] = gram

            return self.topk_hash_table


            
        
        

        

