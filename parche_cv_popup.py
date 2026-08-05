import os

def aplicar_parche():
    html_file = 'index.html'
    css_file = 'css/estilos.css'
    js_file = 'js/script.js'

    print("Iniciando la aplicación del parche...")

    # 1. Modificar index.html
    if os.path.exists(html_file):
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        popup_html = '''
<!-- Pop-up de Descarga de CV -->
<div id="popupOverlay" class="popup-overlay">
    <!-- Paso 1: Pregunta inicial -->
    <div id="popupPaso1" class="popup-content">
        <h3>¿Descargar la versión de pdf?</h3>
        <div class="popup-buttons">
            <button id="btnLuego" class="btn-secundario">Luego</button>
            <button id="btnDescargar" class="btn-primario">Descargar</button>
        </div>
    </div>
    
    <!-- Paso 2: Selección de idioma (Oculto por defecto) -->
    <div id="popupPaso2" class="popup-content oculto">
        <h3>Seleccione la versión</h3>
        <div class="popup-buttons">
            <button id="btnEs" class="btn-primario">Español</button>
            <button id="btnEn" class="btn-primario">English</button>
        </div>
    </div>
</div>
'''
        if 'id="popupOverlay"' not in html_content:
            html_content = html_content.replace('</body>', popup_html + '\n</body>')
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"[OK] {html_file} modificado con éxito.")
        else:
            print(f"[INFO] El pop-up ya parece existir en {html_file}.")
    else:
        print(f"[ERROR] Archivo no encontrado: {html_file}")

    # 2. Modificar css/estilos.css
    if os.path.exists(css_file):
        with open(css_file, 'r', encoding='utf-8') as f:
            css_content = f.read()
        
        popup_css = '''
/* --- Estilos del Pop-up --- */
.popup-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(5px);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 9999;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.3s ease, visibility 0.3s ease;
}
.popup-overlay.mostrar {
    opacity: 1;
    visibility: visible;
}
.popup-content {
    background-color: #ffffff;
    padding: 30px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    max-width: 400px;
    width: 90%;
}
.popup-content.oculto {
    display: none;
}
.popup-content h3 {
    margin-top: 0;
    margin-bottom: 20px;
    color: #333;
}
.popup-buttons {
    display: flex;
    justify-content: center;
    gap: 15px;
}
.popup-buttons button {
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-weight: bold;
    transition: background-color 0.2s ease;
}
.btn-primario {
    background-color: #0056b3;
    color: white;
}
.btn-primario:hover {
    background-color: #004494;
}
.btn-secundario {
    background-color: #e0e0e0;
    color: #333;
}
.btn-secundario:hover {
    background-color: #cccccc;
}
'''
        if '.popup-overlay' not in css_content:
            with open(css_file, 'a', encoding='utf-8') as f:
                f.write('\n' + popup_css)
            print(f"[OK] {css_file} modificado con éxito.")
        else:
            print(f"[INFO] Los estilos del pop-up ya existen en {css_file}.")
    else:
        print(f"[ERROR] Archivo no encontrado: {css_file}")

    # 3. Modificar js/script.js
    if os.path.exists(js_file):
        with open(js_file, 'r', encoding='utf-8') as f:
            js_content = f.read()
        
        popup_js = '''
// Lógica del Pop-up de Descarga
document.addEventListener("DOMContentLoaded", () => {
    const seccionEstudios = document.getElementById("estudios");
    const popupOverlay = document.getElementById("popupOverlay");
    const popupPaso1 = document.getElementById("popupPaso1");
    const popupPaso2 = document.getElementById("popupPaso2");
    
    const btnLuego = document.getElementById("btnLuego");
    const btnDescargar = document.getElementById("btnDescargar");
    const btnEs = document.getElementById("btnEs");
    const btnEn = document.getElementById("btnEn");

    let popupMostrado = false;

    const opcionesObserver = {
        root: null,
        threshold: 0.3
    };

    const mostrarPopup = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !popupMostrado) {
                if(popupOverlay) popupOverlay.classList.add("mostrar");
                popupMostrado = true;
            }
        });
    };

    if (seccionEstudios) {
        const observer = new IntersectionObserver(mostrarPopup, opcionesObserver);
        observer.observe(seccionEstudios);
    }

    if (btnLuego) {
        btnLuego.addEventListener("click", () => {
            popupOverlay.classList.remove("mostrar");
        });
    }

    if (btnDescargar) {
        btnDescargar.addEventListener("click", () => {
            popupPaso1.classList.add("oculto");
            popupPaso2.classList.remove("oculto");
        });
    }

    const ejecutarDescarga = (nombreArchivo) => {
        const link = document.createElement("a");
        link.href = nombreArchivo; 
        link.download = nombreArchivo;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        popupOverlay.classList.remove("mostrar");
    };

    if (btnEs) {
        btnEs.addEventListener("click", () => {
            ejecutarDescarga("CV_RICARDO_ARMANDO_PANDO_AYLLON_1_es.pdf");
        });
    }

    if (btnEn) {
        btnEn.addEventListener("click", () => {
            ejecutarDescarga("CV_RICARDO_ARMANDO_PANDO_AYLLON_1_en.pdf");
        });
    }
});
'''
        if 'popupOverlay' not in js_content:
            with open(js_file, 'a', encoding='utf-8') as f:
                f.write('\n' + popup_js)
            print(f"[OK] {js_file} modificado con éxito.")
        else:
            print(f"[INFO] La lógica del pop-up ya existe en {js_file}.")
    else:
        print(f"[ERROR] Archivo no encontrado: {js_file}")

if __name__ == '__main__':
    aplicar_parche()
