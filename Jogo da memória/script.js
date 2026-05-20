const cardsArray = [
 'Animal1','Animal2','Animal3','Animal4','Animal5',
 'Animal6','Animal7','Animal8','Animal9','Animal10'
];

// duplica as cartas automaticamente
const gameCards = [...cardsArray, ...cardsArray];

let firstCard = null, secondCard = null;
let score = 0;
let playerName = '';
let lockBoard = false;
let startTime;
let timerInterval;
let matchedPairs = 0;

function shuffle(array) {
    //Função para embaralhar as cartas
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

function startGame() {
    //Inicia o jogo
    playerName = document.getElementById('player-name').value.trim();
    if (playerName === '') {
        alert('Por favor, insira seu nome para começar o jogo.');
        return;
    }

    document.getElementById('game-setup').style.display = 'none';
    document.getElementById('game-info').style.display = 'block';
    document.getElementById('game-board').style.display = 'grid';
    document.getElementById('player-name-display').textContent = playerName;
    startTime = new Date();
    timerInterval = setInterval(updateTime, 1000);
    score = 0;
    matchedPairs = 0;
    document.getElementById('score-display').textContent = score;
    createBoard();
}

function createBoard() {
    // Cria o tabuleiro de jogo
    const board = document.getElementById('game-board');
    board.innerHTML = '';
        shuffle(gameCards);
        gameCards.forEach((card) => {
        const cardElement = document.createElement('div');
        cardElement.classList.add('card');
        const imgElement = document.createElement('img');
        imgElement.src = `../images/${card}.png`; //Ajusta o caminho da imagem conforme necessário
        imgElement.alt = card;
        cardElement.appendChild(imgElement);
        cardElement.dataset.card = card;
        cardElement.addEventListener('click', flipCard);
        board.appendChild(cardElement);
    });
}

function flipCard(cardElement, card) {
    // Lógica para virar a carta
    if (lockBoard || cardElement === firstCard) return;
    if (this === firstCard) return;

    const img = this.querySelector('img');
    img.style.display = 'block';

    if (!firstCard) {
        firstCard = this;
        return;
    }

    secondCard = this;
    lockBoard = true;

    if (firstCard.dataset.card.split('.')[0] === secondCard.dataset.card.split('.')[0]) {
        score += 10;
        matchedPairs++;
        firstCard.classList.add('vibrate');
        secondCard.classList.add('vibrate');
        setTimeout(() => {
            firstCard.removeEventListener('click', flipCard);
            secondCard.removeEventListener('click', flipCard);
            resetBoard();
        }, 200);
    } else {
        score -= 5;
        setTimeout(() => {
            firstCard.querySelector('img').style.display = 'none';
            secondCard.querySelector('img').style.display = 'none';
            resetBoard();
        }, 1000);
    }

    document.getElementById('score-display').textContent = score;
    checkWinCondition();
}

function resetBoard() {
    // Reseta o tabuleiro para a próxima jogada
    [firstCard, secondCard, lockBoard] = [null, null, false];
    document.querySelectorAll('.card').forEach(card => card.classList.remove('vibrate'));
}

function updateTime() {
    // atualiza o timer do jogo
    const currentTime = new Date();
    const elapsedTime = Math.floor((currentTime - startTime) / 1000);
    document.getElementById('time').textContent = elapsedTime;

    if (elapsedTime >= 120) {
        clearInterval(timerInterval);
        document.getElementById('game-message').textContent = 'Você perdeu! Mais sorte da próxima.';
        endGame();
    }
}

function checkWinCondition() {
    // Verifica se o jogador ganhou o jogo
    if (matchedPairs === 10) {
        clearInterval(timerInterval);
        const elapsedTime = Math.floor((new Date() - startTime) / 1000);
        document.getElementById('game-message').textContent = `Parabéns, ${playerName}! Você ganhou com uma pontuação de ${score} em ${elapsedTime} segundos!`;
        saveScore(playerName, score, elapsedTime);
        showHighScores();
        endGame();
    }

}

function saveScore(playerName, score, time) {
    // Salva a pontuação do jogador no localStorage
    const scores = JSON.parse(localStorage.getItem('memoryGameScores')) || [];
    scores.push({ playerName, score, time });
    scores.sort((a, b) => b.score - a.score || a.time - b.time);
    localStorage.setItem('memoryGameScores', JSON.stringify(scores));
}

function showHighScores() {
    // Exibe as pontuações mais altas
    const scores = JSON.parse(localStorage.getItem('memoryGameScores')) || [];
    const message = scores.slice(0, 5).map((score => `${score.playerName}: ${score.time} segundos`)).join('\n');
    document.getElementById('game-message').textContent += `\n\nTop 5 Pontuações:\n${message}`;
}

function restartGame() {
    // Reinicia o jogo
    clearInterval(timerInterval);
    document.getElementById('game-board').style.display = 'grid';
    document.getElementById('game-info').style.display = 'block';
    document.getElementById('game-message').style.display = '';
    startTime = new Date();
    timerInterval = setInterval(updateTime, 1000);
    score = 0;
    matchedPairs = 0;
    document.getElementById('score-display').textContent = score;
    createBoard();
}

function endGame() {
    // Finaliza o jogo
    document.getElementById('game-board').style.display = 'none';
    document.getElementById('game-info').style.display = 'none';
}

//Chamar a função para criar o tabuleiro quando a página carregar
createBoard();