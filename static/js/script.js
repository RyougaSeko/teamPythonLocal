document.addEventListener("DOMContentLoaded", function() {
    console.log("JavaScript is working!!");
});

document.addEventListener("DOMContentLoaded", function() {
    let rollDiceButton = document.getElementById('rollDice'); // rollDiceボタンのIDを仮定
    if (rollDiceButton) {
        rollDiceButton.addEventListener('click', function(event) {
            event.preventDefault(); // ページのリロードを防ぐ
            console.log('rollDiceボタンがクリックされました！');
            const result = Math.floor(Math.random() * 6) + 1;
            let message;
            if (result >= 1 && result <= 3) {
                message = 'あなたの勝ち';
            } else if (result >= 4 && result <= 6) {
                message = '相手の勝ち';
            }
            document.querySelector('input[name="winner"]').value = message;
        });
    }
});