from procedural.imports import import_data_procedural
from procedural.queries import run_queries_procedural

from object.imports import import_data_orm
from object.queries import run_queries_orm

if __name__ == "__main__":
    import_data_procedural()
    run_queries_procedural()
    
    print("\n" + "#" * 50 + "\n")
    
    import_data_orm()
    run_queries_orm()