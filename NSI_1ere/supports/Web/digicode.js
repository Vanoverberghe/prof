
b0 = document.getElementById("b0");
b0.addEventListener("click", () => {afficher(0);});

function afficher(chiffre) {
  console.trace("afficher appelé avec", chiffre);
  var el = document.getElementById("code");
  var code = el.textContent.split("*")[0];

  if (code.length < 4) {
    code = code + chiffre;
    el.textContent = code + ("*".repeat(4 - code.length));
  }
};