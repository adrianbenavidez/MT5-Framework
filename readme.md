## Configuración del entorno
Para ejecutar este proyecto, necesitas crear un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno:
| Variable       | Descripción                                                        |
| `MT5_PATH`     | Ruta completa al ejecutable de la plataforma MetaTrader 5.         |
| `MT5_LOGIN`    | Número de cuenta de trading en MetaTrader 5.                       |
| `MT5_PASSWORD` | Contraseña de la cuenta de trading en MetaTrader 5.                |
| `MT5_SERVER`   | Nombre del servidor de trading.                                    |
| `MT5_TIMEOUT`  | Tiempo de espera en milisegundos para la conexión a la plataforma. |
| `MT5_PORTABLE` | Indica si se está utilizando una versión portable de MetaTrader 5 (True/ False). |

**Ejemplo de archivo `.env`:**

MT5_PATH=
MT5_LOGIN=
MT5_PASSWORD=
MT5_SERVER=
MT5_TIMEOUT=
MT5_PORTABLE=