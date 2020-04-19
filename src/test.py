# test.py
import pandas,numpy,math

def load_ciku_2(self):
	data=pandas.read_csv("../res/CorpusWordlist.csv",sep='\t')
	data_=numpy.array(data)
	# print("加载词库....")
	dic=[x[0].split(',')[1::2] for x in data_[0:]]
	print(dic[:3])
	dic={x[0]:-math.log(eval(x[1])/100) for x in dic}
	# print("解析完成..")
	return dic
