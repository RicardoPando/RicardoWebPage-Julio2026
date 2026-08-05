import os
import re

def aplicar_parche_export():
    html_file = 'index.html'
    js_file = 'js/script.js'

    print("Iniciando la aplicación del parche para 'Export to PDF'...")

    # 1. Modificar index.html
    if os.path.exists(html_file):
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Agregamos el ID al elemento que contiene "Export to PDF" si no lo tiene
        if 'id="btnExportPDF"' not in html_content:
            # Buscar etiqueta <a> con "Export to PDF"
            html_content, count_a = re.subn(r'(<a[^>]*)(>\s*Export to PDF\s*</a>)', r'\1 id="btnExportPDF"\2', html_content, flags=re.IGNORECASE)
            
            # Si no encontró un <a>, buscar un <button> o <div> genérico
            if count_a == 0:
                html_content, count_btn = re.subn(r'(<button[^>]*)(>\s*Export to PDF\s*</button>)', r'\1 id="btnExportPDF"\2', html_content, flags=re.IGNORECASE)
                
                # Respaldo simple por si la estructura es diferente
                if count_btn == 0:
                    html_content = html_content.replace('>Export to PDF<', ' id="btnExportPDF">Export to PDF<')

            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"[OK] {html_file} modificado con éxito (ID agregado).")
        else:
            print(f"[INFO] El ID 'btnExportPDF' ya existe en {html_file}.")
    else:
        print(f"[ERROR] Archivo no encontrado: {html_file}")

    # 2. Modificar js/script.js
    if os.path.exists(js_file):
        with open(js_file, 'r', encoding='utf-8') as f:
            js_content = f.read()
        
        popup_js_export = '''
// Lógica para el botón "Export to PDF"
document.addEventListener("DOMContentLoaded", () => {
    const btnExportPDF = document.getElementById("btnExportPDF");
    const popupOverlay = document.getElementById("popupOverlay");
    const popupPaso1 = document.getElementById("popupPaso1");
    const popupPaso2 = document.getElementById("popupPaso2");

    if (btnExportPDF && popupOverlay && popupPaso1 && popupPaso2) {
        btnExportPDF.addEventListener("click", (e) => {
            e.preventDefault(); // Evita que la página salte
            
            // Mostrar el fondo oscuro del pop-up
            popupOverlay.classList.add("mostrar");
            
            // Ocultar la pregunta de "Luego/Descargar" (Paso 1)
            popupPaso1.classList.add("oculto");
            
            // Mostrar directamente la selección de idioma (Paso 2)
            popupPaso2.classList.remove("oculto");
        });
    }
});
'''
        if 'btnExportPDF' not in js_content:
            with open(js_file, 'a', encoding='utf-8') as f:
                f.write('\n' + popup_js_export)
            print(f"[OK] {js_file} modificado con éxito (Event Listener agregado).")
        else:
            print(f"[INFO] La lógica para 'btnExportPDF' ya existe en {js_file}.")
    else:
        print(f"[ERROR] Archivo no encontrado: {js_file}")

if __name__ == '__main__':
    aplicar_parche_export()
