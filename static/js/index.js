$(document).ready(function() {
    const $thumbnails = $('.thumbnail');
    const $largeImage = $('#largeImage');
    const $elements = $('.setting-right-color');
    const $colorTicks = $('.color-tick');
    const $buttons = $('button');
    
    $thumbnails.on('click', function() {
        $thumbnails.css('filter', 'brightness(50%)');
        $(this).css('filter', 'brightness(100%)');
    });
    
    $elements.on('click', function() {
        $elements.removeClass('with-border');
        $(this).addClass('with-border');
    });
    
    $colorTicks.on('click', function() {
        $(this).css('display', 'flex');
    });
    
    $buttons.on('click', function() {
        
    });

});
