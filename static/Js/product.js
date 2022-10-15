let likeFontIcon = document.querySelector('#like-font-icon');
let heartFontIcon = document.querySelector('#heart-font-icon');
let shoppingFontIcon = document.querySelector('#navbarDropdown');
let bookName = document.querySelectorAll('.bookName');
let bookPrize = document.querySelectorAll('.bookPrize');
let sebet = document.querySelector('#Sebet');
let book = document.querySelector('.book-content-info');
let sumBookPrize = 0;
let spanPrizeSection = document.querySelector('#prize-span');
let bookCountdown = document.querySelector('#book-countdown');
let deleteButtonList = document.querySelectorAll('.fa-xmark');
let modalText = document.querySelector('#modal-text-section')



bookSizeBadge()
sumPrize(bookSize()[1]);
spanPrizeSection.innerText = sumBookPrize + ' AZN';

// like unlike
likeFontIcon.addEventListener('click', (event) => {
    if (likeFontIcon.style.transform === 'rotate(180deg)') {
        likeFontIcon.style.transform = 'rotate(0deg)';
        likeFontIcon.classList.replace('text-danger', 'text-primary')
    } else {
        likeFontIcon.style.transform = 'rotate(180deg)';
        likeFontIcon.classList.replace('text-primary', 'text-danger')
    }
});

//heart icon 
heartFontIcon.addEventListener('click', (event) => {
    if (heartFontIcon.classList.contains('text-secondary')) {
        heartFontIcon.classList.replace('text-secondary', 'text-danger')
        alert('Kitabı bəyəndiniz!');
    } else {
        heartFontIcon.classList.replace('text-danger', 'text-secondary')
        alert('Bəyənməkdən imtina etdiniz!', );
    }
});

// shopping icon

function addBasket(element){
    if(element.innerText === 'Səbətə əlavə et'){
        textChangeAdd(element);
    } else {
        textChangeDel(element);
    }
    sumPrize(bookSize()[1]);
    bookSizeBadge();
    deleteButton(deleteButtonList, element);
    spanPrizeSection.innerText = sumBookPrize + ' AZN';
};

function removeObj(){
    sebet.firstChild.remove();
    bookCountdown.innerText = parseInt(bookCountdown.innerText) + 1;
    bookCountdown.parentElement.classList.replace('alert-danger', 'alert-warning');
    deleteButtonList = document.querySelectorAll('.fa-xmark');
};

function addObj(){
    let newEle = document.createElement('li');
    newEle.innerHTML = `
    <p class="dropdown-item d-flex justify-content-between">
       <span>
            <span class="fa-solid fa-xmark deletedSpan text-danger"></span> 
            <span class="bookName" style="margin-right: 1rem">${book.children[0].innerText}</span> 
       </span>
        <span class="bookPrize">${parseInt(book.children[1].children[0].innerText)} AZN</span>
    </p>`
    sebet.prepend(newEle);
    bookCountdown.innerText = parseInt(bookCountdown.innerText) - 1;
    bookCountdown.parentElement.classList.replace('alert-warning', 'alert-danger');
    deleteButtonList = document.querySelectorAll('.fa-xmark');

};

function sumPrize(list){
    sumBookPrize = 0;
    if(list.length !== 0){
        list.forEach(element => {
            sumBookPrize += parseInt(element.innerText.split(' '));
        });
    } else{
        sumBookPrize = 0;
    }
};


function bookSize(){
    let innerBookName = document.querySelectorAll('.bookName');
    let innerBookPrize = document.querySelectorAll('.bookPrize');
    return [innerBookName, innerBookPrize];
}



function deleteButton(list, ele){
    list.forEach(button => {
        button.addEventListener('click', (event) => {
            event.target.parentElement.parentElement.remove();
            sumPrize(bookSize()[1]);
            spanPrizeSection.innerText = sumBookPrize + ' AZN';
            bookSizeBadge();
            if(event.target.classList[2] === 'deletedSpan'){
                ele.innerText = 'Səbətə əlavə et';
                ele.classList.replace('btn-secondary', 'btn-primary');
                modalText.innerText = 'Məhsul səbətdən çıxarıldı';
                removeObj();
            }
            
        })
    })
}

deleteButton(deleteButtonList);

function bookSizeBadge(){
    if(bookSize()[0].length !== 0){
        document.querySelector('#bookSizeSection').innerText = bookSize()[0].length;
    } else{
        document.querySelector('#bookSizeSection').innerText = '';
    }
    
}


function textChangeDel(ele){
    ele.innerText = 'Səbətə əlavə et';
    ele.classList.replace('btn-secondary', 'btn-primary');
    modalText.innerText = 'Məhsul səbətdən çıxarıldı';
    removeObj();
}

function textChangeAdd(ele){
    ele.innerText = 'Səbəttən çıxart';
    ele.classList.replace('btn-primary', 'btn-secondary');
    modalText.innerText = 'Məhsul səbətə əlavə edildi';
    addObj();
}


$(document).ready(function(){
    $('.center').slick({
        centerMode: true,
        centerPadding: '0',
        slidesToShow: 5,
        responsive: [
          {
            breakpoint: 768,
            settings: {
              arrows: false,
              centerMode: true,
              centerPadding: '0',
              slidesToShow: 3
            }
          },
          {
            breakpoint: 480,
            settings: {
              arrows: false,
              centerMode: true,
              centerPadding: '0',
              slidesToShow: 1
            }
          }
        ]
      });
          
  });