document.addEventListener('DOMContentLoaded', () => {
    const botao_adicionar = document.querySelector('#adicionar');
    let dropdown_lista = document.querySelector('#lista');

    if (dropdown_lista.options.length == 0) {
        botao_adicionar.disabled = true
    }
    else {
        botao_adicionar.disabled = false
    }
})