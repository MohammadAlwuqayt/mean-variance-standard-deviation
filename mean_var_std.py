import numpy as np

def Calculate(inputList):

    if len(inputList) != 9 :
        raise VaError("List must contain 9 numbers")

    matrix = np.array(inputList).reshape(3 , 3)

    calculations = {
        "mean": [ 
            np.mean(matrix , axis=0).tolist(),
            np.mean(matrix , axis=1).tolist(),
            np.mean(matrix).item()
        ],
        "Variance": [
            np.var(matrix , axis=0).tolist(),
            np.var(matrix , axis=1).tolist(),
            np.var(matrix).item()
        ] ,
        'standard deviation': [
            np.std(matrix, axis=0).tolist(),
            np.std(matrix, axis=1).tolist(),
            np.std(matrix).item()
        ],
        'max': [
            np.max(matrix, axis=0).tolist(),
            np.max(matrix, axis=1).tolist(),
            np.max(matrix).item()
        ],
        'min': [
            np.min(matrix, axis=0).tolist(),
            np.min(matrix, axis=1).tolist(),
            np.min(matrix).item()
        ],
        'sum': [
            np.sum(matrix, axis=0).tolist(),
            np.sum(matrix, axis=1).tolist(),
            np.sum(matrix).item()
        ]
    }

    return calculations

