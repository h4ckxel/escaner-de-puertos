import socket
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext
from concurrent.futures import ThreadPoolExecutor

# escaneo especifico
def scan_port(ip, port, result_text):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # reductor de timeout
        result = sock.connect_ex((ip, port))
        if result == 0:
            result_text.insert(tk.END, f"Puerto {port} está abierto\n")
        sock.close()
    except Exception as e:
        result_text.insert(tk.END, f"Error al escanear el puerto {port}: {e}\n")

# funcion para iniciar el escaneo con ThreadPoolExecutor
def start_scan(ip, start_port, end_port, result_text):
    result_text.delete(1.0, tk.END)  # Limpiar la caja de texto
    result_text.insert(tk.END, f"Escaneando {ip} desde el puerto {start_port} hasta {end_port}\n")

    # limitador de hilos
    with ThreadPoolExecutor(max_workers=10000) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, ip, port, result_text)

# funcion del boton
def on_scan_button_click(ip_entry, start_port_entry, end_port_entry, result_text):
    ip = ip_entry.get()
    start_port = int(start_port_entry.get())
    end_port = int(end_port_entry.get())

    # hilo separado para no bloquear la interfaz
    scan_thread = threading.Thread(target=start_scan, args=(ip, start_port, end_port, result_text))
    scan_thread.start()

# configuración de la interfaz
def create_gui():
    window = tk.Tk()
    window.title("Escáner de Puertos - H4ckxel")
    window.geometry("600x500")
    window.configure(bg="black")

    # estillo de la interfaz
    style = ttk.Style()
    style.configure("TLabel", foreground="lime", background="black", font=("Consolas", 10))
    style.configure("TButton", foreground="black", background="lime", font=("Consolas", 10), padding=5)
    style.configure("TEntry", foreground="lime", background="black", font=("Consolas", 10))
    
    ascii_art = """
  .uef^"            xeee              < .z@8"`                              x .d88"  
:d88E              d888R               !@88E           uL   ..               5888R   
`888E             d8888R          .    '888E   u     .@88b  @88R      .u     '888R   
 888E .z8k       @ 8888R     .udR88N    888E u@8NL  '"Y888k/"*P    ud8888.    888R   
 888E~?888L    .P  8888R    <888'888k   888E`"88*"     Y888L     :888'8888.   888R   
 888E  888E   :F   8888R    9888 'Y"    888E .dN.       8888     d888 '88%"   888R   
 888E  888E  x"    8888R    9888        888E~8888       `888N    8888.+"      888R   
 888E  888E d8eeeee88888eer 9888        888E '888&   .u./"888&   8888L        888R   
 888E  888E        8888R    ?8888u../   888E  9888. d888" Y888*" '8888c. .+  .888B . 
m888N= 888>        8888R     "8888P'  '"888*" 4888" ` "Y   Y"     "88888%    ^*888%  
 `Y"   888      "*%%%%%%**~    "P'       ""    ""                   "YP'       "%    
      J88"                                                                           
      @%                                                                             
    :"                                                                               
If you want to contribute, visit the creator's GitHub: https://github.com/h4ckxel
    """
    ascii_label = tk.Label(window, text=ascii_art, foreground="lime", background="black", font=("Consolas", 8))
    ascii_label.pack(pady=5)

    # etiquetas
    ip_label = ttk.Label(window, text="Dirección IP:")
    ip_label.pack(pady=5)
    ip_entry = tk.Entry(window, width=30, bg="black", fg="lime", insertbackground="lime", font=("Consolas", 10))
    ip_entry.pack(pady=5)
    ip_entry.insert(0, '192.168.100.34')  # llenar el campo con la IP

    start_port_label = ttk.Label(window, text="Puerto inicial:")
    start_port_label.pack(pady=5)
    start_port_entry = tk.Entry(window, width=10, bg="black", fg="lime", insertbackground="lime", font=("Consolas", 10))
    start_port_entry.pack(pady=5)
    start_port_entry.insert(0, '135')  # llenar el puerto inicial

    end_port_label = ttk.Label(window, text="Puerto final:")
    end_port_label.pack(pady=5)
    end_port_entry = tk.Entry(window, width=10, bg="black", fg="lime", insertbackground="lime", font=("Consolas", 10))
    end_port_entry.pack(pady=5)
    end_port_entry.insert(0, '63080')  # llenar el puerto final

    # boton de escaneo
    scan_button = ttk.Button(window, text="Iniciar Escaneo", command=lambda: on_scan_button_click(ip_entry, start_port_entry, end_port_entry, result_text))
    scan_button.pack(pady=20)

    # caja de texto para mostrar resultados
    result_text = scrolledtext.ScrolledText(window, width=70, height=15, bg="black", fg="lime", font=("Consolas", 10))
    result_text.pack(pady=10)

    # tag
    made_by_label = ttk.Label(window, text="--------------------> Modified by </H4ckxel> <-----------------", foreground="red", background="black", font=("Consolas", 12, "bold"))
    made_by_label.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
