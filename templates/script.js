// Obter todos os botões de aumento e diminuição
const btnAumentar = document.querySelectorAll('.btn-aumentar');
const btnDiminuir = document.querySelectorAll('.btn-diminuir');

// Adicionar um evento de clique a cada botão de aumento e diminuição
btnAumentar.forEach(btn => {
  btn.addEventListener('click', () => {
    const jogadorId = btn.getAttribute('data-jogador-id');
    const totalVitoriasInput = document.querySelector(`.total-vitorias[data-jogador-id="${jogadorId}"]`);
    const totalVitorias = parseInt(totalVitoriasInput.value);
    totalVitoriasInput.value = totalVitorias + 1;
    atualizarTotalVitorias(jogadorId, totalVitorias + 1);
  });
});

btnDiminuir.forEach(btn => {
  btn.addEventListener('click', () => {
    const jogadorId = btn.getAttribute('data-jogador-id');
    const totalVitoriasInput = document.querySelector(`.total-vitorias[data-jogador-id="${jogadorId}"]`);
    const totalVitorias = parseInt(totalVitoriasInput.value);
    if (totalVitorias > 0) {
      totalVitoriasInput.value = totalVitorias

<script>
function adicionarVitoria(jogadorId) {
    // Encontra o campo "Total Vitórias" correspondente ao jogadorId
    var vitoriasCampo = $('#vitorias_' + jogadorId);

    // Obtém o valor atual do campo "Total Vitórias"
    var vitorias = parseInt(vitoriasCampo.text());

    // Adiciona uma vitória
    vitorias++;

    // Atualiza o valor do campo "Total Vitórias"
    vitoriasCampo.text(vitorias);
}

function removerVitoria(jogadorId) {
    // Encontra o campo "Total Vitórias" correspondente ao jogadorId
    var vitoriasCampo = $('#vitorias_' + jogadorId);

    // Obtém o valor atual do campo "Total Vitórias"
    var vitorias = parseInt(vitoriasCampo.text());

    // Remove uma vitória (se a contagem já for zero, não faz nada)
    if (vitorias > 0) {
        vitorias--;
    }

    // Atualiza o valor do campo "Total Vitórias"
    vitoriasCampo.text(vitorias);
}
</script>
