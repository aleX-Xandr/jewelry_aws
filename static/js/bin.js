$(document).ready(function() {
    $('.increment').click(function() {
        var value = parseInt($(this).siblings('.numberInput').val(), 10);

        var redirect = $(this).closest('.bin-card').attr('on-edit');
        var productId = $(this).closest('.bin-card').attr('data-product');
        window.location.replace(redirect + "?product_id=" + productId + "&quantity=" + (value + 1));

//        $(this).siblings('.numberInput').val(value + 1);
    });

    $('.decrement').click(function() {
        var value = parseInt($(this).siblings('.numberInput').val(), 10);

        var redirect = $(this).closest('.bin-card').attr('on-edit');
        var productId = $(this).closest('.bin-card').attr('data-product');
        window.location.replace(redirect + "?product_id=" + productId + "&quantity=" + (value - 1));

//        if (value > 1) {
//            $(this).siblings('.numberInput').val(value - 1);
//        } else {
//            $(".bin-card").each(function( index ) {
//              var prodId = $(this).attr('product-id');
//
//              if (productId == prodId) {
//                $(this).remove();
//              }
//            });
//            $(this).closest('.bin-card').remove();
//        }
    });
    $(document).ready(function() {
        $('.basket-img').click(function() {
            $('.bin-mobile').addClass('show');
            $('.overlay').addClass('show');
        });

        $('.arrow-left-direction').click(function() {
            $('.bin-mobile').removeClass('show');
            $('.overlay').removeClass('show');
        });

        $('.overlay').click(function() {
            $('.bin-mobile').removeClass('show');
            $(this).removeClass('show');
        });
    });
});