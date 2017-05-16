from numpy import *
from numpy import linalg as la
def loadExData():
    return[[0, 0, 0, 2, 2],
           [0, 0, 0, 3, 3],
           [0, 0, 0, 1, 1],
           [1, 1, 1, 0, 0],
           [2, 2, 2, 0, 0],
           [5, 5, 5, 0, 0],
           [1, 1, 1, 0, 0]]

Data = loadExData()
U, Sigma, VT = la.svd(Data)
#print U
print Sigma
'''
[  9.64365076e+00   5.29150262e+00   9.99338251e-16   4.38874654e-16
   1.19121230e-16]
 '''
#print VT
# ����ԭʼ����� ֻʹ��ǰ����
Sig3 = mat([[Sigma[0], 0, 0],[0, Sigma[1], 0],[0, 0, Sigma[2]]])
temp = U[:,:3]*Sig3*VT[:3,:]
print temp
����Ϊʲô��װ������ԭ���ľ�����? 


import numpy as np
b= np.mat(np.arange(20).reshape(4,5))
print(b)
print(b[1:3,2:5])   # ��ȡ��һά���±�Ϊ1,2��2���֣���ȡ�ڶ�ά���±�Ϊ2,3,4��3����
print(b[:2,2:])     # ͬ��ǰ�治д��ͷ��ʼ�����治дһֱ��ĩβ
print(b[:2,3])      # ��Ȼ��Ҳ������ĳά����ֻȡһ��
�Ծ��������Ƭ�����к��е��������ϱ�ʾ, �м���,�Ÿ���


from numpy import *
from numpy import linalg as la

# ŷʽ����ļ��� (0,1]
def euliSin(inA, inB):
    return 1.0/(1.0 + la.norm(inA - inB))
# Ƥ��ѷ���ϵ�� (0,1]
def pearsSim(inA, inB):
    if len(inA) < 3 : return 1.0
    return 0.5 + 0.5*corrcoef(inA, inB, rowvar=0)[0][1]
# �������ƶ� (0,1]
def cosSim(inA, inB):
    num = float(inA.T*inB)
    denom = la.norm(inA)*la.norm(inB)
    return 0.5 + 0.5*(num/denom)

def loadExData():
    return[[0, 0, 0, 2, 2],
           [0, 0, 0, 3, 3],
           [0, 0, 0, 1, 1],
           [1, 1, 1, 0, 0],
           [2, 2, 2, 0, 0],
           [5, 5, 5, 0, 0],
           [1, 1, 1, 0, 0]]
myMat = mat(loadExData())
print euliSin(myMat[:,0], myMat[:,4]) #0.129731907557
print euliSin(myMat[:,0], myMat[:,0]) #1.0

print pearsSim(myMat[:,0], myMat[:,4]) #0.205965381738
print pearsSim(myMat[:,0], myMat[:,0]) #1.0

print cosSim(myMat[:,0], myMat[:,4]) #0.5
print cosSim(myMat[:,0], myMat[:,0]) #1.0
��֪�������ĸ���׼ȷ�����������ٶ����

print myMat[2, :]  # [[4 0 0 1 1]]
print nonzero(myMat[2, :].A==0) #(array([0, 0], dtype=int64), array([1, 2], dtype=int64))
print nonzero(myMat[2, :].A!=0) #(array([0, 0, 0], dtype=int64), array([0, 3, 4], dtype=int64))
for j in range(n):
    overLap = nonzero(logical_and(myMat[:, 2].A > 0, myMat[:,j].A > 0)) # �෴�� (array([3, 4, 5, 6], dtype=int64), array([0, 0, 0, 0], dtype=int64)) 
    print overLap

print shape(myMat) # 7��5�еľ���  shape(dataMat)[1]=5 (7L, 5L) 

from numpy import *
from numpy import linalg as la

def loadExData():
    return[[0, 0, 0, 2, 2],
           [0, 0, 0, 3, 3],
           [0, 0, 0, 1, 1],
           [1, 1, 1, 0, 0],
           [2, 2, 2, 0, 0],
           [5, 5, 5, 0, 0],
           [1, 1, 1, 0, 0]]
# ŷʽ����ļ��� (0,1]
def euliSin(inA, inB):
    return 1.0/(1.0 + la.norm(inA - inB))
# Ƥ��ѷ���ϵ�� (0,1]
def pearsSim(inA, inB):
    if len(inA) < 3 : return 1.0
    return 0.5 + 0.5*corrcoef(inA, inB, rowvar=0)[0][1]
# �������ƶ� (0,1]
def cosSim(inA, inB):
    num = float(inA.T*inB)
    denom = la.norm(inA)*la.norm(inB)
    return 0.5 + 0.5*(num/denom)

