document.getElementById('img10').onclick = show;

function show() {
    alert('посмотри консоль')
    console.log('ну привет. ты наверное в поисках кодового слова, благодаря которому ты сможешь пройти на одну страничку.');
    setTimeout(show2, 2000);
};

function show2() {
    console.log('я тебе помогу, вот код:');
    setTimeout(show3, 2000);
};

function show3() {
    console.log('@3jrof##)F*4v94');
};
