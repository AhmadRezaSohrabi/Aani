$(document).ready(function () {

        $("#shape-panel > div label:nth-child(2)").click(function () {
                 $(this).siblings().removeClass('activebtn'); 
                 $(this).toggleClass('activebtn');
         });
        $("#category-panel > div label:nth-child(2)").click(function () {
                $(this).siblings().removeClass('activebtn1');
                $(this).toggleClass('activebtn1');
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

      


        //icon dropdown
        $('#dropdown-bars').click(function () {
                $('#dropdown-menu').slideToggle(1000);
        })
        




        $(window).scroll(function () {
                $('#dropdown-menu').slideUp(1000);
        })
        
        
        var modal = document.getElementById("myModal");
        var img = document.getElementById("Certificates");
        var modalImg = document.getElementById("img01");
        var captionText = document.getElementById("caption");
        img.onclick = function(){
         modal.style.display = "block";
         modalImg.src = this.src;
         captionText.innerHTML = this.alt;
        }
        var span = document.getElementsByClassName("close")[0];
        span.onclick = function() {
         modal.style.display = "none";
        }
        
        
        
        
        var modal = document.getElementById("myModal");
        var img = document.getElementById("C1");
        var modalImg = document.getElementById("img01");
        var captionText = document.getElementById("caption");
        img.onclick = function(){
         modal.style.display = "block";
         modalImg.src = this.src;
         captionText.innerHTML = this.alt;
        }
        var span = document.getElementsByClassName("close")[0];
        span.onclick = function() {
         modal.style.display = "none";
        }
        
        
         var modal = document.getElementById("myModal");
        var img = document.getElementById("C2");
        var modalImg = document.getElementById("img01");
        var captionText = document.getElementById("caption");
        img.onclick = function(){
         modal.style.display = "block";
         modalImg.src = this.src;
         captionText.innerHTML = this.alt;
        }
        var span = document.getElementsByClassName("close")[0];
        span.onclick = function() {
         modal.style.display = "none";
        }
        
        
         var modal = document.getElementById("myModal");
        var img = document.getElementById("C3");
        var modalImg = document.getElementById("img01");
        var captionText = document.getElementById("caption");
        img.onclick = function(){
         modal.style.display = "block";
         modalImg.src = this.src;
         captionText.innerHTML = this.alt;
        }
        var span = document.getElementsByClassName("close")[0];
        span.onclick = function() {
         modal.style.display = "none";
        }
        
        
        //  var modal = document.getElementById("myModal");
        // var img = document.getElementById("C4");
        // var modalImg = document.getElementById("img01");
        // var captionText = document.getElementById("caption");
        // img.onclick = function(){
        //  modal.style.display = "block";
        //  modalImg.src = this.src;
        //  captionText.innerHTML = this.alt;
        // }
        // var span = document.getElementsByClassName("close")[0];
        // span.onclick = function() {
        //  modal.style.display = "none";
        // }
        
         var modal = document.getElementById("myModal");
        var img = document.getElementById("C5");
        var modalImg = document.getElementById("img01");
        var captionText = document.getElementById("caption");
        img.onclick = function(){
         modal.style.display = "block";
         modalImg.src = this.src;
         captionText.innerHTML = this.alt;
        }
        var span = document.getElementsByClassName("close")[0];
        span.onclick = function() {
         modal.style.display = "none";
        }
        
        
         var modal = document.getElementById("myModal");
        var img = document.getElementById("C6");
        var modalImg = document.getElementById("img01");
        var captionText = document.getElementById("caption");
        img.onclick = function(){
         modal.style.display = "block";
         modalImg.src = this.src;
         captionText.innerHTML = this.alt;
        }
        var span = document.getElementsByClassName("close")[0];
        span.onclick = function() {
         modal.style.display = "none";
        }
        
         var modal = document.getElementById("myModal");
        var img = document.getElementById("C7");
        var modalImg = document.getElementById("img01");
        var captionText = document.getElementById("caption");
        img.onclick = function(){
         modal.style.display = "block";
         modalImg.src = this.src;
         captionText.innerHTML = this.alt;
        }
        var span = document.getElementsByClassName("close")[0];
        span.onclick = function() {
         modal.style.display = "none";
        }
});

$("#contractSubmit").click(function(){
    alert( "your form successfully submitted" );
});


//ahmad

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
            phone_number: $("#phone").val(),
            address: $("#address").val().trim(),
            product_type: $("#productType").val().trim(),
            therapeutic_category: $("#terapeuticCategory").val().trim(),
            food_and_drug_administration_licenses: $("#fdaLicenses").val().trim(),
            temperature_humidity_sensitive: checkit('#thSensitive'),
            allowed_humidity_temperature_range: $("#thRange").val().trim(),
            light_sensitive: checkit('#lightSensitive'),
            light_conditions: $("#lightRange").val().trim(),
            api: checkit('#apiCondition'),
            oel: checkit('#oeLB'),
            oel_value: $("#oeValue").val().trim(),
            valid_msds: checkit('#MSDS'),
            source_country_raw_material: $("#rawSource").val().trim(),
            type_raw_material: $("#typeRaw").val().trim(),
            presentation_washing_method: $("#rawMethod").val().trim(),
            product_batch_weight: $("batchWeight").val().trim(),
            product_batch_number: $("batchNumber").val().trim(),
            production_anticipation: $("#productApp").val().trim(),
            tablet_or_capsule: $("#taCa").val().trim(),
            kind_of_coat: $("#tabKind").val().trim(),
            description: $("#description").val().trim(),
            granule_production_method: $("#gpMethod").val().trim(),
            granulator_type: $("#granulatorType").val().trim(),
            moisture_percentage_granule: $("#moisturePer").val().trim(),
            required_granulator_tank: $("#granuleTank").val().trim(),
            glue_making_tank_required: $("#glueTank").val().trim(),
            temperature_granulation: $("#tempGlue").val().trim(),
            mill_mesh_size: $("#millMeshSize").val().trim(),
            fbd: checkit('#fbd'),
            mesh_for_api_sieving: $("#apiMeshSize").val().trim(),
            mesh_size_required_excipients_sieving: $("#excMeshSize").val().trim(),
            required_blender: $("#blenderReq").val().trim(),
            press_size: $("#pressSize").val().trim(),
            press_shape: $("#pressShape").val().trim(),
            punch_specifications: $("#punchSpec").val().trim(),
            hardness_range_tablet_press: $("#hardnessRange").val().trim(),
            diameter_tablet_press: $("#diameterRange").val().trim(),
            thickness_tablet_press: $("#thickRange").val().trim(),
            tablet_weight_range: $("#weightRange").val().trim(),
            specification_capsule: $("#specContent").val().trim(),
            capsule_size: $("#capsuleSize").val().trim(),
            empty_shell_weight: $("#emptyWeight").val().trim(),
            range_granule_weight_capsule: $("#capsuleRange").val().trim(),
            storage_temperature: $("#stTemp").val().trim(),
            humidity_temperature: $("#stHumid").val().trim(),
            containers: $("#stContainers").val().trim(),
            press: $("#pressPeriod").val().trim(),
            capsule_filling: $("#cFillPeriod").val().trim(),
            coat: $("#coatPeriod").val().trim(),
            toc: $("#toC").val().trim(),
            container: checkit('#containerCheck'),
            material_container: $("#contMaterial").val().trim(),
            container_size: $("#sizeContainer").val().trim(),
            container_height: $("#heightContainer").val().trim(),
            opening_diameter: $("#openDiameter").val().trim(),
            cap_model: $("#capModel").val().trim(),
            number_tablet_capsules_percontainer: $("#contNumber").val().trim(),
            cotton_silicagel: $("#cotSil").val().trim(),
            number_silicagel: $("#siliGelNumber").val().trim(),
            blister_type: $("#blisterType").val().trim(),
            pvc_type: $("#pvcType").val().trim(),
            pvc_other: $("#pvcOther").val().trim(),
            blister_dimensions: $("#blisterDimention").val().trim(),
            aluminum_foil_width: $("#foilWidth").val().trim(),
            pvc_width: $("#pvcWidth").val().trim(),
            number_tablets_blister: $("#blisterNumber").val().trim(),
            number_blister_box: $("#boxNumber").val().trim(),
            leaflet: checkit("leaflet"),
            number_box_carton: $("#cartNumber").val().trim(),
            final_contains: $("#finalContains").val().trim(),
            ttac: $("#ttac").val().trim(),
            diameter: checkit('#qcT1'),
            thickness: checkit('#qcT2'),
            weight: checkit('#qcT3'),
            hardness: checkit('#qcT4'),
            friability: checkit('#qcT5'),
            abrasion: checkit('#qcT6'),
            disintegration_time: checkit('#qcT7'),
            assay: checkit('#qcT8'),
            qc_test: $("#qcTest").val().trim(),
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
            authorized_person: $("#authorizedPerson").val().trim(),
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
    return checkbox
      }
    }
