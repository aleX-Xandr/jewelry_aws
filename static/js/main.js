$(document).ready(function() {

const $thumbnails = $('.thumbnail'); 
const $elements = $('.setting-right-color');
const $buttons = $('button');
const btnBasket = $('#btnBasket');
const overlay = $('#overlay');
const btnCloseSidebar = $('#btnCloseSidebar');
const increment = $('.increment');
const decrement = $('.decrement');


// Setting-right-color click event
$elements.on('click', function() {
    $elements.removeClass('with-border');
    $(this).addClass('with-border');
    $elements.removeClass('checked');
    $(this).addClass('checked'); 
});

// Button click event
$buttons.on('click', function() {
    console.log('button clicked');
});

$thumbnails.on('click', function() {
    console.log("123");
    var src = $(this).attr('data-large-src');
    console.log(src);
    $('#largeImage').attr('src', src);
});

// Pagination click event
$('.pagination').on('click', function() {
    $('.pagination').removeClass('activePagination');
    $(this).addClass('activePagination');
});

// Increment and decrement input value
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

// Breadcrumb click event
$('.breadcrumb').on('click', function() {
    $('.breadcrumb').removeClass('active');
    $(this).addClass('active');
});

 // Add checkmark div to each clickable object

    
 // Toggle checkmark visibility on click
 // $('.clickable-object').on('click', function() {
 //     $(this).find('.checkmark').toggle();
 // });

 // // Hide checkmark on click
 // $('.checkmark').on('click', function(event) {
 //     event.stopPropagation(); // Prevent triggering the parent click event
 //     $(this).hide();
 // });

 $('.buy-now.pc').on('click', function(event) {
     event.preventDefault(); // Prevent triggering the parent click event
     $('#constructor_form').submit();
 });

});   