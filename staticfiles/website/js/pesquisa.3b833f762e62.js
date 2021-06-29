document.addEventListener('DOMContentLoaded', function() {
    // document.querySelector('form').onsubmit = function() {
    //
    //     fetch('https://api.adviceslip.com/advice')
    //     .then(response => response.json())
    //     .then(data => {
    //         const conselho = data.slip.advice;
    //         document.querySelector('#resultado').innerHTML = `1 EUR = ${conselho}`;
    //     })
    //     return false;
    // }

    // document.querySelector('form').onsubmit = function() {
    //     const artist = "U2";
    //     const song = "One";
    //     fetch("https://api.vagalume.com.br/search.php"
    //             + "?art=" + artist
    //             + "&mus=" + song,
    //             + "&apikey=1fe2fd2afc5df897f528244b3fbf41c1"
    //     .then(response => response.json())
    //     .then(data => {
    //             // Letra da música
    //             alert(data.mus[0].text);
    //         })
    //     )
    // };

document.querySelector('form').onsubmit = function() {
    const artista = document.querySelector('#artista').value.toUpperCase();
    const musica = document.querySelector('#musica').value.toUpperCase();
    fetch('https://api.vagalume.com.br/search.php'
            + '?art=' + artista
            + '&mus=' + musica
            + '&apikey=1fe2fd2afc5df897f528244b3fbf41c1')
    .then(response => response.json())
    .then(data => {
        // document.querySelector('#letra-musica').innerHTML = data.art.name;
        // document.querySelector('#resultado').innerHTML += data.mus[0].name;
        console.log(data.mus[0].text);
        alert(data.mus[0].text);
        document.querySelector('#letra-musica').innerHTML = data.mus[0].text;
    })
    return false;
}

});