function Verificar() {
    var data = new Date();
    var ano = data.getFullYear();
    var FAno = document.getElementById('txtano');
    var FSex = document.querySelector('div#res');

    if (FAno.value.length == 0 || FAno.value > ano) {
        window.alert('[ERRO] Verifique os dados e tente novamente!');
    } else {
        var fsex = document.getElementsByName('radsex');
        var idade = ano - Number(FAno.value);
        var gen = '';
        var img = document.createElement('img');
        img.setAttribute('id','foto');
        if (fsex[0].checked) {
            gen = 'Homem';
            if (idade >= 0 && idade < 10) {
                img.setAttribute('src', 'bebe.jpg');
            } else if (idade < 21) {
                img.setAttribute('src', 'jovem-m.jpg');
            } else if (idade < 50) {
                img.setAttribute('src', 'adulto-m.jpg');
            } else {
                img.setAttribute('src', 'idoso-m.jpg');
            }
        }
        else if (fsex[1].checked) {
            gen = 'Mulher';
            if (idade >= 0 && idade < 10) {
                img.setAttribute('src', 'bebe.jpg');
            } else if (idade < 21) {
                img.setAttribute('src', 'jovem-f.jpg');
            } else if (idade < 50) {
                img.setAttribute('src', 'adulto-f.jpg');
            } else {
                img.setAttribute('src', 'idoso-f.jpg');
            }
        }
        res.style.textAlign = 'center';
        res.innerHTML = `Detectamos ${gen} com ${idade} anos.`;
        res.appendChild(img);
    }
}