# NetIdleOff

**NetIdleOff** es una herramienta que supervisa continuamente la velocidad de descarga de la red y apaga automáticamente tu equipo cuando la actividad de red permanece por debajo de un umbral definido durante un tiempo determinado.

## Características

- **Monitoreo en tiempo real:** Muestra la velocidad de descarga actual.
- **Umbral personalizable:** Ajusta la velocidad mínima en Kbps a partir de la cual se considera “inactividad”.
- **Tiempo de inactividad configurable:** Define cuántos segundos de baja actividad son necesarios para ejecutar el apagado.
- **Interfaz gráfica sencilla:** Configura todo a través de una ventana intuitiva creada con *customtkinter*.
- **Automatización del apagado:** Una vez cumplidas las condiciones, el equipo se apaga sin necesidad de intervención manual.

> **Nota:** Esta aplicación está pensada para **Windows**. En caso de usar otros sistemas operativos, deberás ajustar el comando de apagado en el código.

## Requisitos

- **Python 3.x**
- [psutil](https://pypi.org/project/psutil/)  
  ```bash
  pip install psutil
