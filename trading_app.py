from platform_connector.PlatformConnector import PlatformConnector
from data_provider.DataProvider import DataProvider
from queue import Queue
from trading_director.TradingDirector import TradingDirector

if __name__ == "__main__":

    # Definición de variables necesarias para la estrategia
    symbols = ["EURUSD", "USDJPY", "FDSFGD"]
    timeframe = '1min'

    # Creación de la cola de eventos principal
    events_queue = Queue()

    # Creación de los modulos principales del framework
    CONNECT = PlatformConnector(symbol_list=symbols)
    # DATAPROVIDER = DataProvider(
    #    events_queue=Queue, symbol_list=symbols, timeframe=timeframe)

    # Creación del trading director y ejecución del método principal
    # TRADING_DIRECTOR = TradingDirector(
    #    events_queue=events_queue, data_provider=DATAPROVIDER)
    # TRADING_DIRECTOR.execute()
