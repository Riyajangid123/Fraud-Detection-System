from src.database.connection import get_connection
import pandas as pd

def insert_prediction(amount, prediction):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO transactions (amount, prediction)
        VALUES (%s, %s)                                          
        """

        cursor.execute(query, (amount, prediction))
        conn.commit()

        status = "FRAUD" if prediction == 1 else "LEGIT"
        print(f"Transaction inserted → {status} (amount: {amount})")

    except Exception as e:
        print("Error inserting transaction:", e)

    finally:
        cursor.close()
        conn.close()

def fetch_all_predictions():
    try:
        conn=get_connection()
        query="select * from transactions"
        df=pd.read_sql(query,conn)
    except Exception as e:
        print("Error fetching:", e)

    finally:
        conn.close()