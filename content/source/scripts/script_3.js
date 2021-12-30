function start() {
    document.getElementById('to_del').innerHTML=''
    document.body.style.backgroundImage= 'url("scripts/glitch.gif")'
    var audio = new Audio('music/sound_0.mp3');
    audio.play();
    setTimeout(next, 1000)
}



function next() {
    document.body.style.backgroundImage= 'url("scripts/Human.gif") '
    document.getElementById('text').style= 'animation: txt 5s infinite;'
    audio = new Audio('music/space_0.mp3');
    audio.play();
    setTimeout(next2, 5000)
    
}

function next2() {
    document.getElementById('text').innerHTML='ты же понимаешь'
    setTimeout(next3, 5000)
}

function next3() {
    document.getElementById('text').innerHTML='что это всё '
    setTimeout(next4, 5000)
}

function next4() {
    document.getElementById('text').innerHTML='не вечно'
    setTimeout(next5, 5000)
}

function next5() {
    document.getElementById('text').innerHTML='вечно'
    setTimeout(next6, 10000)
}

function next6() {
    document.body.style.backgroundImage= 'url("scripts/4KGS.gif") '
    document.getElementById('text').innerHTML='Поздравляю, ты прошел <br> мою первую игру!'
    
    setTimeout(end, 10000)
    
}
function end() {
    var audio = new Audio('music/space_1.mp3');
    audio.play();
    document.getElementById('text').style= 'animation: txt 5s infinite;'
    document.getElementById('text').innerHTML='О, ты еще тут? ну тогда ты можешь оставить такой отзыв в приложении for_friends: ужасно хорошо'
}

