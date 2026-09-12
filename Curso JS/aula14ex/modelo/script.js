function gerarTabuada() {
    let numero = document.getElementById("numero").value;
    let res = document.getElementById("res");
    res.innerHTML = "";
    if (numero == "") {
        res.innerHTML = "Por favor, insira um número.";
        return;
    }
    else {
        Number(numero);
        for (let i = 1; i <= 10; i++) {
            let resultado = numero * i;
            res.innerHTML += `${numero} x ${i} = ${resultado}<br>`;
        }
    }
}