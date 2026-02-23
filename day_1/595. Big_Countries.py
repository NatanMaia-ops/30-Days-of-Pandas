import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    area = world['area'] >= 3000000
    population = world['population'] >= 25000000

    return pd.DataFrame(world.loc[(area) | (population), ['name','population','area']])
    