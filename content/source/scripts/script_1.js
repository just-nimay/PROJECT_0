document.querySelector('button').onclick = myClick;

function myClick() {
    let a = document.querySelector('.search').value;
    var i = null
    
    if (a == 'как приготовить человека') {
        window.open('page_1.html');
        
        return
            
      } else if (a == 'я слежу за тобой') {
        window.open('page_2.html');
          
          
    }else if (a == 'не открывать меня!' ) {
        check();
        
        
    }else if (a == 'котики'){
        window.open('page_4.html')
    }else{
        alert('введенный запрос неверный!')
       
    }   
};

function check() {
    document.getElementById('check').style='animation: ch_on 0.5s forwards;'
};

function checking() {
    var input = document.getElementById('inp_check').value;;
    document.getElementById('inp_check').value='';
    if(input == 'FUCKYOU') {
        window.open('page_3.html');
        document.getElementById('check').style='animation: ch_off 0.2s forwards;';
    } else if(input == '@3jrof##)F*4v94') {
        alert('Зря ты его послушал...');
        setTimeout(fake_page, 1000);
    } else {
        alert('Нет доступа');
        document.getElementById('check').style='animation: ch_off 0.2s forwards;';
        
    };
    
};
function fake_page() {
    window.open('page_5.html');
};

document.getElementById('close').onclick= clear;
function clear() {
    
    document.getElementById('inp').value='';
};