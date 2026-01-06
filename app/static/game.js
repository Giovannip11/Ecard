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
