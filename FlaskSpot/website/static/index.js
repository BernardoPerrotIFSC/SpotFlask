function removeHistorico(historicoId) {
    fetch("/remove-Historico", {
        method: 'POST',
        body: JSON.stringify({historicoId: historicoId}),
    }).then(() => {
        window.location.href="/view"
    });
}