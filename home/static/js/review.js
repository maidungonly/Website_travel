var slides=document.querySelector('.diadanh_slides');
var slide=Array.from(document.querySelectorAll('.diadanh_slide'));
var slidegr=document.querySelector('.diadanh_slide-gr');
var button=document.querySelector('.left')
var num_page

function makeslide(numberonetime) {
    
    var percentwidth_slide=100/numberonetime;
    // tính độ dài của từng slide
    num_page=Math.ceil(slide.length/numberonetime);
    // tính số lượng trang
    slide.forEach((el,index)=>{
        el.style.width=(slidegr.offsetWidth/100*percentwidth_slide)+'px';
        // set độ rộng của từng slide
    })   
    slides.style.width=(slidegr.offsetWidth/100*percentwidth_slide)*slide.length+'px';
}
makeslide(5);

var curpage = 1;
function showslide(pagenumber){
    slides.style.marginLeft=-(slidegr.offsetWidth*(pagenumber-1))+'px';
}
showslide(1);

function changeslide(n){
    curpage=curpage+n;
    if(curpage<1) curpage=num_page;
    if(curpage>num_page) curpage=1;
    showslide(curpage);
}
