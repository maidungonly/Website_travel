function closeModal() {
    let modal = document.getElementById('myModal');
    modal.style.display = 'none';
}

let nVouchers = 3;
let msg = `<b>Hoac chon mot ma giam gia duoi day</b> (${nVouchers})`;
let vouchers = document.getElementById('vouchers');
vouchers.innerHTML = msg;
let modal = document.getElementById('myModal');
let btn = document.getElementById('voucher-btn');
let span = document.getElementsByClassName('close')[0];

btn.onclick = function () {
    modal.style.display = 'block';
    span.onclick = function () {
        modal.style.display = 'none';
    }

    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
}
function reCalculate() {
    let priceStr = document.getElementById('price').innerText;
    priceStr = priceStr.toString().replace(',', '');
    priceStr = priceStr.replace(' VND', '');
    let price = Number(priceStr);

    let numbers = Number(document.getElementById('num').value);
    let numPrice = price * numbers;
    let vat = Math.floor(0.1 * numPrice);
    let total = numPrice + vat;

    document.getElementById('price').innerHTML = price.toLocaleString() + ' VND';
    document.getElementById('num-price').innerHTML = numPrice.toLocaleString() + ' VND';
    document.getElementById('vat').innerHTML = vat.toLocaleString() + ' VND';
    document.getElementById('sum').innerHTML = total.toLocaleString() + ' VND';
}

let price = 675873;
document.getElementById('price').innerHTML = price.toLocaleString() + ' VND';