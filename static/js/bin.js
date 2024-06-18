$(document).ready(function() {
    $('.increment').click(function() {
        var value = parseInt($(this).siblings('.numberInput').val(), 10);
        $(this).siblings('.numberInput').val(value + 1);
    });

    $('.decrement').click(function() {
        var value = parseInt($(this).siblings('.numberInput').val(), 10);
        if (value > 0) {  // Опционально: не уменьшать значение ниже 0
            $(this).siblings('.numberInput').val(value - 1);
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