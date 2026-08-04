import os
import re

PROJECT_DIR = "/home/rpando/Documentos/GitHub/RicardoWebPage-Agosto2026"
HTML_FILE = os.path.join(PROJECT_DIR, "index.html")
JS_FILE = os.path.join(PROJECT_DIR, "js", "script.js")

def patch_html():
    if not os.path.exists(HTML_FILE):
        print(f"Error: No se encontró {HTML_FILE}")
        return
    
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Eliminar posibles etiquetas meta o iframes que fuercen la descarga HTML
    content = re.sub(r'<meta[^>]*http-equiv=["\']refresh["\'][^>]*CV_RICARDO[^>]*>', '<!-- Auto-descarga meta removida -->', content, flags=re.IGNORECASE)
    content = re.sub(r'<iframe[^>]*src=["\'][^"\']*CV_RICARDO[^"\']*["\'][^>]*></iframe>', '<!-- Auto-descarga iframe removida -->', content, flags=re.IGNORECASE)
    
    # Eliminar scripts inline que hagan el window.open
    content = re.sub(r"""<script>\s*window\.(?:location\.href|open)\s*=\s*['"](?:\./)?CV_RICARDO[^'"]*['"][^;]*;?\s*</script>""", '<!-- Script inline de auto-descarga removido -->', content, flags=re.IGNORECASE)
    
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print("index.html revisado y parcheado.")

def patch_js():
    if not os.path.exists(JS_FILE):
        print(f"Error: No se encontró {JS_FILE}")
        return
    
    with open(JS_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Comentar posibles descargas automáticas en el JS actual
    content = re.sub(r"""(window\.(?:location\.href|open)\s*=\s*['"](?:\./)?CV_RICARDO[^'"]*['"][^;]*;?)""", r'/* \1 (removido por parche) */', content)

    js_addition = """
// --- INICIO PARCHE: Descarga de CV al scrollear a Estudios ---
document.addEventListener("DOMContentLoaded", function() {
    // Intentar encontrar la sección de estudios
    const sectionEstudios = document.getElementById("estudios") || 
                            document.querySelector(".estudios") ||
                            Array.from(document.querySelectorAll("section")).find(el => el.textContent.toLowerCase().includes("estudios"));

    if (sectionEstudios) {
        let cvDescargado = false;
        
        const observer = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting && !cvDescargado) {
                cvDescargado = true; // Asegurar que solo se descargue una vez
                
                const link = document.createElement('a');
                link.href = 'CV_RICARDO_ARMANDO_PANDO_AYLLON_1.pdf';
                link.download = 'CV_RICARDO_ARMANDO_PANDO_AYLLON_1.pdf';
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
                
                observer.unobserve(sectionEstudios);
            }
        }, { threshold: 0.3 });

        observer.observe(sectionEstudios);
    } else {
        console.warn("No se encontro la seccion de Estudios. Asegurate de tener un id='estudios' en tu HTML.");
    }
});
// --- FIN PARCHE ---
"""
    if "Descarga de CV al scrollear a Estudios" not in content:
        with open(JS_FILE, "a", encoding="utf-8") as f:
            f.write(js_addition)
        print("script.js modificado exitosamente.")
    else:
        print("El parche ya había sido aplicado previamente en script.js.")

if __name__ == "__main__":
    patch_html()
    patch_js()