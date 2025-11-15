from stat_tests import normality_ks

from user_interface import make_choise
from src.reporting import result

tests = [
    "Student's t-test (independent samples)", "Student's t-test (paired samples)", 
    'Mann Whitney U test', "Wilcoxon test", "Chi-square test", "McNemar test", 
    "Kolmogorov Smirnov test", "Shapiro Wilk test", 
    "Pearson correlation", "Spearman correlation"
]

def choose_test():
    answers = make_choise(tests)
    if len(answers) == 1:
        test = tests[answers-1]
    else:
        type_of_analysis, type_of_scale, type_of_sample = answers
        if type_of_analysis == 1:
            if type_of_scale == 1:
                test = nominal_sample(type_of_sample)
            if type_of_scale == 2:
                test = ordinal_sample(type_of_sample)
            if type_of_scale == 3:
                test = metric_sample(type_of_sample)
    print(test)
                            
            
def nominal_sample(sample):
    if sample == 1:
        test = "Chi-square test"
    elif sample == 2:
        test = "McNemar test"
    return test

def ordinal_sample(sample):
    if sample == 1:
        test = "Mann Whitney U test"
    elif sample == 2:
        test = "Wilcoxon test"
    return test

def metric_sample(sample, group):
    if normality_ks(group):
        test = "Student's t-test"
    else:
        test = ordinal_sample(sample)
    return test




if __name__ == "__main__":
    choose_test()