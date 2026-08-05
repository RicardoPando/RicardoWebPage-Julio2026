import os
import re

def aplicar_parche_fix_export():
    html_file = 'index.html'

    print("Iniciando la corrección del botón Exportar a PDF...")

    if os.path.exists(html_file):
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Patrón para buscar la etiqueta <a> con la ruta directa al PDF
        # y reemplazarla quitando la ruta y añadiendo el id="btnExportPDF"
        if 'href="./CV_RICARDO_ARMANDO_PANDO_AYLLON_1_es.pdf"' in html_content:
            html_content = html_content.replace(
                '<a href="./CV_RICARDO_ARMANDO_PANDO_AYLLON_1_es.pdf">', 
                '<a href="#" id="btnExportPDF">'
            )
            
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"[OK] {html_file} modificado con éxito. Se quitó la descarga directa.")
        else:
            print(f"[INFO] No se encontró el enlace directo al PDF en {html_file}.")
    else:
        print(f"[ERROR] Archivo no encontrado: {html_file}")

if __name__ == '__main__':
    aplicar_parche_fix_export()
