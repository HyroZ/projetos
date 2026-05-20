        function inserir(num) {
            var numero = document.getElementById('resultado').value;
            document.getElementById('resultado').value = numero + num;
        }

        function operacao(op) {
            var resultado = document.getElementById('resultado').value;
            if (resultado[resultado.length - 1] !== ' ') {
                document.getElementById('resultado').value = resultado + ' ' + op + ' ';
            }
        }

        function limpar() {
            document.getElementById('resultado').value = '';
        }

        function calcular() {
            var resultado = 
            document.getElementById('resultado').value;
            document.getElementById('resultado').value = eval(resultado.replace(/  /g, ' '));
        }