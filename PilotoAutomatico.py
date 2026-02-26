import tkinter as tk
import threading
import time
import pyautogui
from datetime import datetime

running = False
worker_thread = None

def log(msg):
    timestamp = datetime.now().strftime("%H:%M:%S")
    console.config(state="normal")
    console.insert("end", f"[{timestamp}] {msg}\n")
    console.see("end")
    console.config(state="disabled")

def automation():
    global running
    cycle = 1
    while running:
        # Obtener posición actual
        x, y = pyautogui.position()

        # Mover 10 pixeles arriba (desplazamiento continuo)
        pyautogui.moveTo(x, y - 10, duration=0.5)
        time.sleep(0.5)

        # Regresar a posición original
        pyautogui.moveTo(x, y, duration=0.5)
        time.sleep(0.5)

        # Mover 10 pixeles abajo
        pyautogui.moveTo(x, y + 10, duration=0.5)
        time.sleep(0.5)

        # Regresar a posición original
        pyautogui.moveTo(x, y, duration=0.5)
        time.sleep(0.5)

        # Presionar Shift 5 veces
        for _ in range(5):
            pyautogui.keyDown("shift")
            pyautogui.keyUp("shift")
            time.sleep(0.5)

        log(f"Ciclo {cycle} ejecutado correctamente.")
        cycle += 1
        time.sleep(300)

def start():
    global running, worker_thread
    if not running:
        running = True
        log("Piloto automático INICIADO.")
        worker_thread = threading.Thread(target=automation, daemon=True)
        worker_thread.start()

def stop():
    global running
    if running:
        running = False
        log("Piloto automático DETENIDO.")

# Interfaz
root = tk.Tk()
root.title("Piloto Automático")
root.geometry("500x300")
root.resizable(False, False)

# Botones en la parte superior
button_frame = tk.Frame(root)
button_frame.pack(side="top", pady=10)

start_button = tk.Button(button_frame, text="Iniciar", command=start, width=12)
start_button.pack(side="left", padx=10)

stop_button = tk.Button(button_frame, text="Detener", command=stop, width=12)
stop_button.pack(side="left", padx=10)

# Consola
console_frame = tk.Frame(root)
console_frame.pack(side="top", fill="both", expand=True, padx=10, pady=(0, 10))

console = tk.Text(console_frame, bg="#1e1e1e", fg="#00ff00", font=("Consolas", 10),
                   state="disabled", wrap="word")
console.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(console_frame, command=console.yview)
scrollbar.pack(side="right", fill="y")
console.config(yscrollcommand=scrollbar.set)

# Mensaje inicial
log(f"Programa iniciado a las {datetime.now().strftime('%H:%M:%S')}")

root.mainloop()