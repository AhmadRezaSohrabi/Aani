import os
import json
import sys
from django.shortcuts       import render, redirect
from django.http            import HttpResponseRedirect, HttpResponse
from django.urls            import reverse
from django.views.generic   import ListView
from django.template  import Template, Context
from django.conf            import settings
from django.core.mail       import send_mail, EmailMessage
from .forms                 import EducationForm, EmploymentHistoryForm, EmploymentForm, ForeignLanguageForm
from .models                import *
from django.db.models       import Q

# Create your views here.

def index(request):
    return render(request, 'Aanisite/index.html')


# Create your views here.
def employment_form_render(request):
    if request.method == "POST":
        employment_form = EmploymentForm(request.POST)
        education_form = EducationForm(request.POST)
        foreign_language_form = ForeignLanguageForm(request.POST)
        employment_history_form = EmploymentHistoryForm(request.POST)
        if employment_form.is_valid():
            subject = 'employment request'
            surname = employment_form.cleaned_data['surname']
            name = employment_form.cleaned_data['name']
            birth_date = employment_form.cleaned_data['birth_date']
            identification_number = employment_form.cleaned_data['identification_number']
            telephone = employment_form.cleaned_data['telephone']
            home_address = employment_form.cleaned_data['home_address']
            post_code = employment_form.cleaned_data['post_code']
            email = employment_form.cleaned_data['email']
            future_positions = employment_form.cleaned_data['future_positions']
            send_mail(
                subject=subject,
                message="{} the {} born in {} with ID of {} has requested an employment application".format(surname,name,birth_date,identification_number),
                from_email=email,
                recipient_list=['info.aanidarman@gmail.com'],
            )
            return redirect(reverse('index'))

    employment_form = EmploymentForm()
    education_form = EducationForm()
    foreign_language_form = ForeignLanguageForm()
    employment_history_form = EmploymentHistoryForm()
    print(employment_form)
    return render(request, 'Aanisite/hire.html', {'e_form': employment_form ,'edu_form': education_form , 'lang_form': foreign_language_form ,'e_history_form': employment_history_form})            

            
def products_view(request):
    lol = None
    queryset = None
    if request.GET:
        requested_parameter = list(request.GET.values())[0]
        if requested_parameter in ['Capsule', 'Tablet']:
            lol = requested_parameter
            queryset = Product.objects.filter(form__name=requested_parameter)
        else:
            queryset = Product.objects.filter(theraputic_category__name=requested_parameter)
    return render(request, 'Aanisite/products.html', {'product_list': queryset, 'lol': lol})
    
def contact_us_form_handler(request):
    if request.method == "POST":
        client_name    = request.POST.get('your-name')
        client_email   = request.POST.get('your-email')
        subject        = request.POST.get('your-subject')
        message        = request.POST.get('your-message')
        try:
            # Todo handle form inputs
            message = f"Sender:{client_name}\nEmail:{client_email}\n\n{message}"
            send_mail(
                subject=subject,
                message=message,
                from_email=client_email,
                recipient_list=['info.aanico@gmail.com'],
            )
        except Exception as e:
            message = f"Sender:{client_name}\n\n\nThis user tried to contact you but some problem has occured!!"
            send_mail(
                subject=subject,
                message=message,
                from_email=client_email,
                recipient_list=['info.aanico@gmail.com'],
            )
        return redirect('index')
    else:
        return redirect('index')
        
        
