def interp_results(func_result):
    statistic, p_value = func_result
    print(f"t statistic: {statistic}")
    print(f"p-value: {p_value}")

    if p_value < 0.05:
        print("The difference is statistically significant at the 0.05")
    else:
        print("The difference is not statistically significant at the 0.05")
