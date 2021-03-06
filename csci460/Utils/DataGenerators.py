import numpy as np
import pandas as pd
import sklearn.model_selection as sklearnmodels


def GenerateSpiralData(numPoints=97, testSplit=0.25):
    """
    This generates training and testing sets for interwined
    spiral concept.
    Returns a tuple containing (in this order):
      training instance points (X train),
      testing instance points (X test),
      training labels (Y train),
      testing labels (Y test)
    """
    #https://www.researchgate.net/profile/Andre_Coelho3/publication/229011012/figure/fig1/AS:669378081222666@1536603579187/The-two-intertwined-spirals-problem.png
    idx    = np.array(range(numPoints))
    phi    = (idx/16) * 3.1415926
    radius = (6.5 * (104-idx)) / 104
    points = np.array([radius * np.cos(phi), radius * np.sin(phi)]).transpose()
    Xpts = np.append(points, (-points), 0)
    Ypts = np.append( np.array([1]*numPoints), np.array([0]*numPoints), 0 )
    return sklearnmodels.train_test_split(Xpts, Ypts, test_size=testSplit)


def GenerateCircleData(numPoints=200, testSplit=0.25):
    """
    This generates training and testing sets for a circle concept
    Returns a tuple containing (in this order):
      training instance points (X train),
      testing instance points (X test),
      training labels (Y train),
      testing labels (Y test)
    """
    Xpts = np.reshape( np.random.uniform(low=-1, high=1, size=2*numPoints), (numPoints,2) )
    Ypts = ((Xpts**2).sum(1) > 1) + 0
    return sk.train_test_split(Xpts, Ypts, test_size=testSplit)


def GenerateXOR():
    """
    This returns a training set and labels for data representing
    a simple Boolean logic table for the XOR operator.  It also
    generates some synthetic "test" data by assuming any point
    in the top-left or bottom-right quadrants are positive.
    """
    # Training instance data
    #   True, True
    #   False, True
    #   True, False
    #   False, False
    trainX = np.array([ [+1, +1], [-1, +1], [+1, -1], [-1, -1]])

    # Labeled output for training data,
    #   False
    #   True
    #   True
    #   False
    trainY = np.array( [-1, +1, +1, -1] )

    # Generate a synthetic test set
    m = 20
    testX = np.reshape(np.random.uniform(low=-1.0, high=1.0, size=m*2), (m,2))
    testY = 2*((testX[:,0] * testX[:,1]) < 0) - 1

    return trainX, trainY, testX, testY


def GenerateAdder():
    """
    This returns a training set and labels for data representing
    a simple Boolean logic table for the one-bit adder.  It returns
    the training set for testing since there is no real test data
    here.
    """
    # Training instance data
                      # x1, x2, cin
    trainX = np.array([ [0, 0, 0],\
                        [0, 0, 1],\
                        [0, 1, 0],\
                        [0, 1, 1],\
                        [1, 0, 0],\
                        [1, 0, 1],\
                        [1, 1, 0],\
                        [1, 1, 1] ])

    # Labeled output for training data,
                       # ans, cout
    trainY = np.array([ [0, 0],\
                        [1, 0],\
                        [1, 0],\
                        [0, 1],\
                        [1, 0],\
                        [0, 1],\
                        [0, 1],\
                        [1, 1] ] )

    # Just use the same set for testing
    testX = trainX
    testY = trainY

    return trainX, trainY, testX, testY


def GenerateLinearlySeparableData(m=100, testSplit=0.80):
    x1p = np.random.uniform(size=int(m/2))
    x1n = np.random.uniform(size=int(m/2))

    x2p = +0.1 + x1p + np.abs(np.random.normal(size=int(m/2))) # above y=x
    x2n = -0.1 + x1n - np.abs(np.random.normal(size=int(m/2))) # below y=x

    y1 = np.array([1]*int(m/2))
    y2 = np.array([0]*int(m/2))

    x1 = np.append( x1p, x1n )
    x2 = np.append( x2p, x2n)
    Xpts = np.array([x1,x2]).transpose()
    Ypts = np.append(y1,y2)

    return sklearnmodels.train_test_split(Xpts, Ypts, test_size=testSplit)


def GenerateRedundantDF(m=100):
    # There are only really two dimensions to this dataset
    x = np.random.normal(size=m)
    y = np.random.normal(size=m)

    # But we'll trick the caller into thinking there are
    # four different dimensions by combining the above dimensions.
    a =  1*x*y + 2*x - 1*y + 2
    b =  3*x*y - 1*x - 3*y - 4
    c = -2*x*y - 3*x + 2*y + 1
    d =  2*x*y - 2*x + 1*y - 3

    # Convert that into a Pandas data frame
    return pd.DataFrame({'A':a,\
                         'B':b,\
                         'C':c,\
                         'D':d})
