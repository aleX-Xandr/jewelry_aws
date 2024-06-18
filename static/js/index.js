$(document).ready(function() {
    const $thumbnails = $('.thumbnail');
    const $largeImage = $('#largeImage');
    const $elements = $('.setting-right-color');
    const $colorTicks = $('.color-tick');
    const $buttons = $('button');
    const $jewerlyCard = $('.jewerly-card');
    let currentIndex = 0;
    const $slides = $('.slides');
    const $slide = $('.slide');
    const totalSlides = $slide.length;

    // Slider previous button
    $('.prev').on('click', function() {
        currentIndex = (currentIndex === 0) ? totalSlides - 1 : currentIndex - 1;
        updateSlider();
    });

    // Slider next button
    $('.next').on('click', function() {
        currentIndex = (currentIndex === totalSlides - 1) ? 0 : currentIndex + 1;
        updateSlider();
    });

    function updateSlider() {
        $slides.css('transform', `translateX(-${currentIndex * 100}%)`);
    }

    // Thumbnail click event
    $thumbnails.on('click', function() {
        $thumbnails.css('filter', 'brightness(50%)');
        $(this).css('filter', 'brightness(100%)');
    });

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

    // Pagination click event
    $('.pagination').on('click', function() {
        $('.pagination').removeClass('activePagination');
        $(this).addClass('activePagination');
    });

    // Increment and decrement input value
    $('#increment').on('click', function() {
        var value = parseInt($('#numberInput').val(), 10);
        $('#numberInput').val(value + 1);
    });

    $('#decrement').on('click', function() {
        var value = parseInt($('#numberInput').val(), 10);
        if (value > 0) { 
            $('#numberInput').val(value - 1);
        }
    });

    // Breadcrumb click event
    $('.breadcrumb').on('click', function() {
        $('.breadcrumb').removeClass('active');
        $(this).addClass('active');
    });

    // Additional slider controls
    $('.prevo').on('click', function() {
        currentIndex = (currentIndex === 0) ? totalSlides - 1 : currentIndex - 1;
        updateSlider50();
    });

    $('.nexto').on('click', function() {
        currentIndex = (currentIndex === totalSlides - 1) ? 0 : currentIndex + 1;
        updateSlider50();
    });

    function updateSlider50() {
        $slides.css('transform', `translateX(-${currentIndex * 50}%)`);
    }
});
