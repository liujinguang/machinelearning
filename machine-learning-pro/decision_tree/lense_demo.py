#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月17日

@author: bob
'''
from decision_tree.tree import create_tree
from decision_tree.tree_plotter import create_plot

if __name__ == '__main__':
    fr = open('lenses.txt')
    lenses = [inst.strip().split('\t') for inst in fr.readlines()]
    lense_labels = ['age', 'prescript', 'astigmatic', 'tearRate']
    lense_tree = create_tree(lenses, lense_labels)
    print lense_tree
    create_plot(lense_tree)