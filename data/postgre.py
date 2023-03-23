from sqlalchemy import create_engine
import data.settings as settings

postgre_host = settings.POSTGRE_HOST
postgre_port = settings.POSTGRE_PORT
postgre_username = settings.POSTGRE_USERNAME
postgre_password = settings.POSTGRE_PASSWORD
postgre_database_ailab = settings.POSTGRE_DATABASE_1

database_url_ailab = f"postgresql://{postgre_username}:{postgre_password}@{postgre_host}:{postgre_port}/{postgre_database_ailab}"

postgre_engine_ailab = create_engine(database_url_ailab)
