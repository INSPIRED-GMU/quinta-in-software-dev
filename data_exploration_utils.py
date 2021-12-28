"""
Utilities for analyzing the represntation of intersectional identities in data.

Last modified: December 27, 2021
"""

from collections import Counter
import itertools
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

matplotlib.use('TkAgg')
matplotlib.style.use('fast')


def non_inter_idents(table, col_nums):
    """Return a dict of counts of people with each non-intersectional identity.

    Parameters
    ----------
    table : pandas.DataFrame
        The data set.
    col_nums : list
        A list of column numbers of table that contain the parts of identities.

    Returns
    -------
    dict
        A dictionary with keys that are column names, e.g. race, gender, and
        values that are Counters of the number of data points with each
        possible value in the column, e.g. {"Black":3, "White":10}.
    """
    return {col_name: Counter(
        table[col_name]) for col_name in table.columns[col_nums]}


def all_possible_intersects(table, col_nums):
    """Find all possible intersections in a dataset.

    Parameters
    ----------
    table : pandas.DataFrame
        The data set.
    col_nums : list
        A list of column numbers of table that contain the parts of identities.

    Returns
    -------
    itertools.product
        The Cartesian product of every possible value of each column.
        e.g. (('Black, Female'), ('White, Male'), ...)
    """
    return itertools.product(
        *map(lambda d: d.keys, non_inter_idents(table, col_nums).values()))


def true_intersects_counts(table, col_nums):
    """Count the people with each intersectional identity in a dataset.

    Parameters
    ----------
    table : pandas.DataFrame
        The data set.
    col_nums : list
        A list of column numbers of table that contain the parts of identities.

    Returns
    -------
    collections.Counter
        The number of people with each intersectional identity, e.g.
        {('Black', 'Female'): 1, ('White', 'Male'): 3}
    """
    return Counter([tuple(table.iloc[row, col_nums])
                    for row in range(len(table))])


def missed_intersects(table, col_nums):
    """Find all intersections that could be present in a dataset but aren't."""
    return set(all_possible_intersects(table, col_nums)).difference(
        set(true_intersects_counts(table, col_nums).keys()))


def intersectional_rep_pie(table, col_nums, parent):
    """Create a pie chart of percentage of intersectional groups in a dataset.

    Parameters
    ----------
    table : pandas.DataFrame
        The dataset.
    col_nums : list
        A list of column numbers of table that contain the parts of identities.

    Returns
    -------
    None.

    """
    # Plot intersections
    plot_labels = list(
        map(str, true_intersects_counts(table, col_nums).keys()))
    fig, ax = plt.subplots()
    ax.pie(true_intersects_counts(table, col_nums).values(),
           labels=plot_labels, autopct='%1.1f%%')
    ax.set_title("Representation of intersectional identities")
    plt.savefig("representation_intersectional_identities.png")
    return FigureCanvasTkAgg(fig, parent)


def intersectional_rep_difference(counts_before, counts_after):
    """Calculate change in counts of intersectional identities before and after
    cleaning.

    Parameters
    ----------
    counts_before : collections.Counter
        Counter of people with each intersectional identity before cleaning.
    counts_after : collections.Counter
        Counter of people with each intersectional identity after cleaning.

    Returns
    -------
    dict
        A dictionary with intersectional identities as keys and the after value
        minus the before value as values.

    """
    return {key: (counts_after[key] - counts_before[key]
                  if key in counts_after else -counts_before[key])
            for key in counts_before}


def intersectional_rep_rel_change(counts_before, counts_after):
    # TODO: Create a plan for how to do this if counts_after and counts_before
    # have different keys, i.e., a feature was removed.
    """Calculate relative change in counts of intersectional identities before 
    and after cleaning.

    Parameters
    ----------
    counts_before : collections.Counter
        Counter of people with each intersectional identity before cleaning.
    counts_after : collections.Counter
        Counter of people with each intersectional identity after cleaning.

    Returns
    -------
    dict
        A dictionary with intersectional identities as keys and the relative
        change in each after cleaning.

    """
    return {key: ((counts_after[key] - counts_before[key]) / counts_before[key]
                  if key in counts_after else -1.0)
            for key in counts_before}


def intersectional_rep_rel_change_bar(before_table, after_table, before_cols,
                                      after_cols, parent):
    """
    

    Parameters
    ----------
    before_table : pandas.DataFrame
        The data before cleaning.
    after_table : pandas.DataFrame
        The data after cleaning.
    before_cols : list
        Column numbers to compute intersectional identities before cleaning.
    after_cols : list
        Column numbers to compute intersectional identities after cleaning.

    Returns
    -------
    None.

    """
    # Create a figure
    fig, ax = plt.subplots()
    # The counts of each intersectional identity before cleaning
    before_counts = true_intersects_counts(before_table, before_cols)
    # The counts of each intersectional identity after cleaning
    after_counts = true_intersects_counts(after_table, after_cols)
    # A dictionary of the relative change in the representation of each
    # intersectional identity
    changes = intersectional_rep_rel_change(before_counts, after_counts)
    # Use the intersectional identities as plot labels
    labels = changes.keys()
    # Set bar spacing
    positions = np.arange(len(labels))

    # Create bar plot
    ax.bar(positions, changes.values())
    ax.axhline(0, color='Grey')
    ax.set_xticks(positions)
    ax.set_xticklabels(labels)
    ax.set_xlabel('Relative change in representation')
    return FigureCanvasTkAgg(fig, parent)
