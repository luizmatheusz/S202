from database import Database
from motoristaDAO import MotoristaDAO
from cli import MotoristaCLI

# database
db = Database(database='ExercicioAvaliativo', collection='Motoristas')

# model
motoristaDAO = MotoristaDAO(database=db)

# CLI
motoristaCLI = MotoristaCLI(motorista_DAO=motoristaDAO)
motoristaCLI.run()