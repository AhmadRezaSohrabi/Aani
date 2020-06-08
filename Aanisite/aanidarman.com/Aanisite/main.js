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




//form-contract-manufactoring


onreadystatechange(){
    $('').click( function(){
        createTTMT()
})


function createTTMT() {
        let data = {
            generic_name: $("#genericName").val().trim(),
            trade_name: $("#tradeName").val().trim(),
            company_name: $("#companyName").val(),
            company_type: $("#companyType").val(),
            phone_number: $("#Phone").val(),
            address: $("#address").val().trim(),
            product_type: $("#productType").val().trim(),
            terapeutic_category: $("#terapeuticCategory").val().trim(),
            food_and_drug_administration_licenses: $("#fdaLicenses").val().trim(),
            temperature_humidity_sensitive: checkit('#thSensitive'),
            allowed_humidity_temperature_range: $("#thRange").val().trim(),
            Light_Senfsitive: checkit('#lightSensitive'),
            light_conditions: $("#lightRange").val().trim(),
            Api: checkit('#apiCondition'),
            Oel: checkit('#oeLB'),
            Oel_value: $("#oeValue").val().trim(),
            Valid_MSDS: checkit('#MSDS'),
            Source_Country_Raw_Material: $("#rawSource").val().trim(),
            Type_Raw_Material: $("#typeRaw").val().trim(),
            Presentation_washing_method: $("#rawMethod").val().trim(),
            Producr_Batch_Weight: $("batchWeight").val().trim(),
            Producr_Batch_Number: $("batchNumber").val().trim(),
            Production_Anticipation: $("#productApp").val().trim(),
            Tablet_or_Capsule: $("#taCa").val().trim(),
            Kind_of_coat: $("#tabKind").val().trim(),
            Description: $("#description").val().trim(),
            Specification_capsule_content: $("#specContent").val().trim(),
            Granule_Production_Method: $("#gpMethod").val().trim(),
            Granulator_Type: $("#granulatorType").val().trim(),
            Moisture_Percentage_Granule: $("#moisturePer").val().trim(),
            Required_Granulator_Tank: $("#granuleTank").val().trim(),
            Glue_Making_Tank_Required: $("#glueTank").val().trim(),
            Temperature_Granulation: $("#tempGlue").val().trim(),
            Mill_Mesh_Size: $("#millMeshSize").val().trim(),
            Fbd: checkit('#fbd'),
            Mesh_for_API_Sieving: $("#apiMeshSize").val().trim(),
            Mesh_Size_Required_Excipients_Sieving: $("#excMeshSize").val().trim(),
            Required_Blender: $("#blenderReq").val().trim(),
            Required_Blender_Shape: $("#blenderShape").val().trim(),
            Press_Size: $("#pressSize").val().trim(),
            Press_Shape: $("#pressShape").val().trim(),
            Punch_Specifications: $("#punchSpec").val().trim(),
            Hardness_Range_Tablet_Press: $("#hardnessRange").val().trim(),
            Diameter_Tablet_Press: $("#diameterRange").val().trim(),
            Thickness_Tablet_Press: $("#thickRange").val().trim(),
            Tablet_Weight_Range: $("#weightRange").val().trim(),
            Capsule_Size: $("#capsuleSize").val().trim(),
            Empty_Shell_Weight: $("#emptyWeight").val().trim(),
            Range_Granule_Weight_Capsule: $("#capsuleRange").val().trim(),
            Storage_Temperature: $("#stTemp").val().trim(),
            Humidity_Temperature: $("#stHumid").val().trim(),
            Containers: $("#stContainers").val().trim(),
            Press: $("#pressPeriod").val().trim(),
            Capsule_Filling: $("#cFillPeriod").val().trim(),
            Coat: $("#coatPeriod").val().trim(),
            Container: checkit('#containerCheck'),
            Material_Container: $("#contMaterial").val().trim(),
            Container_Size: $("#sizeContainer").val().trim(),
            Container_Height: $("#heightContainer").val().trim(),
            Opening_Diameter: $("#openDiameter").val().trim(),
            Cap_Model: $("#capModel").val().trim(),
            Number_Tablet_Capsules_perContainer: $("#contNumber").val().trim(),
            Cotton_SilicaGel: $("#cotSil").val().trim(),
            Number_SilicaGel: $("#siliGelNumber").val().trim(),
            Blister_Type: $("#blisterType").val().trim(),
            Pvc_Type: $("#pvcType").val().trim(),
            Pvc_Other: $("#pvcOther").val().trim(),
            Blister_Dimensions: $("#blisterDimention").val().trim(),
            Aluminum_Foil_Width: $("#foilWidth").val().trim(),
            Pvc_Width: $("#pvcWidth").val().trim(),
            Number_Tablets_Blister: $("#blisterNumber").val().trim(),
            Number_Blister_Box: $("#boxNumber").val().trim(),
            Final_Product_Packaging_Contains: $("#pvcType").val().trim(), 
            finalContains_other: $("#finalContains").val().trim(),
            Diameter: checkit('#qcT1'),
            Thickness: checkit('#qcT2'),
            Weight: checkit('#qcT3'),
            Hardness: checkit('#qcT4'),
            Friability: checkit('#qcT5'),
            Abrasion: checkit('#qcT6'),
            Disintegration_Time: checkit('#qcT7'),
            Assay: checkit('#qcT8'),
            qcTest: $("#qcTest").val().trim(),
            t11: $("#t11").val().trim(),
            t12: $("#t12").val().trim(),
            t13: $("#t13").val().trim(),
            t21: $("#t21").val().trim(),
            t22: $("#t22").val().trim(),
            t23: $("#t23").val().trim(),
            t31: $("#t31").val().trim(),
            t32: $("#t32").val().trim(),
            t33: $("#t33").val().trim(),
            t41: $("#t41").val().trim(),
            t42: $("#t42").val().trim(),
            t43: $("#t43").val().trim(),
            t51: $("#t51").val().trim(),
            t52: $("#t52").val().trim(),
            t53: $("#t53").val().trim(),
            t61: $("#t61").val().trim(),
            t62: $("#t62").val().trim(),
            t63: $("#t63").val().trim(),
            t71: $("#t71").val().trim(),
            t72: $("#t72").val().trim(),
            t73: $("#t73").val().trim(),
            t81: $("#t81").val().trim(),
            t82: $("#t82").val().trim(),
            t83: $("#t83").val().trim(),
            t91: $("#t91").val().trim(),
            t92: $("#t92").val().trim(),
            t93: $("#t93").val().trim(),
            t101: $("#t101").val().trim(),
            t102: $("#t102").val().trim(),
            t103: $("#t103").val().trim(),
            t111: $("#t111").val().trim(),
            t112: $("#t112").val().trim(),
            t113: $("#t113").val().trim(),
            t121: $("#t121").val().trim(),
            t122: $("#t122").val().trim(),
            t123: $("#t123").val().trim(),
            representative: $("#representative").val().trim(),
            authorised: $("#authorised").val().trim(),
        }

        $.ajax({
            url: "/submit-ttmt/",
            type: "POST",
            data: JSON.stringify(data),
        })

      }
function checkit(checkboxId) {
    let checkbox = null;
    $(checkboxId).change(function () {
        if ($(this).attr('checked')) {
            $(this).val('TRUE');
            checkbox = true;
        } else {
            $(this).val('FALSE');
            checkbox = false;
        }
    return checkbox;
      }
 }