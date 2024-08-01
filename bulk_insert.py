import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

def bulk_load_to_snowflake(df: pd.DataFrame, table_name: str, conn_params: dict):
    """Highly optimized Arrow-based bulk insert for Snowflake."""
    ctx = snowflake.connector.connect(**conn_params)
    try:
        success, nchunks, nrows, _ = write_pandas(
            conn=ctx,
            df=df,
            table_name=table_name.upper(),
            auto_create_table=True,
            quote_identifiers=False
        )
        print(f"Success: {success}, Inserted {nrows} rows in {nchunks} chunks.")
    finally:
        ctx.close()

if __name__ == "__main__":
    print("Utility ready. Used for bypassing slow SQLAlchemy inserts on >1M rows.")
