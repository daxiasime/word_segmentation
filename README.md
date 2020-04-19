# word_segmentation
【NLP】基于DP算法的中文分词系统(Incorporate Semantic )

目前是第一个版本,依然存在很多问题.正在慢慢完善.

该系统的流程如上图所示。首先，将原始文本，通过正则表达式根据非中文字符进行拆分。得到一个句子的列表，然后分别对每一个句子进行分词处理。

对于单个句子，首先进行按照不同的字长进行划分，如单字，双字和三字等等放入汉字列表并去除重复元素。

加载词库，将获得的汉字列表，在词库中进行匹配. 如果存在,则将权值设置为字频的倒数.存入字典中,格式如下{‘我’:1/f,’去一’:1000}.下面以句子中每一个单词为结点以字典为对应权值建立有向网.

找到从开始到结束的最短路径就是分词结果.

[测试用例]:

句子:经常有意见分歧

字典={"经常":2.3, "经":3, "有":2.3, "有意见":2.3,"意见":1.6,"分歧":1.6,"见":3,"意":3,"见分歧":3, "分":2.3,"我":1.6}

结果为 [‘经常’,’有意见’,’分歧’].
