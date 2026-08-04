import os
import re

# Ruta base del repositorio
PROJECT_DIR = "/home/rpando/Documentos/GitHub/RicardoWebPage-Agosto2026"

def apply_patch():
    print(f"Buscando proyecto en: {PROJECT_DIR}\n")
    
    index_path = os.path.join(PROJECT_DIR, "index.html")
    script_path = os.path.join(PROJECT_DIR, "js", "script.js")

    # 1. Modificar index.html
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            html = f.read()

        # Añadir 'checked' al checkbox del idioma
        html = re.sub(
            r'''(<input[^>]*id=["']lang-switch["'][^>]*)(?<!checked)(>)''',
            r'\1 checked\2',
            html,
            count=1,
            flags=re.IGNORECASE
        )
        # Fallback por si no tiene id="lang-switch" sino que es un checkbox cualquiera
        if "checked" not in html:
             html = re.sub(
                r'''(<input[^>]*type=["']checkbox["'][^>]*)(?<!checked)(>)''',
                r'\1 checked\2',
                html,
                count=1,
                flags=re.IGNORECASE
            )

        # Cambiar la bandera/texto inicial a 🇬🇧
        # CORRECCIÓN: Uso de comillas triples r'''...''' para evitar el SyntaxError
        html = re.sub(r'''(<[^>]*id=["']lang-label["'][^>]*>\s*)🇪🇸(\s*</)''', r'\1🇬🇧\2', html, count=1, flags=re.IGNORECASE)
        
        # Reemplazos en caso de que esté estructurado de otra forma
        html = html.replace(">🇪🇸<", ">🇬🇧<")
        html = html.replace("> 🇪🇸 <", "> 🇬🇧 <")
        html = html.replace("🇪🇸", "🇬🇧", 1) # Fallback general para el primer '🇪🇸' que encuentre (usualmente el label)

        with open(index_path, "w", encoding="utf-8") as f:
            f.write(html)
        print("[+] index.html modificado: Interruptor activado por defecto y etiqueta inicial cambiada a 🇬🇧.")
    else:
        print(f"[!] Error: No se encontró {index_path}")

    # 2. Modificar js/script.js
    if os.path.exists(script_path):
        with open(script_path, "r", encoding="utf-8") as f:
            js = f.read()

        # Cambiar el idioma por defecto en el localStorage fallback
        js_new = js.replace(
            "localStorage.getItem('lang') || '🇪🇸'",
            "localStorage.getItem('lang') || '🇬🇧'"
        )

        with open(script_path, "w", encoding="utf-8") as f:
            f.write(js_new)
        
        if js != js_new:
            print("[+] js/script.js modificado: Lógica de idioma inicial cambiada a 🇬🇧.")
        else:
            print("[~] js/script.js no requirió cambios o ya tenía 🇬🇧 por defecto.")
    else:
        print(f"[!] Error: No se encontró {script_path}")

if __name__ == '__main__':
    apply_patch()
    print("\n¡Operación finalizada!")