import pandas
from sqlalchemy import create_engine
from pathlib import Path


def create_db():
    BASE_DIR = Path(__file__).parent
    DATA_DIR = BASE_DIR / 'data'
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    DB_PATH = DATA_DIR / 'research.db'

    engine = create_engine(f'sqlite:///{DB_PATH}')
    engine.connect()
    return engine

def path_to_db():
    url = create_db().url
    path = url.database
    return path
    
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


if __name__ == "__main__":
    db_engine = create_db()
    db_path = path_to_db()
    load_excel_to_sqlite('data/data.xls', db_path, 'partissipants', False, ['group_type', 'score'])