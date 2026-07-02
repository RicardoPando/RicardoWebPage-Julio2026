// Función para cambiar entre modos claro y oscuro
function toggleDarkMode() {
    const body = document.body;
    body.classList.toggle('dark-mode');
    
    // Almacenar la preferencia del usuario en localStorage
    if (body.classList.contains('dark-mode')) {
        localStorage.setItem('dark-mode', 'enabled');
    } else {
        localStorage.setItem('dark-mode', 'disabled');
    }
}

// Obtener la preferencia de modo almacenada en localStorage
const savedMode = localStorage.getItem('dark-mode');

if (savedMode === 'enabled') {
    document.body.classList.add('dark-mode');
}

// Manejar eventos de cambio de conmutador
const modeSwitch = document.getElementById('mode-switch');
modeSwitch.addEventListener('change', toggleDarkMode);

// Selecciona el elemento de etiqueta (label) por su ID
const modeSwitchLabel = document.querySelector('.switch-label');

// Agrega un evento de escucha al cambio del interruptor
document.querySelector('#mode-switch').addEventListener('change', function() {
  // Verifica si el interruptor está activado o desactivado
  if (this.checked) {
    // Cambia el contenido del elemento a "🌙" cuando está activado
    modeSwitchLabel.textContent = "🌙";
    const menu = document.getElementById('menu')
    menu.style.color = 'black'; 

    const barras_menu = document.getElementById('icon_menu'); // Obtén el elemento SVG por su ID
// Luego, puedes acceder a los elementos rect dentro del SVG utilizando querySelectorAll
    const rects = barras_menu.querySelectorAll('rect');
    // Ahora, puedes trabajar con los elementos rects como una colección NodeList
    // Por ejemplo, cambiar su color de fondo a blanco
    rects.forEach(rect => {
        rect.setAttribute('fill', 'white');
    });

    const logoUPC = document.getElementById('logo-upc'); // Obtén el elemento SVG por su ID
    const pathElement = logoUPC.querySelector('path'); // Obtén el elemento <path> dentro del SVG

    // Cambia el color de relleno a blanco
    pathElement.setAttribute('fill', 'white');

    const svgElement = document.getElementById('imagenExporPDF'); // Obtén el elemento SVG por su ID
    const paths = svgElement.querySelectorAll('path'); // Obtén todas las rutas dentro del SVG
    
    // Itera a través de las rutas y cambia su color de relleno a blanco
    for (let i = 0; i < paths.length; i++) {
        paths[i].setAttribute('fill', 'white');
    }
    





  } else {
    // Cambia el contenido del elemento a "☀️" cuando está desactivado
    modeSwitchLabel.textContent = "☀️";
    const barras_menu = document.getElementById('icon_menu'); // Obtén el elemento SVG por su ID
    // Luego, puedes acceder a los elementos rect dentro del SVG utilizando querySelectorAll
        const rects = barras_menu.querySelectorAll('rect');
        // Ahora, puedes trabajar con los elementos rects como una colección NodeList
        // Por ejemplo, cambiar su color de fondo a blanco
        rects.forEach(rect => {
            rect.setAttribute('fill', 'black');
        });
        const logoUPC = document.getElementById('logo-upc'); // Obtén el elemento SVG por su ID
        const pathElement = logoUPC.querySelector('path'); // Obtén el elemento <path> dentro del SVG
          
        // Cambia el color de relleno a blanco
        pathElement.setAttribute('fill', 'black');

        const svgElement = document.getElementById('imagenExporPDF'); // Obtén el elemento SVG por su ID
        const paths = svgElement.querySelectorAll('path'); // Obtén todas las rutas dentro del SVG
        
        // Itera a través de las rutas y cambia su color de relleno a blanco
        for (let i = 0; i < paths.length; i++) {
            paths[i].setAttribute('fill', 'black');
        }
  }
});

document.getElementById("icon_menu").addEventListener("click", mostrar_menu);

function mostrar_menu(){

    document.querySelector(".Menu").classList.toggle("mostrar_menu");
    
}

document.addEventListener("DOMContentLoaded", function() {
    var button = document.getElementById("toggleButton");
    var seccion = document.getElementById("SeccionContacto");
    var label = document.getElementById("SeccionContacto label");
    var input = document.getElementById("SeccionContacto input");
    var textarea = document.getElementById("SeccionContacto textarea");

  
    button.addEventListener("click", function() {
      // Alternar la visibilidad de la sección
      if (seccion.style.display === "none" || seccion.style.display === "") {
        seccion.style.display = "block";
        label.style.display = "block";
        input.style.display = "block";
        textarea.style.display = "block";
      } else {
        seccion.style.display = "none";
        label.style.display = "none";
        input.style.display = "none";
        textarea.style.display = "none";
      }
    });
  });