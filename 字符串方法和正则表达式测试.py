# 字符串方法和正则表达式测试

import re

sample_1 = '&ldquo;明天就知道了.&rdquo;'
print(sample_1)
# text = sample_1.replace('[a-z&!;]+', ' ')
# 提取中文的正则 '&+;+[a-z]+'
text1 = re.sub('[a-z]+', '', sample_1).strip('&.;')
print(text1)
text2 = re.findall(';(.*?)\.', sample_1)
print(text2)
text3 = re.sub('.', '', sample_1).strip('&.;')