import numpy as np


def package_responses(experiment, node):
    return np.loadtxt('/home/john/workspace/foil_activation/response/response_vectors/experiment_{}_node_{}.txt'.format(experiment, node))
