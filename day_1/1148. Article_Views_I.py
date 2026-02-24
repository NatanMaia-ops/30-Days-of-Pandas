import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    condition = views['author_id'] == views['viewer_id']
    return pd.DataFrame(views.loc[condition, ['author_id']]).sort_values(by="author_id").drop_duplicates(subset=["author_id"]).rename(columns={"author_id":"id"})

    