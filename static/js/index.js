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
    const constructorItems = $('#constructorItems');
    const binCard = $('.bin-card');
    const priceTotal = $('.priceTotal');
    const selectedItemsInput = $('#selectedItems');
    

    const toggleSidebar = () => {
        sidebarPanel.hasClass('show') ? sidebarPanel.removeClass('show') : sidebarPanel.addClass('show');
        overlay.hasClass('show') ? overlay.removeClass('show') : overlay.addClass('show');
    };

    announcesSlider.slick({
        infinite: true,
        slidesToShow: 1,
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
        slidesToShow: 1,
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

    let priceTotalVal = parseFloat(priceTotal.text());
    let selectedItems = [];
    binCard.each(function () {
        let card = $(this);
        let checkmark = card.find('.checkmark');
        let binImg = card.find('.bin-img-img');
        let price = parseFloat(card.data('price'));
        let itemId = card.data('id');
        let fullImgSrc = card.data('img');

        card.on('click', (e) => {
            checkmark.toggle();
            if (checkmark.is(':visible')) {
                let constructorItem = $('<div class="constructor-item" data-id="' + itemId + '">' +
                    '<img src="' + fullImgSrc + '" alt=""></div>');
                constructorItems.append(constructorItem);
                priceTotalVal += price;
                selectedItems.push(itemId);
            } else {
                constructorItems.find('.constructor-item[data-id="' + itemId + '"]').remove();
                priceTotalVal -= price;
                for (let i= 0; i < selectedItems.length; i++) {
                    if (selectedItems[i] === itemId) {
                        delete selectedItems[i];
                    }
                }
            }
            priceTotal.text(priceTotalVal.toFixed(2));
            selectedItems = selectedItems.filter(element => element !== null);
            selectedItemsInput.val(selectedItems.join(','));
            console.log(selectedItemsInput.val());
        });
    });
});   
