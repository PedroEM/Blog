window.addEventListener('DOMContentLoaded', () => {
  let scrollPos = 0;
  const mainNav = document.getElementById('mainNav');
  const headerHeight = mainNav.clientHeight;
  window.addEventListener('scroll', function() {
      const currentTop = document.body.getBoundingClientRect().top * -1;
      if ( currentTop < scrollPos) {
          // Scrolling Up
          if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
              mainNav.classList.add('is-visible');
          } else {
              console.log(123);
              mainNav.classList.remove('is-visible', 'is-fixed');
          }
      } else {
          // Scrolling Down
          mainNav.classList.remove(['is-visible']);
          if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
              mainNav.classList.add('is-fixed');
          }
      }
      scrollPos = currentTop;
  });



  // Función para obtener los precios de las monedas desde una API
function obtenerPreciosMonedas() {
  // Aquí debes realizar una solicitud a una API para obtener los precios actualizados de las monedas
  // En este ejemplo, se utiliza una simulación de datos aleatorios para ilustrar el concepto

  const monedas = [
    { nombre: 'Dólar Oficial', codigo: 'USD' },
    { nombre: 'Euro', codigo: 'EUR' },
    { nombre: 'Libra Esterlina', codigo: 'GBP' },
    { nombre: 'Yen Japonés', codigo: 'JPY' },
    { nombre: 'Franco Suizo', codigo: 'CHF' },
    { nombre: 'Dólar Canadiense', codigo: 'CAD' },
    { nombre: 'Dólar Australiano', codigo: 'AUD' },
    { nombre: 'Peso Mexicano', codigo: 'MXN' },
    { nombre: 'Real Brasileño', codigo: 'BRL' },
    { nombre: 'Rublo Ruso', codigo: 'RUB' }
  ];

  // Simulación de precios aleatorios para las monedas
  const preciosMonedas = {};
  monedas.forEach(moneda => {
    preciosMonedas[moneda.nombre] = getRandomPrice();
  });

  return preciosMonedas;
}

// Función para obtener los precios de las criptomonedas desde una API
function obtenerPreciosCriptomonedas() {
  // Aquí debes realizar una solicitud a una API para obtener los precios actualizados de las criptomonedas
  // En este ejemplo, se utiliza una simulación de datos aleatorios para ilustrar el concepto

  const criptomonedas = [
    { nombre: 'Bitcoin', codigo: 'BTC' },
    { nombre: 'Ethereum', codigo: 'ETH' },
    { nombre: 'Binance Coin', codigo: 'BNB' },
    { nombre: 'Cardano', codigo: 'ADA' },
    { nombre: 'XRP', codigo: 'XRP' }
  ];

  // Simulación de precios aleatorios para las criptomonedas
  const preciosCriptomonedas = {};
  criptomonedas.forEach(cripto => {
    preciosCriptomonedas[cripto.nombre] = getRandomPrice();
  });

  return preciosCriptomonedas;
}

// Función para generar un precio aleatorio
function getRandomPrice() {
  return (Math.random() * (50000 - 100) + 100).toFixed(2); // Genera un número aleatorio entre 100 y 50000 con 2 decimales
}

// Función para actualizar la lista de monedas con los precios
function actualizarListaMonedas() {
  const preciosMonedas = obtenerPreciosMonedas();
  const listaMonedas = document.getElementById('currency-list');

  // Limpia la lista antes de agregar los nuevos elementos
  listaMonedas.innerHTML = '';

  // Agrega dinámicamente los elementos de la lista con los precios de las monedas
  for (const moneda in preciosMonedas) {
    const li = document.createElement('li');
    const spanMoneda = document.createElement('span');
    const spanPrecio = document.createElement('span');

    spanMoneda.className = 'currency';
    spanMoneda.textContent = moneda;
    spanPrecio.className = 'price';
    spanPrecio.textContent = preciosMonedas[moneda];

    li.appendChild(spanMoneda);
    li.appendChild(spanPrecio);
    listaMonedas.appendChild(li);
  }
}

// Función para actualizar la lista de criptomonedas con los precios
function actualizarListaCriptomonedas() {
  const preciosCriptomonedas = obtenerPreciosCriptomonedas();
  const listaCriptomonedas = document.getElementById('crypto-list');

  // Limpia la lista antes de agregar los nuevos elementos
  listaCriptomonedas.innerHTML = '';

  // Agrega dinámicamente los elementos de la lista con los precios de las criptomonedas
  for (const cripto in preciosCriptomonedas) {
    const li = document.createElement('li');
    const spanCripto = document.createElement('span');
    const spanPrecio = document.createElement('span');

    spanCripto.className = 'crypto';
    spanCripto.textContent = cripto;
    spanPrecio.className = 'price';
    spanPrecio.textContent = preciosCriptomonedas[cripto];

    li.appendChild(spanCripto);
    li.appendChild(spanPrecio);
    listaCriptomonedas.appendChild(li);
  }
}

// Llama a las funciones para actualizar los precios inicialmente
actualizarListaMonedas();
actualizarListaCriptomonedas();

  

})
