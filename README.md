<div align="center">

# ⚡ Escáner de Puertos - H4ckxel ⚡


<image src="images/Untitled video - Made with Clipchamp (3).mp4"/>

> "Port Scanning made easy by **H4ckxel**"
</div>

Este proyecto es una herramienta gráfica de escaneo de puertos construida con **Python** y **Tkinter**, diseñada para ayudar a los usuarios a verificar rápidamente qué puertos están abiertos en una dirección IP específica.

## 🚀 Funcionalidades

- Escaneo de puertos específico para un rango dado.
- Interface gráfica con estilo **hacker** para una experiencia interactiva y visualmente atractiva.
- Escaneo rápido utilizando **multithreading**.
- Personalizable: ingresa la dirección IP y el rango de puertos que deseas escanear.
- Experiencia optimizada con resultados en tiempo real.

![Scan Ports](https://media.giphy.com/media/QHE5gWI0QjqF2/giphy.gif)

---

## 📋 ¿Cómo usarlo?

### Requisitos previos

Antes de ejecutar la aplicación, asegúrate de tener instalado lo siguiente:

- **Python 3.x**.
- Módulos: `socket`, `threading`, `tkinter`, `concurrent.futures`.

Puedes instalarlos con el siguiente comando:

```bash
pip install tkinter
```

### Ejecución

1. Clona este repositorio:
   ```bash
   git clone https://github.com/h4ckxel/escaner-de-puertos.git
   ```
2. Navega hasta el directorio del proyecto:
   ```bash
   cd escaner-de-puertos
   ```
3. Ejecuta el script principal:
   ```bash
   python scanner.py
   ```

### GUI (Interfaz Gráfica)

- **IP**: Introduce la dirección IP que deseas escanear.
- **Puerto inicial**: El puerto desde el cual deseas iniciar el escaneo.
- **Puerto final**: El último puerto a escanear.
- Haz clic en **Iniciar Escaneo** para empezar a detectar los puertos abiertos.

---

## 🌟 Mejoras posibles

Aunque el escáner funciona de manera eficiente, hay varias mejoras que podrías implementar:

1. **Compatibilidad multiplataforma**: Actualmente la aplicación funciona en Windows, pero la interfaz puede necesitar ajustes para Linux y macOS. Una futura actualización incluirá estos cambios.
2. **Reporte en archivo**: Crear un reporte al finalizar el escaneo, exportando los resultados a un archivo `.txt` o `.csv`.
3. **Optimización del tiempo de escaneo**: Se puede ajustar el tiempo de espera (`timeout`) en función de la velocidad de la red.
4. **Seguridad**: Incluir notificaciones de advertencia si se detecta un comportamiento inusual durante el escaneo.
5. **Detección de Servicios**: Agregar la funcionalidad de detección de servicios asociados a los puertos escaneados (por ejemplo, HTTP, SSH).

---

## 🔧 Futuras Actualizaciones

- **Versión para Linux**: Próximamente se lanzará una versión optimizada para usuarios de Linux, con instalación automática de dependencias y ajustes en la GUI para un mejor rendimiento en escritorios basados en GNOME y KDE.
- **Detección de Sistema Operativo**: Se añadirá una función para detectar automáticamente el sistema operativo del objetivo, junto con información adicional sobre el estado de la red.

---

## 📂 Estructura del Proyecto

```bash
📦port-scanner-h4ckxel
 ┣ 📜port_scanner.py           # Código fuente principal
 ┣ 📜README.md                 # Este archivo
```

---

## 💻 Ejemplo de Uso

### Escaneo de un puerto específico:
```bash
192.168.100.x
Puerto inicial: 135
Puerto final: 63080
```

**Resultado**: Muestra todos los puertos abiertos entre los puertos 135 y 63080 para la IP 192.168.100.x.

---

## 🔗 Contribuciones

Si te gustaría contribuir a este proyecto, por favor visita mi [GitHub](https://github.com/h4ckxel) y siéntete libre de hacer pull requests o reportar problemas.

<div align="center">

![Contribute](https://media.giphy.com/media/l1J9u3TZfpmeDLkDq/giphy.gif)

</div>

---

## Créditos

**Modificado por H4ckxel** — Proyecto original inspirado en la personalización de herramientas de red para entornos de hacking.

---

### 📧 Contacto

¡Para más información o sugerencias, no dudes en contactarme a través de mi perfil de GitHub! [H4ckxel](https://github.com/h4ckxel)

---

#### ¡Disfruta de tu escaneo! 😎

---


_Añade aquí tus propias capturas o GIFs que muestren el escáner en acción._

---

### Inspiración:

Este proyecto es parte de una serie de herramientas de red que buscan mejorar la comprensión del escaneo y la seguridad en redes.

---

**Modified by**: `h4ckxel`

---
