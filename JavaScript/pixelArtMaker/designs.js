//////////////////////////****CONSTANTE**********************

// constante pour formation grille
const grid = document.getElementById("pixelCanvas");
const gridSizeInput = document.getElementById("gridSizeInput");
let sizeDisplay = document.getElementById("sizeDisplay");
const boutonEnvoyer = document.getElementById("boutonEnvoyer");

// constante pour couleur pixel
let inputCouleur = document.getElementById("inputCouleur");
const palette = document.getElementById("palette");
const erase = document.getElementById("erase");
let colorArray = [];

//////////////////////////****FONCTION**********************

//*************** CRÉATION DE LA GRILLE

gridSizeInput.addEventListener("change", function (e) {
  grid.innerHTML = " ";
  e.preventDefault();
  fabricationGrille(e.target.value);
});

function fabricationGrille(amount) {
  grid.innerHTML = "";
  sizeDisplay.innerText = `${amount}x${amount}`;
  for (let i = 0; i < sizeDisplay.value; i++) {
    const row = grid.insertRow(0);
    for (let j = 0; j < sizeDisplay.value; j++) {
      row.insertCell(0);
    }
  }
}

const dimension = (e) => {
  const gridSizeInput = document.getElementById("gridSizeInput").value;
  document.getElementById("sizeDisplay").value = gridSizeInput;
};

//*************** CRAYON À DESSIN

if (window.screen.width < 600) {
  grid.addEventListener("touch", function (e) {
    if (e.target.nodeName === "TD") {
      e.target.style.backgroundColor = getRandomColor();
    }
  });
} else {
  grid.addEventListener("mouseover", function (e) {
    if (e.target.nodeName === "TD") {
      e.target.style.backgroundColor = getRandomColor();
    }
  });
}

grid.addEventListener("mouseover", function (e) {
  if (e.target.nodeName === "TD") {
    e.target.style.backgroundColor = getRandomColor();
  }
});

function getRandomColor(e) {
  let letters = "0123456789ABCDEF";
  if (colorArray.length === 0) {
    let color = "#";
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }
  if (colorArray.length > 0) {
    const color = colorArray[Math.floor(Math.random() * colorArray.length)];
    return color;
  }
}

//*************** ÉLÉMENT PALETTE

document
  .getElementById("inputCouleur")
  .addEventListener("change", ajoutCouleur);

function ajoutCouleur(e) {
  colorArray.push(e.target.value);
  initializeColorDisplay();
}

const initializeColorDisplay = () => {
  palette.innerHTML = "";
  colorArray.length > 0
    ? (erase.style.visibility = "visible")
    : (erase.style.visibility = "hidden");

  for (let idx = 0; idx < colorArray.length; idx++) {
    const color = document.createElement("div");
    color.style.backgroundColor = colorArray[idx];
    color.style.height = "35px";
    color.style.width = "35px";
    palette.appendChild(color);
  }
};

erase.addEventListener("click", () => {
  palette.innerHTML = "";
  colorArray = [];
  erase.style.visibility = "hidden";
});

///*************** test référence

function maFonction() {
  alert("Pas facile de faire un pixel art maker quand t'es une newbie");
}

document.getElementById("titre").addEventListener("click", maFonction);
