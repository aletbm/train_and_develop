(function(){
    $(document).ready(function(){
        var n_courses = $('.category-visible .courses-cards .courses-slider .courses-card').length
            document.documentElement.style.setProperty('--n_courses', n_courses/2);
        $(".carrousel-button-cat").click(function () {
            var category = $(this).attr("data-filter");
            $('.courses-category').removeClass("category-visible")
            $('.courses-category[data-category='+category+']').addClass("category-visible")
            $('.carrousel-button-cat').removeClass("btn-active")
            $(this).addClass("btn-active")
            var n_courses = $('.category-visible .courses-cards .courses-slider .courses-card').length
            document.documentElement.style.setProperty('--n_courses', n_courses/2);
        });
    });
}())