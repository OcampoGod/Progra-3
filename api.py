import pandas as pd
from sodapy import Socrata


def get_data(limite_registros, nombredepartamento):
    cliente = Socrata("www.datos.gov.co", None)
    resultados = cliente.get("gt2j-8ykr", limit=limite_registros, departamento_nom=nombredepartamento)
    # Convert to pandas DataFrame
    resultados_df = pd.DataFrame.from_records(resultados)
    return resultados_df
