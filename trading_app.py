from platform_connector.PlatformConnector import PlatformConnector

if __name__ == "__main__":

    # Definición de variables necesarias para la estrategia
    symbols = ["EURUSD", "USDJPY", "FDSFGD"]

    CONNECT = PlatformConnector(symbol_list = symbols)
    