# �����ڸ������ƶȼ��㷽�����������û�����Ʒ�Ĺ�������ֵ
# dataMat��ԭʼ����  user���û��±�(����) item:δ���ֵĲ�ʽ���±�
def standEst(dataMat, user, simMeans, item):
    n = shape(dataMat)[1]  
    simTotal = 0.0; ratSimTotal = 0.0
    for j in range(n):
        userRating = dataMat[user, j]
        if userRating == 0: continue
        # ����{��itemֵ>0}  ��  ����{��jֵ>0}  ����
        overLap = nonzero(logical_and(dataMat[:, item].A > 0, dataMat[:,j].A > 0))[0]
        if len(overLap) == 0: similarity = 0
        # �������е������
        else: similarity = simMeans(dataMat[overLap, item], dataMat[overLap, j])
        #print 'the %d and %d similarity is : %f' %(item, j, similarity)
        simTotal += similarity
        ratSimTotal += similarity * userRating
    if simTotal == 0: return 0
    else: return ratSimTotal/simTotal
    
def recommend(dataMat, user, N=3, simMeans = cosSim, estMethod = standEst):
    # nonzero �����ǲ�Ϊ0���±�
    unreatedItems = nonzero(dataMat[user, :].A==0)[1]
    #print unreatedItems  # δ���۵Ĳ�ʽ���±꼯��[1,2] 
    if len(unreatedItems) == 0: return 'you rated everything'
    itemScores = []
    for item in unreatedItems:
        estimatedScore = estMethod(dataMat, user, simMeans, item)
        itemScores.append((item, estimatedScore))
    return sorted(itemScores, key = lambda jj: jj[1], reverse=True)[:N]

myMat = mat(loadExData())
myMat[0,1]=myMat[0,0]=myMat[1,0]=myMat[2,0]=4
print recommend(myMat, 2)
#print recommend(myMat, 2, simMeans=euliSin)
#print recommend(myMat, 2, simMeans=pearsSim)


def loadExData2():
    return[[0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 5],
           [0, 0, 0, 3, 0, 4, 0, 0, 0, 0, 3],
           [0, 0, 0, 0, 4, 0, 0, 1, 0, 4, 0],
           [3, 3, 4, 0, 0, 0, 0, 2, 2, 0, 0],
           [5, 4, 5, 0, 0, 0, 0, 5, 5, 0, 0],
           [0, 0, 0, 0, 5, 0, 1, 0, 0, 5, 0],
           [4, 3, 4, 0, 0, 0, 0, 5, 5, 0, 1],
           [0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 4],
           [0, 0, 0, 2, 0, 2, 5, 0, 0, 1, 2],
           [0, 0, 0, 0, 5, 0, 0, 0, 0, 4, 0],
           [1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0]]

'''
U, Sigma, VT = la.svd(mat(loadExData2()))
print len(Sigma) # 11ά
print Sigma  
Sig2 = Sigma**2  # ��ƽ��
sumS = sum(Sig2)
print sumS      # 542.0
standard = sumS*0.9  # �ﵽ��������90%�Ϳ��ԶԾ���ά
print sum(Sig2[:2]) # 378.829559511 / 542.0 = 0.698947526774
print sum(Sig2[:3]) # 500.500289128 / 542.0 = 0.923432267763
# ��11ά����ת����3ά�ľ���
'''
def svdEst(dataMat, user, simMeans, item):
    n = shape(dataMat)[1]  
    simTotal = 0.0; ratSimTotal = 0.0
    U, Sigma, VT = la.svd(dataMat)
    Sig4 = mat(eye(4)*Sigma[:4])  # �����ԽǾ���
    print '-----before--------------'
    print Sig4
    print dataMat.T  # transpose of the matrix ת��
    print U[:,:4]
    print Sig4.I  # inverse of invertible self  ��
    print '-----end--------------'
    xformedItems = dataMat.T * U[:,:4] * Sig4.I # ����ת�������Ʒ����11ά��4ά��
    #print xformedItems
    for j in range(n):
        userRating = dataMat[user, j]
        if userRating == 0 or j == item: continue
        similarity = simMeans(xformedItems[item,:].T, xformedItems[j,:].T)
        simTotal += similarity
        ratSimTotal += similarity * userRating
    if simTotal == 0: return 0
    else: return ratSimTotal/simTotal

