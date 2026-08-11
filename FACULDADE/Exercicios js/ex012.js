const meses = [
    'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
    'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
];
var hora = new Date().getHours();
var ano = new Date().getFullYear();
var mes = new Date().getMonth() + 1;
var dia = new Date().getDate();
console.log(`Agora são ${hora} horas do dia ${dia} de ${meses[mes - 1]} de ${ano}.`);
if (6 <= hora && hora < 12) {
    console.log("Bom dia!");
}else if (12 <= hora && hora < 18) {
    console.log("Boa tarde!");  
} else if (18 <= hora && hora < 24) {
    console.log("Boa noite!")
} else {
    console.log("Boa madrugada!");
}