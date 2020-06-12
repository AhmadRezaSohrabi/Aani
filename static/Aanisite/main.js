$(document).ready(function () {
        $('#contractSubmit').click(function () {
                createTTMT();
        })

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
        img.onclick = function () {
                modal.style.display = "block";
                modalImg.src = this.src;
                captionText.innerHTML = this.alt;
        }
        var span = document.getElementsByClassName("close")[0];
        span.onclick = function () {
                modal.style.display = "none";
        }




        var modal = document.getElementById("myModal");
        var img = document.getElementById("C1");
        var modalImg = document.getElementById("img01");
        var captionText = document.getElementById("caption");
        img.onclick = function () {
                modal.style.display = "block";
                modalImg.src = this.src;
                captionText.innerHTML = this.alt;
        }
        var span = document.getElementsByClassName("close")[0];
        span.onclick = function () {
                modal.style.display = "none";
        }


        var modal = document.getElementById("myModal");
        var img = document.getElementById("C2");
        var modalImg = document.getElementById("img01");
        var captionText = document.getElementById("caption");
        img.onclick = function () {
                modal.style.display = "block";
                modalImg.src = this.src;
                captionText.innerHTML = this.alt;
        }
        var span = document.getElementsByClassName("close")[0];
        span.onclick = function () {
                modal.style.display = "none";
        }


        var modal = document.getElementById("myModal");
        var img = document.getElementById("C3");
        var modalImg = document.getElementById("img01");
        var captionText = document.getElementById("caption");
        img.onclick = function () {
                modal.style.display = "block";
                modalImg.src = this.src;
                captionText.innerHTML = this.alt;
        }
        var span = document.getElementsByClassName("close")[0];
        span.onclick = function () {
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
        img.onclick = function () {
                modal.style.display = "block";
                modalImg.src = this.src;
                captionText.innerHTML = this.alt;
        }
        var span = document.getElementsByClassName("close")[0];
        span.onclick = function () {
                modal.style.display = "none";
        }


        var modal = document.getElementById("myModal");
        var img = document.getElementById("C6");
        var modalImg = document.getElementById("img01");
        var captionText = document.getElementById("caption");
        img.onclick = function () {
                modal.style.display = "block";
                modalImg.src = this.src;
                captionText.innerHTML = this.alt;
        }
        var span = document.getElementsByClassName("close")[0];
        span.onclick = function () {
                modal.style.display = "none";
        }

        var modal = document.getElementById("myModal");
        var img = document.getElementById("C7");
        var modalImg = document.getElementById("img01");
        var captionText = document.getElementById("caption");
        img.onclick = function () {
                modal.style.display = "block";
                modalImg.src = this.src;
                captionText.innerHTML = this.alt;
        }
        var span = document.getElementsByClassName("close")[0];
        span.onclick = function () {
                modal.style.display = "none";
        }


        //ahmad
        function createTTMT() {
                let data = {
                        generic_name: $("#genericName").val(),
                        trade_name: $("#tradeName").val(),
                        company_name: $("#companyName").val(),
                        company_type: $("#companyType").val(),
                        phone_number: $("#phone").val(),
                        address: $("#address").val(),
                        product_type: $("#productType").val(),
                        therapeutic_category: $("#terapeuticCategory").val(),
                        food_and_drug_administration_licenses: $("#fdaLicenses").val(),
                        temperature_humidity_sensitive: checkit('#thSensitive'),
                        allowed_humidity_temperature_range: $("#thRange").val(),
                        light_sensitive: checkit('#lightSensitive'),
                        light_conditions: $("#lightRange").val(),
                        api: checkit('#apiCondition'),
                        oel: checkit('#oeLB'),
                        oel_value: $("#oeValue").val(),
                        valid_msds: checkit('#MSDS'),
                        source_country_raw_material: $("#rawSource").val(),
                        type_raw_material: $("#typeRaw").val(),
                        presentation_washing_method: $("#rawMethod").val(),
                        product_batch_weight: $("batchWeight").val(),
                        product_batch_number: $("batchNumber").val(),
                        production_anticipation: $("#productApp").val(),
                        tablet_or_capsule: $("#taCa").val(),
                        kind_of_coat: $("#tabKind").val(),
                        description: $("#description").val(),
                        granule_production_method: $("#gpMethod").val(),
                        granulator_type: $("#granulatorType").val(),
                        moisture_percentage_granule: $("#moisturePer").val(),
                        required_granulator_tank: $("#granuleTank").val(),
                        glue_making_tank_required: $("#glueTank").val(),
                        temperature_granulation: $("#tempGlue").val(),
                        mill_mesh_size: $("#millMeshSize").val(),
                        fbd: checkit('#fbd'),
                        mesh_for_api_sieving: $("#apiMeshSize").val(),
                        mesh_size_required_excipients_sieving: $("#excMeshSize").val(),
                        required_blender: $("#blenderReq").val(),
                        press_size: $("#pressSize").val(),
                        press_shape: $("#pressShape").val(),
                        punch_specifications: $("#punchSpec").val(),
                        hardness_range_tablet_press: $("#hardnessRange").val(),
                        diameter_tablet_press: $("#diameterRange").val(),
                        thickness_tablet_press: $("#thickRange").val(),
                        tablet_weight_range: $("#weightRange").val(),
                        specification_capsule: $("#specContent").val(),
                        capsule_size: $("#capsuleSize").val(),
                        empty_shell_weight: $("#emptyWeight").val(),
                        range_granule_weight_capsule: $("#capsuleRange").val(),
                        storage_temperature: $("#stTemp").val(),
                        humidity_temperature: $("#stHumid").val(),
                        containers: $("#stContainers").val(),
                        press: $("#pressPeriod").val(),
                        capsule_filling: $("#cFillPeriod").val(),
                        coat: $("#coatPeriod").val(),
                        toc: $("#toC").val(),
                        container: checkit('#containerCheck'),
                        material_container: $("#contMaterial").val(),
                        container_size: $("#sizeContainer").val(),
                        container_height: $("#heightContainer").val(),
                        opening_diameter: $("#openDiameter").val(),
                        cap_model: $("#capModel").val(),
                        number_tablet_capsules_percontainer: $("#contNumber").val(),
                        cotton_silicagel: $("#cotSil").val(),
                        number_silicagel: $("#siliGelNumber").val(),
                        blister_type: $("#blisterType").val(),
                        pvc_type: $("#pvcType").val(),
                        pvc_other: $("#pvcOther").val(),
                        blister_dimensions: $("#blisterDimention").val(),
                        aluminum_foil_width: $("#foilWidth").val(),
                        pvc_width: $("#pvcWidth").val(),
                        number_tablets_blister: $("#blisterNumber").val(),
                        number_blister_box: $("#boxNumber").val(),
                        leaflet: checkit("leaflet"),
                        number_box_carton: $("#cartNumber").val(),
                        final_contains: $("#finalContains").val(),
                        ttac: $("#ttac").val(),
                        diameter: checkit('#qcT1'),
                        thickness: checkit('#qcT2'),
                        weight: checkit('#qcT3'),
                        hardness: checkit('#qcT4'),
                        friability: checkit('#qcT5'),
                        abrasion: checkit('#qcT6'),
                        disintegration_time: checkit('#qcT7'),
                        assay: checkit('#qcT8'),
                        qc_test: $("#qcTest").val(),
                        t11: $("#t11").val(),
                        t12: $("#t12").val(),
                        t13: $("#t13").val(),
                        t21: $("#t21").val(),
                        t22: $("#t22").val(),
                        t23: $("#t23").val(),
                        t31: $("#t31").val(),
                        t32: $("#t32").val(),
                        t33: $("#t33").val(),
                        t41: $("#t41").val(),
                        t42: $("#t42").val(),
                        t43: $("#t43").val(),
                        t51: $("#t51").val(),
                        t52: $("#t52").val(),
                        t53: $("#t53").val(),
                        t61: $("#t61").val(),
                        t62: $("#t62").val(),
                        t63: $("#t63").val(),
                        t71: $("#t71").val(),
                        t72: $("#t72").val(),
                        t73: $("#t73").val(),
                        t81: $("#t81").val(),
                        t82: $("#t82").val(),
                        t83: $("#t83").val(),
                        t91: $("#t91").val(),
                        t92: $("#t92").val(),
                        t93: $("#t93").val(),
                        t101: $("#t101").val(),
                        t102: $("#t102").val(),
                        t103: $("#t103").val(),
                        t111: $("#t111").val(),
                        t112: $("#t112").val(),
                        t113: $("#t113").val(),
                        t121: $("#t121").val(),
                        t122: $("#t122").val(),
                        t123: $("#t123").val(),
                        representative: $("#representative").val(),
                        authorized_person: $("#authorizedPerson").val(),
                }

                $.ajax({
                        url: "/submit-contract/",
                        type: "POST",
                        data: JSON.stringify(data),
                        success: function (data) {
                                alert("your form successfully submitted");
                        }
                })
                return
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
                })
        }
});