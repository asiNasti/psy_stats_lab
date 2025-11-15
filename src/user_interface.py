def make_choise(tests):
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
        if type_of_test == 1:
            type_of_sample = int(input("Select sample type:\n" \
            "1 related\n2 unrelated\n" \
            "choose number: "))

        return (type_of_test, type_of_sample)
    
    return (type_of_analysis, type_of_scale, type_of_sample)
