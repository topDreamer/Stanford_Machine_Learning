## Tips

1. sklearn里面的SVM使用的是libsvm，其中kernel有‘linear’：线性函数，‘poly’：多项式函数，‘rbf’：高斯核函数，‘sigmoid’：sigmoid函数，‘precomputed’：已经计算过了，‘callable’：自己写的函数，默认为rbf
2. ‘ovr‘：训练k个分类器，’ovo‘：训练k(k-1)/2个分类器，使用投票数量最多的作为最后结果
3. sklearn里面的模型基本都是使用fit来进行数据训练，然后使用predict来进行预测
4. python的正则与octave不同，其中有些符号需要添加转义字符\

## 感受

在机器学习的实践中，数据不是直接就可以获取的，需要通过特征工程来进行数据清洗。在数据整理的过程之中需要对于目标选取合适的方法来进行处理，在本次实验中就需要使用正则来对文本进行简单处理，进而抽象成为数字特征，在进行自然语言处理的时候，还会对于单词进行化简，防止过多的特征扰乱训练导致过拟合。

在kernel函数选择的时候，线性核函数最简单，但是直接使用rbf核函数可以最终优化到线性函数的程度，但是需要调整系数。