(function () {
    $(document).ready(function () {
        var filter_h = $('.filters').height() + 60 + 150
        $('.filters').css("max-height", "100px")
        $('input[type=checkbox]').change(function () {
            var checkboxs = $('input[type=checkbox]')
            var filters = []
            var type_filter = []
            var large_pag = 10
            var nav_buttons = ""
            var categories = ""
            var authors = ""
            for (var n = 0; n < checkboxs.length; n++) {
                var checkbox = $('input[type=checkbox]:eq(' + n + ')')
                if (checkbox.prop("checked")) {
                    filters.push(checkbox.prop("id"))
                    type_filter.push(checkbox.parent().parent().prop("id"))
                }
            }
            for (var n = 0; n < filters.length; n++) {
                if (type_filter[n] == "category") {
                    categories = categories + filters[n]
                }

                if (type_filter[n] == "author") {
                    authors = authors + filters[n]
                }
            }

            categories = categories.replace(/ /g, "").replace(", ", "").replace(',', "")
            authors = authors.replace(/ /g, "").replace(", ", "").replace(',', "")
            $('.mode-results').removeClass("course-visible")
            $('.mode-results').addClass("course-novisible")
            if (filters.length > 0) {
                if (authors == "" && $('.mode-results[data-category*=' + categories + ']')) {
                    $('.mode-results[data-category*=' + categories + ']').removeClass("course-novisible")
                    $('.mode-results[data-category*=' + categories + ']').addClass("course-visible")
                }
                else if (categories == "" && $('.mode-results[data-author*=' + authors + ']').length) {
                    $('.mode-results[data-author*=' + authors + ']').removeClass("course-novisible")
                    $('.mode-results[data-author*=' + authors + ']').addClass("course-visible")
                }
                else if (authors != "" && categories != "" && $('.mode-results[data-author *=' + authors + '][data-category*=' + categories + ']')) {
                    $('.mode-results[data-author*=' + authors + '][data-category*=' + categories + ']').removeClass("course-novisible")
                    $('.mode-results[data-author*=' + authors + '][data-category*=' + categories + ']').addClass("course-visible")
                }
            }

            if (filters.length == 0) {
                var cant_cursos = $('.mode-results').length
                var ratio = cant_cursos / large_pag
                cant_pages = Math.ceil(ratio)
                for (var x = 1; x <= cant_pages; x++) {
                    if (x == 1) {
                        nav_buttons = '<button class="btn-page btn-page-active" data-btn="1">1</button>'
                    }
                    else {
                        nav_buttons += '<button class="btn-page" data-btn="' + x + '">' + x + '</button>'
                    }
                }
                $('button').remove('.btn-page')
                $('button').remove('.btn-page-filter')
                $('.courses-nav-page').append(nav_buttons)
                nav(1, $(".btn-page-active"), filter=false)
            }
            else {
                var cant_cursos = $(".course-visible").length
                var ratio = cant_cursos / large_pag
                var cant_pages = Math.ceil(ratio)
                for (var x = 1; x <= cant_pages; x++) {
                    if (x == 1) {
                        nav_buttons = '<button class="btn-page-filter btn-page-active" data-btn="1">1</button>'
                    }
                    else {
                        nav_buttons += '<button class="btn-page-filter" data-btn="' + x + '">' + x + '</button>'
                    }
                }
                $('button').remove('.btn-page')
                $('button').remove('.btn-page-filter')
                $('.courses-nav-page').append(nav_buttons)
                nav(1, $(".btn-page-active"), filter=true)
            }

        });

        $('body').on('click', '.btn-page', function () { nav(0, $(this), false) })
        $('body').on('click', '.btn-page-filter', function () { nav(0, $(this), true) })
        $('body').on('click', '#slider',{"h":filter_h}, function (event){
            if($('.slider-img').attr("style") != "transform: rotate(180deg);"){
                $('.filters').css({"max-height": event.data.h})
                $('.slider-img').css("transform", "rotate(180deg)")
            }
            else{
                $('.filters').css({"max-height": "100px"})
                $('.slider-img').css("transform", "rotate(0deg)")
            }
        })
    });

    function nav(indice_def = 0, this_, filter = false) {
        var large_pag = 10
        var indice_page = indice_def
        if (indice_def == 0) {
            var indice_page = this_.prop("innerText")
        }
        if (filter == false) {
            var n_course_max = indice_page * large_pag
            var n_course_min = n_course_max - large_pag + 1
            $('.mode-results').addClass("course-novisible")
            $('.mode-results').removeClass("course-visible")
            for (var i = n_course_min; i <= n_course_max; i++) {
                $('.mode-results[data-course=' + i + ']').addClass("course-visible")
                $('.mode-results[data-course=' + i + ']').removeClass("course-novisible")
            }
            $('.btn-page').removeClass("btn-page-active")
            $('.btn-page[data-btn=' + indice_page + ']').addClass("btn-page-active")
        }
        else if(filter == true){
            var cursos_visibles = $(".course-visible")
            cursos_visibles.css("display", "none")
            var n_course_max = indice_page * large_pag
            var n_course_min = n_course_max - large_pag
            for (var i = n_course_min; i < n_course_max; i++) {
                $('.course-visible:eq('+i+')').css("display", "")
            }
            $('.btn-page-filter').removeClass("btn-page-active")
            $('.btn-page-filter[data-btn=' + indice_page + ']').addClass("btn-page-active")
            
        }
    }
}())