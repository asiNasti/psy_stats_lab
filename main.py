import pandas
from sqlalchemy import create_engine
from pathlib import Path
import sqlite3

from src.stat_tests import (
    chi_square_stat_test, mc_nemar_stat_test, mann_whitneyu_stat_test, 
    wilcoxon_stat_test, student_stat_test, pearson_stat_test, 
    spearman_stat_test, normality_ks)

from src.stat_analysis import choose_test
from src.reporting import interp_results

tests_with_func = {
    "Student's t-test": student_stat_test,
    "Mann Whitney U test": mann_whitneyu_stat_test, "Wilcoxon test": wilcoxon_stat_test, 
    "Chi-square test": chi_square_stat_test, "McNemar test": mc_nemar_stat_test, 
    "Kolmogorov Smirnov test": normality_ks, "Shapiro Wilk test": None, 
    "Pearson correlation": pearson_stat_test, "Spearman correlation": spearman_stat_test
    }


BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / 'data'
DATA_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = DATA_DIR / 'research.db'

    
def load_excel_to_sqlite(
        excel_path,
        db_path,
        table_name='data_table',
        header=True,
        column_names=None
):
    
    file = pandas.read_excel(excel_path, header=0 if header else None) 
    if column_names is not None:
        file.columns = column_names

    engine = create_engine(f'sqlite:///{db_path}')
    file.to_sql(table_name, engine, if_exists='replace', index=False)

    print(f"Data from {excel_path} written in to table '{table_name}' in {db_path}")


def execute_analysis():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    sql_query = "SELECT group1, group2 FROM experiment_results;"

    cursor.execute(sql_query)
    result = cursor.fetchall()

    result_group1 = []
    result_group2 = []
    for item in result:
        result_group1.append(item[0])
        result_group2.append(item[1])

    connection.close()

    test_info = choose_test(result_group1, result_group2)
    samples = None
    if isinstance(test_info, tuple):
        name_of_test, samples = test_info
    else:
        name_of_test = test_info

    test_func = tests_with_func.get(name_of_test)
    if test_func is None:
        try:
            if name_of_test == "Student's t-test":
                stat_result = test_func(samples, result_group1, result_group2)

            elif name_of_test in ["Mann Whitney U test", "Wilcoxon test", 
                                "Pearson correlation", "Spearman correlation",
                                "Chi-square test", "McNemar test", "Shapiro Wilk test"]:
                stat_result = test_func(result_group1, result_group2)

            elif name_of_test == "Kolmogorov Smirnov test":
                stat_result = test_func(result_group1)

            else:
                stat_result = test_func(result_group1, result_group2)
        except TypeError as e:
            print(f"Call error {name_of_test}: {e}")
            print("Check if the arguments are passed correctly in execute_analysis.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    interp_results(stat_result)


if __name__ == "__main__":
    load_excel_to_sqlite('data/data.xls', DB_PATH, 'experiment_results', False, ['group1', 'group2'])
    execute_analysis()