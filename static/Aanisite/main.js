// hidden shodan hame ghesmat ha dar badve vorood
$("#historyText").css("display", "none");
$("#viewText").css("display", "none");
$("#missionText").css("display", "none");
$("#holdingGroupText").css("display", "none");
$("#eventText").css("display", "none");

//cocdehaye type effect

// bakhsh namayan ya makhfi shodan section haye mokhtalef site injas ke shayad badan ba jquery zadim

var a
a = document.getElementById("main-tag")
a.addEventListener("click", function () {
        $("#motto").css("diplay", "none");
        counter = 0;
        typeWriter();
})

$(document).ready(function () {

         $("div label").click(function () {
                 $(this).siblings().removeClass('activebtn'); 
                 $(this).toggleClass('activebtn');
         });
        (function ($) {
                $.fn.visible = function (partial) {

                        var $t = $(this),
                                $w = $(window),
                                viewTop = $w.scrollTop(),
                                viewBottom = viewTop + $w.height(),
                                _top = $t.offset().top,
                                _bottom = _top + $t.height(),
                                compareTop = partial === true ? _bottom : _top,
                                compareBottom = partial === true ? _top : _bottom;

                        return ((compareBottom <= viewBottom) && (compareTop >= viewTop));

                };

        })(jQuery);
        $(window).scroll(function (event) {

                $(".cardMainDivright").each(function (i, el) {
                        var el = $(el);
                        if (el.visible(true)) {
                                el.addClass("come-in");
                        }
                });

                $(".cardMainDivleft").each(function (i, el) {
                        var el = $(el);
                        if (el.visible(true)) {
                                el.addClass("come-inleft");
                        }
                });

        });

        var win = $(window);
        var allMods = $(".module");

        // Already visible modules
        allMods.each(function (i, el) {
                var el = $(el);
                if (el.visible(true)) {
                        el.addClass("already-visible");
                }
        });

        win.scroll(function (event) {

                allMods.each(function (i, el) {
                        var el = $(el);
                        if (el.visible(true)) {
                                el.addClass("come-in");
                        }
                });

        });


        //Preloader
        $(window).on("load", function () {
                preloaderFadeOutTime = 500;

                function hidePreloader() {
                        var preloader = $('.spinner-wrapper');
                        preloader.fadeOut(preloaderFadeOutTime);
                }
                hidePreloader();
        });

        typeWriter();


        //icon dropdown
        $('#dropdown-bars').click(function () {
                $('#dropdown-menu').slideToggle(1000);
        })
        




        $(window).scroll(function () {
                $('#dropdown-menu').slideUp(1000);
        })

});


var myCenter = new google.maps.LatLng(35.755316, 51.416302);

function initialize() {
        var mapProp = {
                center: myCenter,
                zoom: 20,
                mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        var map = new google.maps.Map(document.getElementById("map"), mapProp);
        var marker = new google.maps.Marker({
                position: myCenter,
        });
        marker.setMap(map);
}
google.maps.event.addDomListener(window, 'load', initialize);


