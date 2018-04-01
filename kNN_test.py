import knn
import kNNo
from numpy import *
import matplotlib
import matplotlib.pyplot as plt

# group , labels = kNN.createDataSet()
#
# res = kNN.classify0([0,0], group, labels, 3)
#
# print res


# datingDataMat, datingLabel = knn.file2matrix('datingTestSet2.txt')
# #
# # print datingDataMat, datingLabel
# #
# # fig = plt.figure()
# # ax  = fig.add_subplot(111)
# # ax.scatter(datingDataMat[:,1], datingDataMat[:,2],
# #            15.0*array(datingLabel), 15.0*array(datingLabel))
# # plt.show()
#
# normMat, ranges, minVals = knn.autoNorm(datingDataMat)
# print normMat
# print ranges
# print minVals

knn.handwritingClassTest()