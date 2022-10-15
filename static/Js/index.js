$(document).ready(function () {
    let button = $('#start-page-calc');
    let myForm = $('.calc-form');
    let calcButton = $('#calculate-button');
    let minusButton = $('#minus-button');
    let plusButton = $('#plus-button');
    let writeBookLength = $('#book-length-add');
    let cardSection = $('#card-adding-section');
    let prevIndex = -1;
    let doublePreIndex = -2;
    let type;
    let myList = [{
            'title': 'The Withcer: Baptism of Fire',
            'Author': 'Andrzej Sapkowski',
            'src': '../static/Images/Ateşle_İmtihan.jpg',
            'type': 'science-fiction'
        },
        {
            'title': 'Incognito',
            'Author': 'David Eaglemani',
            'src': '../static/Images/Kitab.png',
            'type': 'psychology'
        },
        {
            'title': 'Səfillər',
            'Author': 'Viktor Hüqo',
            'src': '../static/Images/Viktor.jpg',
            'type': 'novel'

        },
        {
            'title': 'The Withcer: Blood of Elves',
            'Author': 'Andrzej Sapkowski',
            'src': '../static/Images/Elflerin_Kanı_kapak.jpg',
            'type': 'science-fiction'
        },
        {
            'title': 'The Withcer: The Lady of the Lake',
            'Author': 'Andrzej Sapkowski',
            'src': '../static/Images/Gölün_Hanımı.jpg',
            'type': 'science-fiction'
        },
        {
            'title': 'The Withcer: The Tower of the Swallow',
            'Author': 'Andrzej Sapkowski',
            'src': '../static/Images/Kırlangıç_Kulesi.jpg',
            'type': 'science-fiction'
        },
        {
            'title': 'The Withcer: The Last Wish',
            'Author': 'Andrzej Sapkowski',
            'src': '../static/Images/Son_Dilek_kapak.jpg',
            'type': 'science-fiction'
        },
        {
            'title': 'Illuminae',
            'Author': 'Amie Kaufman and Jay Kristoff',
            'src': '../static/Images/Illuminae.jpg',
            'type': 'science-fiction'
        }
    ]
    // Calculate event section

    button.on('click', function (e) {
        if (button.hasClass('btn-warning')) {
            changeButtonClose();
            calculatePageSize();
        } else {
            changeButtonOpen();
            closeSucceedAlert();
            closeDangerAlert();
        }
    });

    // Calculate section funtion 

    function changeButtonClose() {
        button.removeClass('btn-warning');
        button.addClass('btn-danger');
        button.text('Bitir');
        showForm();
    }

    function changeButtonOpen() {
        button.removeClass('btn-danger');
        button.addClass('btn-warning');
        button.text('Başla');
        closeForm();
    }

    function showForm() {
        myForm.removeClass('d-none');
        myForm.addClass('d-flex');
    }

    function closeForm() {
        myForm.removeClass('d-flex');
        myForm.addClass('d-none');
    }

    function calculatePageSize() {
        calcButton.on('click', function (e) {
            let pageSize = $('#page-size').val();
            let daySize = $('#day-size').val();
            let resultSection = $('#day-section');
            if (daySize !== '0') {
                let result = Math.ceil(parseInt(pageSize) / parseInt(daySize));
                resultSection.text(result);
                closeDangerAlert();
                showSucceedAlert();

            } else {
                closeSucceedAlert();
                showDangerAlert();
            }
        });
    }

    function showSucceedAlert() {
        let showsection = $('#alert-section');
        showsection.removeClass('d-none');
        showsection.addClass('d-block');
    }

    function closeSucceedAlert() {
        let showsection = $('#alert-section');
        showsection.removeClass('d-block');
        showsection.addClass('d-none');
    }

    function showDangerAlert() {
        let section = $('#danger-alert-section');
        section.removeClass('d-none');
        section.addClass('d-block');
    }

    function closeDangerAlert() {
        let section = $('#danger-alert-section');
        section.removeClass('d-block');
        section.addClass('d-none');
    }



    // Filter type of book 

    // Show all book 
    $('#all-button').on('click', function (e) {
        [...cardSection.children()].forEach(element =>{
            element.className = '';
            element.classList.add('row')
        });
    });

    // Show psychology book 
    $('#crime_novel').on('click', function (e) {
        [...cardSection.children()].forEach(element =>{
            element.className = '';
            element.classList.add('row')
            if (element.dataset.type != 2){
                element.className = 'd-none';
            }
        });
    });


    $('#fiction').on('click', function (e) {
        [...cardSection.children()].forEach(element =>{
            element.className = '';
            element.classList.add('row')
            if (element.dataset.type != 3){
                element.className = 'd-none';
            }
        });
    });


    $('#fantasy').on('click', function (e) {
        [...cardSection.children()].forEach(element =>{
            element.className = '';
            element.classList.add('row')
            if (element.dataset.type != 1){
                element.className = 'd-none';
            }
        });
    });

    $('#Children').on('click', function (e) {
        [...cardSection.children()].forEach(element =>{
            element.className = '';
            element.classList.add('row')
            if (element.dataset.type != 4){
                element.className = 'd-none';
            }
        });
    });
});