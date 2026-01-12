async function playCard(card) {
  const res = await fetch("/play", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ card }),
  });

  const data = await res.json();

  document.getElementById("status-text").innerText =
    `Você jogou ${data.player_card} — Oponente jogou ${data.bot_card}
Resultado: ${data.result}`;
}

function resetGame() {
  location.reload();
}
function playCard(cardName) {
  fetch("/play", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ card: cardName }),
  })
    .then((res) => res.json())
    .then((data) => {
      showBotCard(data.bot_card);
      showResult(data.winner);
    });
}
function showBotCard(cardName) {
  const botHand = document.getElementById("bot-hand");

  botHand.innerHTML = `
        <img src="/static/cards/${cardName}.png" class="card reveal">
    `;
}
function showResult(winner) {
  const status = document.getElementById("status-text");

  if (winner === "player") {
    status.innerText = "🎉 Você venceu a rodada!";
  } else if (winner === "bot") {
    status.innerText = "💀 O bot venceu!";
  } else {
    status.innerText = "😐 Empate!";
  }
}
