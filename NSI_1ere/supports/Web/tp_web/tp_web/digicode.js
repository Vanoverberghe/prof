function afficher(chiffre) {
  var el = document.getElementById("code");
  var code = el.textContent.split("*")[0];

  if (code.length < 4) {
    code = code + chiffre;
    el.textContent = code + ("*".repeat(4 - code.length));
  }
}
