# just a driver program to informally test functions

from degreeplan_data import *      # imports catalog, corereq, and majorreq
from degreeplan_functions import * # import the functions


# def possibilities(coursestaken=coursestaken,
#                   corereq=corereq, majorreq=majorreq,cselectives=cselectives,
#                   langPhilCulture=langPhilCulture, creativeArts=creativeArts,
#                   socialScience=socialScience):

#     # start with: corereq | majorreq | langPhilCulture | creativeArts | socialScience | cselectives
#     possibilities = corereq | majorreq | langPhilCulture | creativeArts | socialScience | cselectives

p = possibilities()
