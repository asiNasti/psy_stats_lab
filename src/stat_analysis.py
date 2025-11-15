from .stat_tests import normality_ks
from .user_interface import make_choise

tests = [
    "Student's t-test", 'Mann Whitney U test', 
    "Wilcoxon test", "Chi-square test", "McNemar test", 
    "Kolmogorov Smirnov test", "Shapiro Wilk test", 
    "Pearson correlation", "Spearman correlation"
]

def choose_test(group1, group2):
    answers = make_choise(tests)
    if len(answers) == 1:
        test_number = answers[0]
        return tests[test_number-1]
    elif len(answers) == 2:
        test_number, type_of_sample = answers
        return tests[test_number-1], type_of_sample
     
    else:
        type_of_analysis, type_of_scale, type_of_sample = answers
        test = None
        if type_of_analysis == 1:
            if type_of_scale == 1:
                test = nominal_sample(type_of_sample)
            elif type_of_scale == 2:
                test = ordinal_sample(type_of_sample)
            elif type_of_scale == 3:
                test = metric_sample(type_of_sample, group1, group2)
        
        elif type_of_analysis == 2:
            if type_of_scale == 3:
                test = "Pearson correlation"
            elif type_of_scale == 2:
                test = "Spearman correlation"

    return test, type_of_sample
                            
            
def nominal_sample(sample):
    if sample == 1:
        test = "Chi-square test"
    elif sample == 2:
        test = "McNemar test"
    else:
        test = None    
    return test

def ordinal_sample(sample):
    if sample == 1:
        test = "Mann Whitney U test"
    elif sample == 2:
        test = "Wilcoxon test"
    else:
        test = None
    return test

def metric_sample(sample, group1, group2):
    is_group1_normal = normality_ks(group1)[1] > 0.05
    is_group2_normal = normality_ks(group2)[1] > 0.05

    if is_group1_normal and is_group2_normal:
        test = "Student's t-test"
    else:
        test = ordinal_sample(sample)
    return test




if __name__ == "__main__":
    pass