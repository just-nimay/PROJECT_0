var ticks = 120;
var i = false;
function letsGo() {

  if(i == false){
      if(ticks<0) {
           scrmr()
      }

      document.getElementById("tick").innerHTML=ticks;

      ticks--;
      setTimeout(letsGo,1000);

        document.getElementsByClassName('class-inputa')[0].onkeypress = function(e) {
                   let a = document.querySelector('.class-inputa').value; 
                    if(e.key=='Enter') {
                        if(a == 'пароль') {
                            alert('вы угадали!')
                            i = true;
                            document.getElementById('tick').innerHTML='';
                            document.getElementById('wrapper').innerHTML='';
                            document.getElementById('text1').innerHTML='знаешь чего ты избежал?';
    
                            setTimeout(next, 3000);
                            
                            
                            

                        } else {
                            alert('неверно!')
                            ticks = ticks-2;
                        }
                    }

                }
    }
}

function next(){
    document.getElementById('text1').innerHTML='я тебе сейчас расскажу)))<br> и даже покажу';
    setTimeout(scrmr, 5000);
    
}

function scrmr() {
    document.getElementById('text1').innerHTML='';
    
    document.getElementById("scrimer").innerHTML="<img src='img/scrimer_3.jpg'>"; 
    play();
    setTimeout(next2, 1000);
   
    return;
    
    
    
}

function play() {
  var audio = new Audio('music/sound_3.mp3');
  audio.play();
}

function next2() {
    window.close()
}
 