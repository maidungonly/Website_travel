function signin(){
    window.location.href = '/signin';
}

const username = document.querySelector('input[name="tentaikhoan"]');
const passwd = document.querySelector('input[name="matkhau"]');

username.invalid = function(event) {
	event.target.setCustomValidity('Nhập tên tài khoản để đăng kí');
}
passwd.oninvalid = function(event) {
	event.target.setCustomValidity('Nhập mật khẩu cho tài khoản để đăng kí');
}