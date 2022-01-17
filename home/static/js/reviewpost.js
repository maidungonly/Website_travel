
/*Danhgia===========================================================================*/
const danhgia = document.querySelector('.danhgia');
var starthu;

for (var i = 1; i <= 5; i++)
{
    const star = document.querySelector('i[id="saodanhgia"]');
    star.onclick = function(){
        starthu = star.getAttribute("name");
    }
}
danhgia.addEventListener('click', showdanhgia)

function showdanhgia(){
    for(var y = 1; y <= starthu; y++){
    }
}

/*reaction==========================================================================*/
const btnreact = document.querySelector('.reaction > button');
const hearticon = document.querySelector('button[name="reaction"] > i')
const buttonchatbox = document.querySelector('button[class="nut-mo-chatbox"')

btnreact.onclick = function (){
    if (hearticon.getAttribute("class") != 'fas fa-heart'){ 
        hearticon.setAttribute('class','fas fa-heart');
        btnreact.style.color = '#EC1522';
    }
    else{
        confirmbox();
        hearticon.setAttribute('class','far fa-heart');
        btnreact.style.color = '#EC1522'; 
    }
}

function confirmbox(){
    if(confirm("Bạn có chắc chắn muốn huỷ yêu thích bài viết này?") == true){
        hearticon.setAttribute('class','far fa-heart');
        btnreact.style.color = '#EC1522'; 
    }else{
    }
}


/*Chatbox=========================================================================*/
var listtuvanvien = ['Nguyễn Thị Cẩm Tiên', 'Mai Trọng Dũng', 'Nguyễn Sỹ Trường','Đỗ Minh Tú','Dương Thị Ngân Giang'];
const tuvanvien = document.querySelector('.tuvanvien');


function randomValueFromArray(array) {
    const random = Math.floor(Math.random() * array.length);
    return array[random];
}

function moForm() {
    document.getElementById("myForm").style.display = "block";
    buttonchatbox.style.visibility = 'hidden';
    tuvanvien.textContent = randomValueFromArray(listtuvanvien);
  }

  function dongForm() {
    document.getElementById("myForm").style.display = "none";
    buttonchatbox.style.visibility = 'visible';
  }

const msg = document.querySelector('textarea[name="msg"]');

msg.oninvalid = function(event) {
	event.target.setCustomValidity('Nhập lời nhắn trước khi bắt đầu chat để tư vấn viên có thể hỗ trợ bạn nhanh hơn');
}
