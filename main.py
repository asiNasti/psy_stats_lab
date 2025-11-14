import pandas
from sqlalchemy import create_engine

#print(file.head())

def load_excel_to_sqlite(
        excel_path,
        db_path='data/research.db',
        table_name='data_table',
        header=True,
        column_names=None
):
    
    file = pandas.read_excel(excel_path, header=0 if header else None) 
    if column_names != None:
        file.columns = column_names

    engine = create_engine(f'sqlite:///{db_path}')
    file.to_sql(table_name, engine, if_exists='replace', index=False)

    print(f"Data from {excel_path} written in to table '{table_name}' in {db_path}")

#load_excel_to_sqlite('data/data.xls', 'data/research.db', 'partissipants', False, ['group_type', 'score'])

