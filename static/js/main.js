$(document).ready(function() {

    const $thumbnails = $('.thumbnail'); 
    const $elements = $('.setting-right-color');
    const $buttons = $('button');
    const btnBasket = $('#btnBasket');
    const overlay = $('#overlay');
    const btnCloseSidebar = $('#btnCloseSidebar');
    const increment = $('.increment');
    const decrement = $('.decrement');

    const saveScrollPosition = () => {
        sessionStorage.setItem('scrollPosition', window.scrollY);
    }
    const loadScrollPosition = () => {
        if (sessionStorage.getItem('scrollPosition') !== null) {
            window.scrollTo(0, sessionStorage.getItem('scrollPosition'));
        }
    }
    
    loadScrollPosition()

    $elements.on('click', function() {
        $elements.removeClass('with-border');
        $(this).addClass('with-border');
        $elements.removeClass('checked');
        $(this).addClass('checked'); 
    });

    $buttons.on('click', function() {
        console.log('button clicked');
    });

    $thumbnails.on('click', function() {
        console.log("123");
        var src = $(this).attr('data-large-src');
        console.log(src);
        $('#largeImage').attr('src', src);
    });

    $('.pagination').on('click', function() {
        $('.pagination').removeClass('activePagination');
        $(this).addClass('activePagination');
    });

    $('.incrementProduct').on('click', function() {
        var value = parseInt($('#numberInput').val(), 10);
        $('#numberInput').val(value + 1);
        event.preventDefault();
    });

    $('.setting-amound').on('click', function(){
        $('.setting-amound').css('border:none;');
    });

    $('.decrementProduct').on('click', function() {
        var value = parseInt($('#numberInput').val(), 10);
        if (value > 0) {
            $('#numberInput').val(value - 1);
        }
        event.preventDefault();
    });

    $('.breadcrumb').on('click', function() {
        $('.breadcrumb').removeClass('active');
        $(this).addClass('active');
    });

    $('#checkoutButton').on('click', function() {
        var form = $('#checkoutForm');
        var reportValidity = form[0].reportValidity();
        if(reportValidity){
            form.submit();
        }
    });

    $('.checkout').on('click', function() {
        let form = $('#checkoutForm');
        let reportValidity = form[0].reportValidity();
        if(reportValidity){
            form.submit();
        }
    });

    $('input[name="delivery"]').on('click', function(event) {
        let form = $('#checkoutForm');
        let reportValidity = form[0].reportValidity();
        console.log(reportValidity);
        if(reportValidity){
            saveScrollPosition()
            form.submit();
        }else{
            event.preventDefault();
        }
    });

});   