def contract(request):
    if request.method == "POST":
        req_body = request.body.decode('utf-8')
        data = json.loads(req_body)
        generic_name = data['generic_name']
        trade_name = data['trade_name']
        company_name = data['company_name']
        company_type = data['company_type']
        phone_number = data['phone_number']
        address = data['address']
        product_type = data['product_type']
        therapeutic_category = data['therapeutic_category']
        food_and_drug_administration_licenses = data['food_and_drug_administration_licenses']
        representative = data['representative']
        authorized_person = data['authorized_person']


        temperature_humidity_sensitive = data['temperature_humidity_sensitive']
        allowed_humidity_temperature_range = data['allowed_humidity_temperature_range']
        light_senfsitive = data['light_senfsitive']
        light_conditions = data['light_conditions']
        api = data['api']
        oel = data['oel']
        oel_value = data['oel_value']
        valid_msds = data['valid_msds']
        source_country_raw_material = data['source_country_raw_material']
        type_raw_material = data['type_raw_material']
        presentation_washing_method = data['presentation_washing_method']


        product_batch_weight = data['product_batch_weight']
        product_batch_number = data['product_batch_number']
        production_anticipation = data['production_anticipation']
        tablet_or_capsule = data['tablet_or_capsule']
        kind_of_coat = data['kind_of_coat']
        description = data['description']
        granule_production_method = data['granule_production_method']
        granulator_type = data['granulator_type']
        moisture_percentage_granule = data['moisture_percentage_granule']
        required_granulator_tank = data['required_granulator_tank']
        glue_making_tank_required = data['glue_making_tank_required']
        temperature_granulation = data['temperature_granulation']
        mill_mesh_size = data['mill_mesh_size']
        fbd = data['fbd']
        mesh_for_api_sieving = data['mesh_for_api_sieving']
        mesh_size_required_excipients_sieving = data['mesh_size_required_excipients_sieving']
        required_blender = data['required_blender']
        press_size = data['press_size']
        press_shape = data['press_shape']
        punch_specifications = data['punch_specifications']
        hardness_range_tablet_press = data['hardness_range_tablet_press']
        diameter_tablet_press = data['diameter_tablet_press']
        thickness_tablet_press = data['thickness_tablet_press']
        tablet_weight_range = data['tablet_weight_range']
        specification_capsule = data['specification_capsule']
        capsule_size = data['capsule_size']
        empty_shell_weight = data['empty_shell_weight']
        range_granule_weight_capsule = data['range_granule_weight_capsule']
        storage_temperature = data['storage_temperature']
        humidity_temperature = data['humidity_temperature']
        containers = data['containers']
        press = data['press']
        capsule_filling = data['capsule_filling']
        coat = data['coat']


        toc = data['toc']
        container = data['container']
        material_container = data['material_container']
        container_size = data['container_size'] 
        container_height = data['container_height']
        opening_diameter = data['opening_diameter']
        cap_model = data['cap_model']
        number_tablet_capsules_percontainer = data['number_tablet_capsules_percontainer']
        cotton_silicagel = data['cotton_silicagel']
        number_silicagel = data['number_silicagel']
        blister_type = data['blister_type']
        pvc_type = data['pvc_type']
        pvc_other = data['pvc_other']
        blister_dimensions = data['blister_dimensions']
        aluminum_foil_width = data['aluminum_foil_width']
        pvc_width = data['pvc_width']
        number_tablets_blister = data['number_tablets_blister']
        number_blister_box = data['number_blister_box']
        leaflet = data['leaflet']
        number_box_carton = data['number_box_carton']
        final_contains = data['final_contains']
        ttac = data['ttac']



        diameter = data['diameter']
        thickness = data['thickness']
        weight = data['weight']
        hardness = data['hardness']
        friability = data['friability']
        abrasion = data['abrasion']
        disintegration_time = data['disintegration_time']
        assay = data['assay']
        qc_test = data['qc_test']
        t11 = data['t11']
        t12 = data['t12']
        t13 = data['t13']
        t21 = data['t21']
        t22 = data['t22']
        t23 = data['t23']
        t31 = data['t31']
        t32 = data['t32']
        t33 = data['t33']
        t41 = data['t41']
        t42 = data['t42']
        t43 = data['t43']
        t51 = data['t51']
        t52 = data['t52']
        t53 = data['t53']
        t61 = data['t61']
        t62 = data['t62']
        t63 = data['t63']
        t71 = data['t71']
        t72 = data['t72']
        t73 = data['t73']
        t81 = data['t81']
        t82 = data['t82']
        t83 = data['t83']
        t91 = data['t91']
        t92 = data['t92']
        t93 = data['t93']
        t101 = data['t101']
        t102 = data['t102']
        t103 = data['t103']
        t111 = data['t111']
        t112 = data['t112']
        t113 = data['t113']
        t121 = data['t121']
        t122 = data['t122']
        t123 = data['t123']

        raw_material_and_excipient_specifications= RawMaterialAndExcipientSpecifications.objects.create(
            temperature_humidity_sensitive=temperature_humidity_sensitive,
            allowed_humidity_temperature_range=allowed_humidity_temperature_range,
            light_senfsitive=light_senfsitive,
            light_conditions=light_conditions,
            api=api,
            oel=oel,
            oel_value=oel_value,
            valid_msds=valid_msds,
            source_country_raw_material=source_country_raw_material,
            type_raw_material=type_raw_material,
            presentation_washing_method=presentation_washing_method
        )

        specifications_of_devices_and_equipment_used_in_production= SpecificationsOfDevicesAndEquipmentUsedInProduction.objects.create(
            product_batch_weight=product_batch_weight,
            product_batch_number=product_batch_number,
            production_anticipation=production_anticipation,
            tablet_or_capsule=tablet_or_capsule,
            kind_of_coat=kind_of_coat,
            description=description,
            granule_production_method=granule_production_method,
            granulator_type=granulator_type,
            moisture_percentage_granule=moisture_percentage_granule,
            required_granulator_tank=required_granulator_tank,
            glue_making_tank_required=glue_making_tank_required,
            temperature_granulation=temperature_granulation,
            mill_mesh_size=mill_mesh_size,
            fbd=fbd,
            mesh_for_api_sieving=mesh_for_api_sieving,
            mesh_size_required_excipients_sieving=mesh_size_required_excipients_sieving,
            required_blender=required_blender,
            press_size=press_size,
            press_shape=press_shape,
            punch_specifications=punch_specifications,
            hardness_range_tablet_press=hardness_range_tablet_press,
            diameter_tablet_press=diameter_tablet_press,
            thickness_tablet_press=thickness_tablet_press,
            tablet_weight_range=tablet_weight_range,
            specification_capsule=specification_capsule,
            capsule_size=capsule_size,
            empty_shell_weight=empty_shell_weight,
            range_granule_weight_capsule=range_granule_weight_capsule,
            storage_temperature=storage_temperature,
            humidity_temperature=humidity_temperature,
            containers=containers,
            press=press,
            capsule_filling=capsule_filling,
            coat=coat
        )

        packagin_material_specifications = PackagingMaterialsSpecifications.objects.create(
            toc=toc,
            container=container,
            material_container=material_container,
            container_size=container_size,
            container_height=container_height,
            opening_diameter=opening_diameter,
            cap_model=cap_model,
            number_tablet_capsules_percontainer=number_tablet_capsules_percontainer,
            cotton_silicagel=cotton_silicagel,
            number_silicagel=number_silicagel,
            blister_type=blister_type,
            pvc_type=pvc_type,
            pvc_other=pvc_other,
            blister_dimensions=blister_dimensions,
            aluminum_foil_width=aluminum_foil_width,
            pvc_width=pvc_width,
            number_tablets_blister=number_tablets_blister,
            number_blister_box=number_blister_box,
            leaflet=leaflet,
            number_box_carton=number_box_carton,
            final_contains=final_contains,
            ttac=ttac,
        )

        experiments = Experiments.objects.create(
            diameter=diameter,
            thickness=thickness,
            weight=weight,
            hardness=hardness,
            friability=friability,
            abrasion=abrasion,
            disintegration_time=disintegration_time,
            assay=assay,
            qc_test=qc_test,
            t11=t11,
            t12=t12,
            t13=t13,
            t21=t21,
            t22=t22,
            t23=t23,
            t31=t31,
            t32=t32,
            t33=t33,
            t41=t41,
            t42=t42,
            t43=t43,
            t51=t51,
            t52=t52,
            t53=t53,
            t61=t61,
            t62=t62,
            t63=t63,
            t71=t71,
            t72=t72,
            t73=t73,
            t81=t81,
            t82=t82,
            t83=t83,
            t91=t91,
            t92=t92,
            t93=t93,
            t101=t101,
            t102=t102,
            t103=t103,
            t111=t111,
            t112=t112,
            t113=t113,
            t121=t121,
            t122=t122,
            t123=t123
        )


        TTMTContract.objects.create(
            generic_name=generic_name,
            trade_name=trade_name,
            company_name=company_name,
            company_type=company_type,
            phone_number=phone_number,
            address=address,
            product_type=product_type,
            therapeutic_category=therapeutic_category,
            food_and_drug_administration_licenses=food_and_drug_administration_licenses,
            representative=representative,
            authorized_person=authorized_person,
            raw_material_and_excipient_specifications=raw_material_and_excipient_specifications,
            specifications_of_devices_and_equipment_used_in_production=specifications_of_devices_and_equipment_used_in_production,
            packagin_material_specifications=packagin_material_specifications,
            experiments=experiments,
        )

        raw_template = open(os.path.join(settings.BASE_DIR , 'Aanisite/templates/export.html'))
        rendered_template = Template(raw_template.read())
        rendered_template = rendered_template.render(Context(data))
        raw_template.close()
        return HttpResponse(rendered_template)
        file_name = 'contract_export.html'
        email = EmailMessage(
            'Contract submission',
            'A new contract is submitted. Contact system administrator for contract detail.',
            'info.aanico@gmail.com',
            ['info.aanico@gmail.com', 'info.aanidarman@gmail.com'],
        )
        email.attach(file_name, rendered_template, 'application/pdf')
        email.send()
        return redirect('index')
    return render(request, 'Aanisite/contract.html')        
      