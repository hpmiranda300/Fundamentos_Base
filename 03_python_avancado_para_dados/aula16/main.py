from pathlib import Path
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select, text

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

# Aponta para a pasta onde o próprio main.py está localizado (aula16/)
# 1. Define os caminhos da pasta aula16
pasta = Path(__file__).parent
db_path = pasta / "database.db"
sql_file = pasta / "read_sql.sql"

# 2. Lê a query do arquivo .sql
query = sql_file.read_text(encoding="utf-8")

# 3. Cria a conexão
# Usamos .as_posix() para padronizar as barras no formato aceito pelo SQLite (/)
engine = create_engine(f"sqlite:///{db_path.as_posix()}", echo=True)
#engine = create_engine("sqlite:///database.db", echo=True)
#engine = create_engine("sqlite:///aula16/database.db", echo=True)

SQLModel.metadata.create_all(engine)

#Arquivo C:\Projetos_Git\Fundamentos_Base\03_python_avancado_para_dados\aula16\create.py
hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.commit()

#Arquivo C:\Projetos_Git\Fundamentos_Base\03_python_avancado_para_dados\aula16\read.py
with Session(engine) as session:
    statement = select(Hero).where(Hero.name == "Spider-Boy")
    hero = session.exec(statement).first()
    print(hero)


#Arquivo C:\Projetos_Git\Fundamentos_Base\03_python_avancado_para_dados\aula16\read_ops.py
with Session(engine) as session:
    # Sua consulta SQL
    statement = text("SELECT * FROM hero;")
    
    # Executando a consulta
    results = session.exec(statement)
    
    # Fetch dos resultados
    heroes = results.fetchall()
    
    # Imprimindo os resultados
    for hero in heroes:
        print(hero)

#Arquivo C:\Projetos_Git\Fundamentos_Base\03_python_avancado_para_dados\aula16\read_sql.sql
with Session(engine) as session:
    results = session.exec(text(query)).fetchall()
    
    for row in results:
        print(row)