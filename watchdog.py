import os
import sys
import time
import subprocess
from datetime import datetime

# Asegurar codificación UTF-8 en consola de Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

def run_command(cmd: str):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)

def main():
    interval_seconds = 300 # 5 minutos por defecto
    if len(sys.argv) > 1:
        try:
            interval_seconds = int(sys.argv[1])
        except ValueError:
            pass

    print(f"🚀 Iniciando Local Watchdog & Cloud Sync cada {interval_seconds}s ({interval_seconds//60} mins)...")
    print("Este script ejecuta el análisis y sincroniza los resultados directamente con GitHub.")
    print("Presiona Ctrl+C para detenerlo.\n")

    while True:
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n[{now_str}] 🔄 Sincronizando con GitHub y ejecutando ciclo...")

        # 1. Traer cambios recientes de la nube
        run_command("git pull --rebase origin main")

        # 2. Ejecutar análisis de Gemini y trading
        proc = subprocess.run([sys.executable, "-u", "main.py", "--run-once"], capture_output=False)

        # 3. Subir resultados actualizados a GitHub
        run_command("git add portfolio.json trading.log README.md")
        diff_check = run_command("git diff --staged --quiet")
        if diff_check.returncode != 0:
            commit_res = run_command('git commit -m "🤖 Ciclo local sincronizado con GitHub [skip ci]"')
            push_res = run_command("git push origin main")
            if push_res.returncode == 0:
                print("☁️ Cambios sincronizados con GitHub exitosamente.")
            else:
                print("⚠️ Error al hacer push a GitHub (se reintentará en el próximo ciclo).")
        else:
            print("ℹ️ Sin cambios en el portafolio para este ciclo.")

        print(f"⏳ Esperando {interval_seconds} segundos para el siguiente análisis...")
        time.sleep(interval_seconds)

if __name__ == "__main__":
    main()
