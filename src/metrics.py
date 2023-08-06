#from pandas import DataFrame

def confusion_matrix(y_true, y_pred, labels=None):
    if not labels:
        labels = sorted(set(y_pred).union(set(y_true)))
    lookup_d = dict()
    lookup_c = 0
    matrix = [[0 for _ in range(len(labels))] for _ in range(len(labels))]
    for label in labels:
        lookup_d[label] = lookup_c
        lookup_c += 1
    print(lookup_d)
    print(matrix)
    for i in range(len(y_pred)):
        matrix[lookup_d[y_true[i]]][lookup_d[y_pred[i]]] +=1
    return matrix

def accuracy(conf_matrix):
    size = len(conf_matrix)
    total = 0
    accurate = 0
    for i in range(size):
        for j in range(size):
            total += conf_matrix[i][j]
            if i == j: accurate += conf_matrix[i][j]
    return accurate / total

def precision(conf_matrix):
    tn, fp, fn, tp = conf_matrix.ravel()
    return tp / tp + fp

def recall(conf_matrix):
    tn, fp, fn, tp = conf_matrix.ravel()
    return tp / tp + fn

def f1_measure(conf_matrix):
    tn, fp, fn, tp = conf_matrix.ravel()
    return 2*tp / ( 2*tp + fp + fn )