import numpy

from scipy.stats import ttest_ind, ttest_rel
from scipy.stats import mannwhitneyu, wilcoxon
from scipy.stats import chi2_contingency
from scipy.stats import kstest, shapiro
from scipy.stats import pearsonr, spearmanr

from statsmodels.stats.contingency_tables import mcnemar


def chi_square_stat_test(group1, group2):
    return chi2_contingency(group1, group2)

def mc_nemar_stat_test(group1, group2):
    return mcnemar(group1, group2)

def mann_whitneyu_stat_test(group1, group2):
    return mannwhitneyu(group1, group2)

def wilcoxon_stat_test(group1, group2):
    return wilcoxon(group1, group2)

def student_stat_test(samples, group1, group2):
    if samples == "unrelated":
        t_stat, p_value = ttest_ind(group1, group2)
    elif samples == "related":
        t_stat, p_value = ttest_rel(group1, group2)
    return (t_stat, p_value)

def pearson_stat_test(group1, group2):
    return pearsonr(group1, group2)

def spearman_stat_test(group1, group2):
    return spearmanr(group1, group2)

def normality_ks(group):
    return kstest(group, 'norm', qrgs=(numpy.mean(group), numpy.std(group)))