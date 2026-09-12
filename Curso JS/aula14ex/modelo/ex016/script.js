function contar() {
    let i = document.getElementById('inicio').value;
    let f = document.getElementById('fim').value;
    let p = document.getElementById('passo').value;
    let res = document.getElementById('res');
    if (numberI == 0 || numberF == 0 || numberP == 0) {
        res.innerHTML = 'Impossível contar!';
        alert('[ERRO] Faltam dados!');
    }
    else {
        numberI = Number(i);
        numberF = Number(f);
        numberP = Number(p);
        res.innerHTML = 'Contando: <br>';
        if ( numberI < numberF) {
            for (let c = numberI; c <= numberF; c += numberP) {
                res.innerHTML += `${c} \u{1F449}`;
            }
        } else {
            for (let c = numberI; c >= numberF; c -= numberP) {
                res.innerHTML += `${c} \u{1F449}`;
            }
        }
        res.innerHTML += `\u{1F3C1}`;
    }

    
}
