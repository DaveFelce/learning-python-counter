from in_out.file import Read
from collections import Counter

file = Read()

nums = file.read_lines('/Users/davidfelce/test.file')[0]
cnt = Counter(nums)
mc_list = cnt.most_common(2)
d = {k:v for k,v in (t for t in mc_list)}
for key in sorted(d.keys(), reverse=True):
    print(str(key) + ": " + str(d[key]))

