"""Tests for the data_exploration_utils.

Last modified: July 8, 2021
"""
import pandas as pd
import data_exploration_utils as deu

data1 = pd.read_csv('test_data/data1.csv')
data2 = pd.read_csv('test_data/data2.csv')
relevant_cols = [1, 2, 3]

deu.intersectional_rep_pie(data1, relevant_cols)
deu.intersectional_rep_pie(data2, relevant_cols)

counts_before = deu.true_intersects_counts(data1, relevant_cols)
counts_after = deu.true_intersects_counts(data2, relevant_cols)
print(deu.intersectional_rep_difference(counts_before, counts_after))
print(deu.intersectional_rep_rel_change(counts_before, counts_after))

# make a bar chart of relative change
