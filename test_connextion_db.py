from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql+psycopg2://postgres:Sa%40123456@127.0.0.1:5432/restaurant_db"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT current_user, current_database();"))
        print("Connexion successfully !")
        print(result.fetchone())

except Exception as e:
    print("Failed :", e)