$(document).ready(function() {
    $('.increment').click(function() {
        var value = parseInt($(this).siblings('.numberInput').val(), 10);

        var redirect = $(this).closest('.bin-card').attr('on-edit');
        var productId = $(this).closest('.bin-card').attr('data-product');
        var price = $(this).closest('.bin-card').attr('data-price');

        var url = redirect + "?product_id=" + productId + "&quantity=" + (value + 1) + "&ajax=true";

        $.ajax({
            url: url,
            dataType: 'json',
            success: function(result){
                console.log(result);
                $('.payment-price').each(function (index, element) {
                    $(this).find('a').text('€' + result.order_price.toFixed(1));
                });
          }});

         $(this).siblings('.numberInput').val(value + 1);
         $(this).closest('.bin-card').find('.bin-price').text('€' + ((value + 1) * price).toFixed(1));
    });

    $('.decrement').click(function() {
        var value = parseInt($(this).siblings('.numberInput').val(), 10);

        var redirect = $(this).closest('.bin-card').attr('on-edit');
        var productId = $(this).closest('.bin-card').attr('data-product');
        var price = $(this).closest('.bin-card').attr('data-price');

         var url = redirect + "?product_id=" + productId + "&quantity=" + (value - 1) + "&ajax=true";

        $.ajax({
            url: url,
            dataType: 'json',
            success: function(result){
                console.log(result);
                $('.payment-price').each(function (index, element) {
                    $(this).find('a').text('€' + result.order_price.toFixed(1));
                });
          }});

        if (value > 1) {
            $(this).siblings('.numberInput').val(value - 1);
            $(this).closest('.bin-card').find('.bin-price').text('€' + ((value - 1) * price).toFixed(1));
        } else {
            $(".bin-card").each(function( index ) {
              var prodId = $(this).attr('product-id');

              if (productId == prodId) {
                $(this).remove();
              }
            });
            $(this).closest('.bin-card').remove();
        }
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