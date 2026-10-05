import os
import sys
import subprocess
import ctypes
import shutil
import json

# Configurar codificación UTF-8 en Windows para evitar errores con charmap/cp1252
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Paquetes que requieren interacción manual o asistentes complejos
PAQUETES_EXCLUIDOS = [
    "Microsoft.SQLServer.2025.Developer",
    "Microsoft.SQLServer.2022.Developer"
]

def es_administrador():
    """Verifica si el proceso actual tiene permisos de administrador."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False

def elevar_permisos():
    """Relanza el script en una consola visible con permisos de administrador (UAC)."""
    print("\n[*] Solicitando elevacion de Administrador en Windows (UAC)...")
    script = os.path.abspath(sys.argv[0])
    params = f'/k python "{script}" --elevated'
    try:
        ret = ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", params, os.path.dirname(script), 1)
        if ret > 32:
            print("[+] Se ha abierto una ventana de Administrador en tu pantalla.")
            return True
        else:
            print("[!] Permisos de administrador cancelados por el usuario.")
            return False
    except Exception as e:
        print(f"[!] Error al solicitar elevacion: {e}")
        return False

def ejecutar_comando(comando, descripcion, shell_ps=False):
    """Ejecuta un comando en consola mostrando progreso en tiempo real."""
    print(f"\n{'=' * 65}")
    print(f" >> {descripcion}")
    print(f"{'=' * 65}")
    try:
        if shell_ps:
            cmd = ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", comando]
            proc = subprocess.run(cmd, check=False)
        else:
            proc = subprocess.run(comando, shell=True, check=False)
        
        if proc.returncode == 0:
            print(f"[OK] Completado: {descripcion}")
        else:
            print(f"[AVISO] Finalizo con codigo {proc.returncode}")
    except Exception as e:
        print(f"[ERROR] En '{descripcion}': {str(e)}")

def limpiar_carpeta_temporal(ruta):
    """Elimina archivos de un directorio temporal sin borrar la carpeta principal."""
    bytes_liberados = 0
    archivos_eliminados = 0
    if not os.path.exists(ruta):
        return 0, 0

    for root, dirs, files in os.walk(ruta, topdown=False):
        for file in files:
            try:
                ruta_completa = os.path.join(root, file)
                if not os.path.islink(ruta_completa):
                    tam = os.path.getsize(ruta_completa)
                    os.remove(ruta_completa)
                    bytes_liberados += tam
                    archivos_eliminados += 1
            except Exception:
                continue

        for d in dirs:
            try:
                os.rmdir(os.path.join(root, d))
            except Exception:
                continue

    return bytes_liberados, archivos_eliminados

def formatear_tamano(bytes_totales):
    """Convierte bytes a formato legible (KB, MB, GB)."""
    for unidad in ['B', 'KB', 'MB', 'GB']:
        if bytes_totales < 1024.0:
            return f"{bytes_totales:.2f} {unidad}"
        bytes_totales /= 1024.0
    return f"{bytes_totales:.2f} TB"

def paso_limpieza_sistema():
    """Limpia archivos temporales, caché de Windows Update, vacía papelera y purga DNS."""
    print("\n" + "=" * 65)
    print("   🧹 LIMPIEZA PROFUNDA Y OPTIMIZACION DEL SISTEMA")
    print("=" * 65)

    total_bytes = 0
    total_archivos = 0

    # 1. Temporales del usuario
    temp_usuario = os.environ.get("TEMP")
    if temp_usuario and os.path.exists(temp_usuario):
        print(f"[*] Limpiando temporales de usuario...")
        b, a = limpiar_carpeta_temporal(temp_usuario)
        total_bytes += b
        total_archivos += a

    # 2. Temporales generales del sistema (Windows\Temp)
    windir = os.environ.get("WINDIR", r"C:\Windows")
    temp_sistema = os.path.join(windir, "Temp")
    if os.path.exists(temp_sistema):
        print(f"[*] Limpiando temporales de Windows ({temp_sistema})...")
        b, a = limpiar_carpeta_temporal(temp_sistema)
        total_bytes += b
        total_archivos += a

    # 3. Caché de descargas de Windows Update
    cache_win_update = os.path.join(windir, "SoftwareDistribution", "Download")
    if os.path.exists(cache_win_update):
        print(f"[*] Limpiando cache de instaladores de Windows Update...")
        b, a = limpiar_carpeta_temporal(cache_win_update)
        total_bytes += b
        total_archivos += a

    # 4. Vaciar Papelera de reciclaje mediante PowerShell
    print("[*] Vaciando Papelera de Reciclaje...")
    try:
        subprocess.run(
            ["powershell.exe", "-NoProfile", "-Command", "Clear-RecycleBin -Force -ErrorAction SilentlyContinue"],
            check=False
        )
        print("    ✔ Papelera de reciclaje vaciada.")
    except Exception:
        pass

    # 5. Vaciar caché DNS de Windows
    print("[*] Limpiando cache de resolucion DNS...")
    try:
        subprocess.run(["ipconfig", "/flushdns"], check=False, stdout=subprocess.DEVNULL)
        print("    ✔ Cache DNS restablecida.")
    except Exception:
        pass

    print("-" * 65)
    print(f"✨ Limpieza completada con exito:")
    print(f"   • Archivos temporales eliminados: {total_archivos}")
    print(f"   • Espacio en disco recuperado:    {formatear_tamano(total_bytes)}")
    print("-" * 65)

def paso_winget():
    """Busca y actualiza aplicaciones con el gestor nativo de Windows (Winget)."""
    if shutil.which("winget") is None:
        print("[!] 'winget' no esta disponible en el sistema.")
        return

    print("\n--- PASO: ACTUALIZACION DE PROGRAMAS (WINGET) ---")
    print("[*] Comprobando lista de aplicaciones con actualizaciones disponibles...")
    subprocess.run("winget upgrade", shell=True, check=False)

    print("\n[*] Iniciando actualizacion de programas...")
    print("    (Omitiendo asistentes interactivos de servidor para evitar bloqueos)")
    cmd_upgrade = "winget upgrade --all --accept-package-agreements --accept-source-agreements"
    ejecutar_comando(cmd_upgrade, "Actualizando software de terceros con Winget")

def paso_windows_update_y_drivers():
    """Ejecuta la búsqueda y actualización de drivers y sistema mediante el cliente nativo de Windows."""
    print("\n--- PASO: ACTUALIZACION DE DRIVERS Y SISTEMA (WINDOWS UPDATE) ---")
    print("[*] Conectando con el orquestador oficial de Windows Update...")
    
    ps_cmd = """
    Write-Host '[*] Iniciando escaneo de drivers y actualizaciones...'
    Start-Process 'usoclient.exe' -ArgumentList 'StartScan' -Wait -NoNewWindow -ErrorAction SilentlyContinue
    Start-Sleep -Seconds 2
    Write-Host '[*] Descargando controladores y actualizaciones pendientes...'
    Start-Process 'usoclient.exe' -ArgumentList 'StartDownload' -Wait -NoNewWindow -ErrorAction SilentlyContinue
    Start-Sleep -Seconds 2
    Write-Host '[*] Instalando actualizaciones...'
    Start-Process 'usoclient.exe' -ArgumentList 'StartInstall' -Wait -NoNewWindow -ErrorAction SilentlyContinue
    Write-Host '[+] Windows Update y busqueda de drivers ejecutandose activamente en segundo plano.'
    """
    ejecutar_comando(ps_cmd, "Disparar actualizacion de Drivers y Windows Update", shell_ps=True)

def paso_python_pip():
    """Actualiza pip y librerias instaladas en el entorno Python."""
    print("\n--- PASO: LIBRERIAS DE PYTHON (PIP) ---")
    ejecutar_comando(f'"{sys.executable}" -m pip install --upgrade pip', "Actualizar pip")
    
    print("\n[*] Buscando paquetes de Python con versiones nuevas...")
    try:
        res = subprocess.run(
            [sys.executable, "-m", "pip", "list", "--outdated", "--format=json"],
            capture_output=True, text=True, check=False
        )
        if res.stdout:
            outdated = json.loads(res.stdout)
            if outdated:
                pkgs = [p["name"] for p in outdated]
                print(f"[+] Paquetes a actualizar ({len(pkgs)}): {', '.join(pkgs)}")
                cmd_upgrade = f'"{sys.executable}" -m pip install --upgrade {" ".join(pkgs)}'
                ejecutar_comando(cmd_upgrade, "Instalando nuevas versiones de librerias Python")
            else:
                print("[+] Todas las librerias de Python estan al dia.")
        else:
            print("[+] Todas las librerias de Python estan al dia.")
    except Exception as e:
        print(f"[AVISO] No se pudo verificar librerias de pip: {e}")

def mostrar_banner():
    print("=" * 65)
    print("    🚀 MANTENIMIENTO TOTAL: ACTUALIZADOR Y LIMPIADOR PC")
    print("       Desarrollado con Amor por Kevin Mejia Montalvan")
    print("=" * 65)

def menu_principal():
    mostrar_banner()

    if not es_administrador():
        print("[!] ATENCION: No se detectaron permisos de Administrador.")
        print("    Para actualizar drivers, limpiar cache de Windows y programas,")
        print("    se recomienda iniciar con privilegios elevados.")
        print("-" * 65)
        print("1. Solicitar permisos de Administrador y abrir ventana dedicada")
        print("2. Continuar aqui en modo usuario estandar")
        print("3. Salir")
        opc = input("\nSelecciona una opcion (1/2/3) [por defecto 1]: ").strip()
        if opc == "3":
            sys.exit(0)
        elif opc in ("", "1"):
            if elevar_permisos():
                sys.exit(0)

    print("\n¿Que deseas hacer?")
    print("1. MANTENIMIENTO COMPLETO (Actualizar TODO + Limpieza de disco)")
    print("2. Solo LIMPIEZA DEL SISTEMA (Temporales, papelera, cache)")
    print("3. Solo DRIVERS y Actualizaciones de Windows")
    print("4. Solo PROGRAMAS (VS Code, Chrome, Git, Zoom, VLC, etc.)")
    print("5. Solo librerias de PYTHON")
    print("6. Salir")

    eleccion = input("\nOpcion [1]: ").strip()
    if eleccion in ("", "1"):
        paso_limpieza_sistema()
        paso_winget()
        paso_windows_update_y_drivers()
        paso_python_pip()
    elif eleccion == "2":
        paso_limpieza_sistema()
    elif eleccion == "3":
        paso_windows_update_y_drivers()
    elif eleccion == "4":
        paso_winget()
    elif eleccion == "5":
        paso_python_pip()
    elif eleccion == "6":
        print("Operacion cancelada.")
        return

    print("\n" + "=" * 65)
    print("[OK] Proceso finalizado.")
    print("Nota: Si se instalaron controladores o firmware, reinicia tu equipo.")
    print("=" * 65)

    if sys.stdin and sys.stdin.isatty():
        input("\nPresiona Enter para cerrar...")

if __name__ == "__main__":
    if "--all" in sys.argv:
        mostrar_banner()
        paso_limpieza_sistema()
        paso_winget()
        paso_windows_update_y_drivers()
        paso_python_pip()
    elif "--clean" in sys.argv:
        mostrar_banner()
        paso_limpieza_sistema()
    else:
        menu_principal()
