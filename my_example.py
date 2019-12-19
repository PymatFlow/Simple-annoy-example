# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 10:57:22 2019

@author: Kazem
"""

from annoy import AnnoyIndex
dim = 2
a = AnnoyIndex(dim,'euclidean')

points = [[1,0],[2,1],[1,3],[-2,2],[-1,-2],[3,-1],[-1,3]]

for i,v in enumerate(points):
    a.add_item(i,v)


print(str(a.get_n_items())+ "  items are added")

a.build(30)

print(str(a.get_n_trees())+ "  trees are made")

result = a.get_nns_by_item(6,2)


items = a.get_nns_by_vector([0,4],2)