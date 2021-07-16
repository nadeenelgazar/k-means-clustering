import numpy

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

#in order to make algorithm go faster and more accurate data need to be normalized that what this function do
def normalizeimages():
    dict=unpickle("data_batch_1")

    normDict=[]


    for row in dict[b'data']:
        dataset=numpy.array(row)
        normDataset=(dataset-min(dataset))/(max(dataset)-min(dataset))
        normDict.append(normDataset)

    return normDict