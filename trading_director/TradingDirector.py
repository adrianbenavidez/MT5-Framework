import queue
import time
from data_provider.DataProvider import DataProvider
from typing import Dict, Callable
from events.Event import Event


class TradingDirector():

    def __init__(self, events_queue: queue.Queue, data_provider: DataProvider):

        self.events_queue = events_queue

        # Referencia de los distintos módulos
        self.data_provider = data_provider

        # Controlador de Trading
        self.continue_trading: bool = True

        # Creación del event Handler
        self.event_handler: Dict[str, Callable] = {
            "DATA": self._handle_data_event
        }

    def _handle_data_event(self, event: Event):
        # Aquí dentro gestionamos los eventos de tipo Event
        print(
            f"Recibidos nuevos datos de {event.symbol} - ultimo precio: {event.data.close}")

    def execute(self) -> None:
        # Definición del bucle principal
        while self.continue_trading:
            try:
                # Recordar que es una cola FIFO
                event = self.events_queue.get(block=False)
            except queue.Empty:
                self.data_provider.check_for_new_data()

            else:
                if event is not None:
                    handler = self.event_handler.get(event.event_type)
                    handler(event)
                else:
                    self.continue_trading = False
                    print(
                        "Error: Recibido evento nulo. Terminando ejecución del Framework")
            time.sleep(1)
        print("FIN")
