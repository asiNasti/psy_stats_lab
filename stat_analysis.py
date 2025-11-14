def make_choise():
    choise = input("How do you want to choose the static test?\n" \
    "1 automatic\n2 manual\n")

    if choise in ['1', 'automatic']:
        type_of_analysis = input("Select the type of analysis:\n" \
        "1 comparison\n2 correlation\n")

        if type_of_analysis in ['2', 'correlation']:
            type_of_sample = "related"
        elif type_of_analysis in ['1', 'comparison']:
            type_of_sample = input("Select sample type:\n" \
            "1 related\n2 unrelated\n")

        type_of_scale = input("Select the measerement scale:\n" \
        "1 ordinal\n2 nominal \n3 metric\n")


    elif choise in ['2', 'manual']:
        type_of_test = input("Which statistical test would you like to use?\n"
        "1 - Student's t-test (independent samples)\n"
        "2 - Student's t-test (paired samples)\n"
        "3 - Mann Whitney U test\n"
        "4 - Wilcoxon test\n"
        "5 - Chi-square test\n"
        "6 - McNemar test\n"
        "7- Kolmogorov Smirnov test (normality)\n"
        "8 - Shapiro Wilk test (normality)\n"
        "9 - Pearson correlation\n"
        "10 - Spearman correlation\n" \
        "your option: ")
