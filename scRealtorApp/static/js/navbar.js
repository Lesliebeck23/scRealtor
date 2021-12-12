window.onload = function(){

    (function($){
        $('.mobile_bar').click(function(e){
            e.preventDefault();
            $('.navbar').toggleClass('active');
        })
    })(jQuery);

}


