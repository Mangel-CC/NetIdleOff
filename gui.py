import time
import threading
import customtkinter as ctk
from functions import obtener_velocidad_red, apagar_computadora

class NetIdleOffApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("NetIdleOff")
        self.geometry("400x350")

        self.monitoring = False
        self.monitor_thread = None

        # Variables
        self.umbral_var = ctk.StringVar(value="100")
        self.tiempo_var = ctk.StringVar(value="300")

        # Interfaz
        self.create_widgets()

    def create_widgets(self):
        titulo_label = ctk.CTkLabel(self, text="NetIdleOff", font=("Arial", 20, "bold"))
        titulo_label.pack(pady=10)

        frame_config = ctk.CTkFrame(self)
        frame_config.pack(pady=10, padx=20, fill="x")

        umbral_label = ctk.CTkLabel(frame_config, text="Umbral (kbps):")
        umbral_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        umbral_entry = ctk.CTkEntry(frame_config, textvariable=self.umbral_var)
        umbral_entry.grid(row=0, column=1, padx=5, pady=5, sticky="e")

        tiempo_label = ctk.CTkLabel(frame_config, text="Tiempo inactividad (seg):")
        tiempo_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        tiempo_entry = ctk.CTkEntry(frame_config, textvariable=self.tiempo_var)
        tiempo_entry.grid(row=1, column=1, padx=5, pady=5, sticky="e")

        frame_buttons = ctk.CTkFrame(self)
        frame_buttons.pack(pady=10)

        self.iniciar_btn = ctk.CTkButton(frame_buttons, text="Iniciar", command=self.iniciar_monitoreo)
        self.iniciar_btn.grid(row=0, column=0, padx=10, pady=5)

        self.detener_btn = ctk.CTkButton(frame_buttons, text="Detener", command=self.detener_monitoreo)
        self.detener_btn.grid(row=0, column=1, padx=10, pady=5)

        self.velocidad_label = ctk.CTkLabel(self, text="Velocidad actual: -- Kbps")
        self.velocidad_label.pack(pady=10)

        self.inactividad_label = ctk.CTkLabel(self, text="Inactividad: 0s")
        self.inactividad_label.pack(pady=10)

    def iniciar_monitoreo(self):
        if not self.monitoring:
            self.monitoring = True
            self.monitor_thread = threading.Thread(target=self.monitorear_red, daemon=True)
            self.monitor_thread.start()

    def detener_monitoreo(self):
        self.monitoring = False

    def monitorear_red(self):
        umbral_kbps = float(self.umbral_var.get().strip())
        tiempo_verificacion = int(self.tiempo_var.get().strip())
        tiempo_inactividad = 0

        while self.monitoring:
            velocidad_red = obtener_velocidad_red()
            self.velocidad_label.configure(text=f"Velocidad actual: {velocidad_red:.2f} Kbps")

            if velocidad_red < umbral_kbps:
                tiempo_inactividad += 1
            else:
                tiempo_inactividad = 0

            self.inactividad_label.configure(text=f"Inactividad: {tiempo_inactividad}s")

            if tiempo_inactividad >= tiempo_verificacion:
                apagar_computadora()
                self.monitoring = False
                break

            for _ in range(10):
                if not self.monitoring:
                    break
                time.sleep(0.1)
