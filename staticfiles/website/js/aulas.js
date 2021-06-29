window.onpopstate = function(event) {
    showSection(event.state.seccao);
}

function showSection(seccao) {

    fetch(`/aulas_seccao/${seccao}`)
    .then(response => response.json())
    .then(dados => {
        // dados.forEach(obj => {
        //     Object.entries(obj).forEach(([key, value]) => {
        //         console.log(`${key} ${value}`);
        //     });
        //     console.log('-------------------');
        // });
            Object.entries(JSON.stringify(dados.toString())).forEach(([key, value]) => {
            console.log(`${key} ${value}`);
        });
    });
    //     console.log(dados);
    //     const campos = dados["conteudo"][0]["fields"];
    //     Object.entries(campos).forEach((entry) => {
    //         const [key, value] = entry;
    //         console.log(`${key}: ${value}`);
    //     });
    //     // document.querySelector('#conteudo').appendChild(criaLista(seccao, campos));
    // });
};


function criaLista(seccao, campos) {
    const ol = document.createElement('ol');

    for (let i = 0; i < campos.length; i++) {
        console.log(campos[i])
        const li = document.createElement('li');
        if (seccao == 1) {
            console.log('seccao 1')
            li.appendChild(document.createTextNode('Aula de ' + campos["titulo"] + ' | Duração: ' + campos["duracao"]));
            ol.appendChild(li);
        }
        else if (seccao == 2) {
            console.log(campos[i])
            const date = new Date(campos["criado"]);
            const criacao = date.getDate() + '/' + (date.getMonth()+1) + '/' + date.getFullYear();
            li.appendChild(document.createTextNode('(' + criacao + ') ' + campos["nome"] + ' ' + campos["apelido"]));
            ol.appendChild(li);
        }

        return ol;
    }
};

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('button').forEach(button => {
        button.onclick = function() {
            const seccao = this.dataset.seccao;
            history.pushState({seccao: seccao}, "", `aulas_section_view${seccao}`);
            showSection(seccao);
        };
    });
});