myMat = mat(loadExData2())
print recommend(myMat, 1, estMethod=svdEst)
#print recommend(myMat, 1, estMethod=svdEst, simMeans=pearsSim)
#print recommend(myMat, 1, estMethod=svdEst, simMeans=euliSin)
'''
[(4, 3.3447149384692283), (7, 3.3294020724526963), (9, 3.328100876390069)]
[(4, 3.3469521867021736), (9, 3.3353796573274699), (6, 3.307193027813037)]
[(4, 3.3286756747000452), (9, 3.3247038080937834), (7, 3.3224884985810177)]
'''

def printMat(inMat, thresh=0.8):
    for i in range(32):
        for k in range(32):
            if float(inMat[i,k]) > thresh:
                print 1,
            else:
                print 0,
        print ''
'''
ͼ��ѹ��  �� 32X32=1024 ѹ����32X2 + 2 + 32X2 = 130  1024/130=7.876
numSV�� SVD������� ���õ�ά�ȸ���
thresh�� ��ֵ
'''      
def imgCompress(numSV=3, thresh=0.8):
    myl = []
    for line in open('0_5.txt').readlines():
        newRow = []
        for i in range(32):
            newRow.append(int(line[i]))
        myl.append(newRow)
    myMat = mat(myl)
    print '----------original matrix-----------'
    printMat(myMat, thresh)
    U, Sigma, VT = la.svd(myMat)
    SigRecon = mat(zeros((numSV, numSV)))   
    for k in range(numSV):
        SigRecon[k,k] = Sigma[k]  # ��Sigma�ع���SigRecon
    reconMat = U[:,:numSV] * SigRecon*VT[:numSV,:]  # ��������С����ԭ��ԭ����
    print '------------reconstructed matrix using %d singular values-------' % numSV
    printMat(reconMat, thresh)

imgCompress(2) 
		   
		   
	
********************************* PCA ***********************************************
1000L  1L�����ݽ��н�ά��ͼ����
from numpy import *

def loadDataSet(fileName, delim='\t'):
    fr = open(fileName)
    stringArr = [line.strip().split(delim) for line in fr.readlines()]
    datArr = [map(float, line) for line in stringArr]
    return mat(datArr)

def pca(dataMat, topNfeat = 9999999):
    meanVals = mean(dataMat, axis = 0)          # ��ƽ��ֵ   [[ 9.06393644  9.09600218]]
    meanRemoved =  dataMat - meanVals           # ��ֵ
    covMat = cov(meanRemoved, rowvar = 0)       # ����Э������� 
    eigVals , eigVects = linalg.eig(mat(covMat)) # ����ֵ ��������
    ''' 
    eigVals = [ 0.36651371  2.89713496]
    eigVects = [[-0.85389096 -0.52045195]
                [ 0.52045195 -0.85389096]] 
    '''
    eigValInd = argsort(eigVals)         # ������ֵ��С��������   [0, 1]
    eigValInd = eigValInd[:-(topNfeat + 1) : -1] # ����������ֵ  [1]
    redEigVects = eigVects[:,eigValInd]          # ����ǰN����������
    lowDDataMat = meanRemoved * redEigVects      # ������ת����N�����������������¿ռ���
    reconMat = (lowDDataMat * redEigVects.T) + meanVals  # ��������ֵ�»�ԭ��ԭ����
    return lowDDataMat, reconMat

dataMat = loadDataSet('testSet.txt')
lowDMat, reconMat = pca(dataMat, 1)
print shape(lowDMat)
print lowDMat
print reconMat

import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(dataMat[:,0].flatten().A[0], dataMat[:,1].flatten().A[0], marker='^', s=90)
ax.scatter(reconMat[:,0].flatten().A[0], reconMat[:,1].flatten().A[0], marker='o', s=50, c='red')

		   
����ȱʡֵNaN��ƽ��ֵ������   590������5.3M  ML���ڲ��Է�����ȱ�ݵĲ�Ʒ  
def replaceNanWithMean():
    datMat = loadDataSet('secom.data', ' ')  
    numFeat = shape(datMat)[1]
    for i in range(numFeat):
        meanVal = mean(datMat[nonzero(~isnan(datMat[:,i].A))[0], i])  # �������з�NaN��ƽ��ֵ
        datMat[nonzero(isnan(datMat[:,i].A))[0], i] = meanVal   # ������NaN��Ϊƽ��ֵ 
    return datMat
dataMat = replaceNanWithMean()
# print shape(dataMat) # 1567L 590L
meanVals = mean(dataMat, axis =0)  # ��ȡ��ֵ
meanRemoved = dataMat - meanVals   # ȥ��ֵ
covMat = cov(meanRemoved, rowvar = 0) # Э�������
eigVals, eigVects = linalg.eig(mat(covMat))
#print eigVals   #ǰ20�����ɷָ�����99.3%�ķ���
for i in range(len(eigVals)*2/10):
    print eigVals[i]



