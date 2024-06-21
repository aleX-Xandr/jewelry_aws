$(document).ready(function() {
    const $largeImage = $('#largeImage');
    const $colorTicks = $('.color-tick');
    const $jewerlyCard = $('.jewerly-card');
    const $slides = $('.slides');
    const $slide = $('.slide');
    const totalSlides = $slide.length;
    const announcesSlider = $('#announcesSlider');
    const announcesSliderPrev = $('#announcesSliderPrev');
    const announcesSliderNext = $('#announcesSliderNext');
    const announcesSliderPagination = $('#announcesSliderPagination');
    const additionalSlider = $('#additionalSlider');
    const sliderPresentosa = $('#sliderPresentosa');
    const sliderPresentosaPrev = $('#sliderPresentosaPrev');
    const sliderPresentosaNext = $('#sliderPresentosaNext');
    const sliderPresentosaPagination = $('#sliderPresentosaPagination');
    const sidebarPanel = $('#sidebarPanel');
    const btnBasket = $('#btnBasket');
    const overlay = $('#overlay');
    const btnCloseSidebar = $('#btnCloseSidebar');
    const increment = $('.increment');
    const decrement = $('.decrement');
    

    const toggleSidebar = () => {
        sidebarPanel.hasClass('show') ? sidebarPanel.removeClass('show') : sidebarPanel.addClass('show');
        overlay.hasClass('show') ? overlay.removeClass('show') : overlay.addClass('show');
    };

    announcesSlider.slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        dots: true,
        dotsClass: 'breadcrumbs slider-soon',
        appendDots: announcesSliderPagination,
        prevArrow: announcesSliderPrev,
        nextArrow: announcesSliderNext,
        centerMode: true,
        variableWidth: true,
        responsive: [
            {
                breakpoint: 660,
                settings: {
                    slidesToShow: 1
                }
            }
        ]
    });

    additionalSlider.slick({
        infinite: true,
        slidesToShow: 4,
        slidesToScroll: 1,
        dots: false,
        arrows: false,
        centerMode: true,
        variableWidth: true,
    });

    sliderPresentosa.slick({
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        dots: true,
        dotsClass: 'breadcrumbs',
        appendDots: sliderPresentosaPagination,
        prevArrow: sliderPresentosaPrev,
        nextArrow: sliderPresentosaNext,
        speed: 500,
        fade: true,
        cssEase: 'linear'
    });

    btnBasket.on('click', () => { toggleSidebar(); });
    btnCloseSidebar.on('click', () => { toggleSidebar(); });
    overlay.on('click', () => { toggleSidebar(); });

    increment.each(function () {
        let inc = $(this);
        inc.on('click', () => {
            let value = parseInt(inc.siblings('.numberInput').val(), 10);
            inc.siblings('.numberInput').val(value + 1);
        });
    });

    decrement.each(function () {
        let dec = $(this);
        dec.on('click', () => {
            let value = parseInt(dec.siblings('.numberInput').val(), 10);
            if (value > 0) {
                dec.siblings('.numberInput').val(value - 1);
            }
        });
    });
       
});   
