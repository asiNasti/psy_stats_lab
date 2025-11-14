import numpy

from scipy.stats import ttest_ind, ttest_rel
from scipy.stats import mannwhitneyu, kstest


tests = [
    "Student's t-test (independent samples)", "Student's t-test (paired samples)", 
    'Mann Whitney U test', "Wilcoxon test", "Chi-square test", "McNemar test", 
    "Kolmogorov Smirnov test", "Shapiro Wilk test", 
    "Pearson correlation", "Spearman correlation"
]

def make_choise():
    choise = int(input("How do you want to choose the static test?\n" \
    "1 automatic\n2 manual\n"))

    if choise == 1:
        type_of_analysis = int(input("Select the type of analysis:\n" \
        "1 comparison\n2 correlation\n"
        "choose number: "))

        type_of_scale = int(input("Select the measerement scale:\n" \
        "1 nominal\n2 ordinal\n3 metric\n" \
        "choose number: "))

        if type_of_analysis == 2:
            type_of_sample = "related"
        elif type_of_analysis == 1:
            type_of_sample = int(input("Select sample type:\n" \
            "1 related\n2 unrelated\n" \
            "choose number: "))

    elif choise == 2:
        menu_lines = [f"{i} - {test_name}" for i, test_name in enumerate(tests, start=1)]
        prompt = "Which statistical test would you like to use?\n" + "\n".join(menu_lines) + "\nchoose number: "
        type_of_test = int(input(prompt))

        return (type_of_test)
    
    return (type_of_analysis, type_of_scale, type_of_sample)


def choose_test():
    answers = make_choise()
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



def student_stat_tests(samples, group1, group2):
    if samples == "unrelated":
        t_stat, p_value = ttest_ind(group1, group2)
    elif samples == "related":
        t_stat, p_value = ttest_rel(group1, group2)
    return (t_stat, p_value)

def mann_whitneyu_stat_tests(group1, group2):
    return mannwhitneyu(group1, group2)

def normality_ks(group):
    return kstest(group, 'norm', qrgs=(numpy.mean(group), numpy.std(group)))



def result():
    statistic, p_value = choose_test()
    print(f"t statistic: {statistic}")
    print(f"p-value: {p_value}")

    if p_value < 0.05:
        print("The difference is statistically significant at the 0.05")
    else:
        print("The difference is not statistically significant at the 0.05")



if __name__ == "__main__":
    group1 = [20, 22, 19, 20, 21, 25, 22]
    group2 = [28, 26, 30, 27, 29, 25, 27]
    #student_stat_tests("unrelated", group1, group2)
    choose_test()