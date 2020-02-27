import math
import os
import sys
from kilogram import KiloGram



documents = list()
ngrams = list()
bucket = list()
stride = 2
lipsum = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"]


ngrams_2 = ["no", "on", "or", "mo", "ut", "la", "do", "ed", "ei"]

'''
First phase - KiloGram finds the top k hashes for some corpora. Once the top k hashes are found we can then encode the bucket numbers of the top hashes into a matrix for a quantum computer to use.

Second phase  - This is where we would replace part of the KiloGram algorithm with Grovers Algorithm to do a linear search on this unsorted data (Grovers does not do as well on sorted data). 
'''


kg = KiloGram(lipsum, ngrams_2)

topk_hashes = kg.rollingHash()

print("\n==== TOP K HASHES / N-GRAMS =====\n")
print("----- hash(crc32)    :    n-gram -----\n")
for key in topk_hashes:
    print(str(key) + "    :    " + topk_hashes[key])

print()





