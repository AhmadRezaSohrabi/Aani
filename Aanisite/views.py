import os
import json
import sys
from django.shortcuts       import render, redirect
from django.http            import HttpResponseRedirect, HttpResponse, JsonResponse
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
            surname = employment_form.cleaned_data.get('surname')
            name = employment_form.cleaned_data.get('name')
            birth_date = employment_form.cleaned_data.get('birth_date')
            identification_number = employment_form.cleaned_data.get('identification_number')
            telephone = employment_form.cleaned_data.get('telephone')
            home_address = employment_form.cleaned_data.get('home_address')
            post_code = employment_form.cleaned_data.get('post_code')
            email = employment_form.cleaned_data.get('email')
            future_positions = employment_form.cleaned_data.get('future_positions')
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
    return render(request, 'Aanisite/contract.html')

def submit_contract(request):
    print('111111111111111111111111111111')
    req_body = request.body.decode('utf-8')
    data = json.loads(req_body)
    generic_name = data.get('generic_name')
    trade_name = data.get('trade_name')
    company_name = data.get('company_name')
    company_type = data.get('company_type')
    phone_number = data.get('phone_number')
    address = data.get('address')
    product_type = data.get('product_type')
    therapeutic_category = data.get('therapeutic_category')
    food_and_drug_administration_licenses = data.get('food_and_drug_administration_licenses')
    representative = data.get('representative')
    authorized_person = data.get('authorized_person')


    temperature_humidity_sensitive = data.get('temperature_humidity_sensitive')
    allowed_humidity_temperature_range = data.get('allowed_humidity_temperature_range')
    light_sensitive = data.get('light_sensitive')
    light_conditions = data.get('light_conditions')
    api = data.get('api')
    oel = data.get('oel')
    oel_value = None
    valid_msds = data.get('valid_msds')
    source_country_raw_material = data.get('source_country_raw_material')
    type_raw_material = data.get('type_raw_material')
    presentation_washing_method = data.get('presentation_washing_method')

    print('222222222222222222222222222')
    product_batch_weight = data.get('product_batch_weight', None)
    product_batch_number = data.get('product_batch_number', None)
    production_anticipation = None
    tablet_or_capsule = data.get('tablet_or_capsule')
    kind_of_coat = data.get('kind_of_coat')
    description = data.get('description')
    granule_production_method = data.get('granule_production_method')
    granulator_type = data.get('granulator_type')
    moisture_percentage_granule = data.get('moisture_percentage_granule')
    required_granulator_tank = data.get('required_granulator_tank')
    glue_making_tank_required = data.get('glue_making_tank_required')
    temperature_granulation = data.get('temperature_granulation')
    mill_mesh_size = data.get('mill_mesh_size')
    fbd = data.get('fbd')
    mesh_for_api_sieving = data.get('mesh_for_api_sieving')
    mesh_size_required_excipients_sieving = data.get('mesh_size_required_excipients_sieving')
    required_blender = data.get('required_blender')
    press_size = data.get('press_size')
    press_shape = data.get('press_shape')
    punch_specifications = data.get('punch_specifications')
    hardness_range_tablet_press = data.get('hardness_range_tablet_press')
    diameter_tablet_press = data.get('diameter_tablet_press')
    thickness_tablet_press = data.get('thickness_tablet_press')
    tablet_weight_range = data.get('tablet_weight_range')
    specification_capsule = data.get('specification_capsule')
    capsule_size = data.get('capsule_size')
    empty_shell_weight = data.get('empty_shell_weight')
    range_granule_weight_capsule = data.get('range_granule_weight_capsule')
    storage_temperature = data.get('storage_temperature')
    humidity_temperature = data.get('humidity_temperature')
    containers = data.get('containers')
    press = data.get('press')
    capsule_filling = data.get('capsule_filling')
    coat = data.get('coat')


    toc = data.get('toc')
    container = data.get('container')
    material_container = data.get('material_container')
    container_size = data.get('container_size') 
    container_height = data.get('container_height')
    opening_diameter = data.get('opening_diameter')
    cap_model = data.get('cap_model')
    number_tablet_capsules_percontainer = data.get('number_tablet_capsules_percontainer')
    cotton_silicagel = data.get('cotton_silicagel')
    number_silicagel = data.get('number_silicagel')
    blister_type = data.get('blister_type')
    pvc_type = data.get('pvc_type')
    pvc_other = data.get('pvc_other')
    blister_dimensions = data.get('blister_dimensions')
    aluminum_foil_width = data.get('aluminum_foil_width')
    pvc_width = data.get('pvc_width')
    number_tablets_blister = data.get('number_tablets_blister')
    number_blister_box = data.get('number_blister_box')
    leaflet = data.get('leaflet')
    number_box_carton = data.get('number_box_carton')
    final_contains = data.get('final_contains')
    ttac = data.get('ttac')



    diameter = data.get('diameter')
    thickness = data.get('thickness')
    weight = data.get('weight')
    hardness = data.get('hardness')
    friability = data.get('friability')
    abrasion = data.get('abrasion')
    disintegration_time = data.get('disintegration_time')
    assay = data.get('assay')
    qc_test = data.get('qc_test')
    t11 = data.get('t11')
    t12 = data.get('t12')
    t13 = data.get('t13')
    t21 = data.get('t21')
    t22 = data.get('t22')
    t23 = data.get('t23')
    t31 = data.get('t31')
    t32 = data.get('t32')
    t33 = data.get('t33')
    t41 = data.get('t41')
    t42 = data.get('t42')
    t43 = data.get('t43')
    t51 = data.get('t51')
    t52 = data.get('t52')
    t53 = data.get('t53')
    t61 = data.get('t61')
    t62 = data.get('t62')
    t63 = data.get('t63')
    t71 = data.get('t71')
    t72 = data.get('t72')
    t73 = data.get('t73')
    t81 = data.get('t81')
    t82 = data.get('t82')
    t83 = data.get('t83')
    t91 = data.get('t91')
    t92 = data.get('t92')
    t93 = data.get('t93')
    t101 = data.get('t101')
    t102 = data.get('t102')
    t103 = data.get('t103')
    t111 = data.get('t111')
    t112 = data.get('t112')
    t113 = data.get('t113')
    t121 = data.get('t121')
    t122 = data.get('t122')
    t123 = data.get('t123')

    print(oel_value)
    print(product_batch_weight)
    print(product_batch_number)
    print(production_anticipation)
    raw_material_and_excipient_specifications = RawMaterialAndExcipientSpecifications.objects.create(
        temperature_humidity_sensitive=temperature_humidity_sensitive,
        allowed_humidity_temperature_range=allowed_humidity_temperature_range,
        light_sensitive=light_sensitive,
        light_conditions=light_conditions,
        api=api,
        oel=oel,
        oel_value=oel_value,
        valid_msds=valid_msds,
        source_country_raw_material=source_country_raw_material,
        type_raw_material=type_raw_material,
        presentation_washing_method=presentation_washing_method,
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

    packaging_material_specifications = PackagingMaterialsSpecifications.objects.create(
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
        packaging_materials_specifications=packaging_material_specifications,
        experiments=experiments,
    )

    raw_template = open(os.path.join(settings.BASE_DIR , 'Aanisite/templates/Aanisite/export.html'))
    rendered_template = Template(raw_template.read())
    rendered_template = rendered_template.render(Context(data))
    raw_template.close()
    file_name = 'contract_detail.html'
    email = EmailMessage(
        'Contract submission',
        'A new contract is submitted. Contact system administrator for contract detail.',
        'info.aanico@gmail.com',
        ['info.aanico@gmail.com', 'info.aanidarman@gmail.com'],
    )
    email.attach(file_name, rendered_template, 'application/pdf')
    email.send()
    return JsonResponse({'message': 'success'})