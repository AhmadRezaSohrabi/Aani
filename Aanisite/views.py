import json
import sys
from django.shortcuts       import render, redirect
from django.http            import HttpResponseRedirect
from django.urls            import reverse
from django.views.generic   import ListView
from django.core.mail       import send_mail, EmailMessage
from .forms                 import EducationForm, EmploymentHistoryForm, EmploymentForm, ForeignLanguageForm
from .models                import Product, Form, TheraputicCategory
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
        context = json.loads(req_body)
        generic_name = data['generic_name']
        trade_name = data['trade_name']
        company_name = data['company_name']
        company_type = data['company_type']
        phone_number = data['phone_number']
        address = data['address']
        product_type = data['product_type']
        terapeutic_category = data['terapeutic_category']
        food_and_drug_administration_licenses = data['food_and_drug_administration_licenses']
        temperature_humidity_sensitive = data['temperature_humidity_sensitive']
        allowed_humidity_temperature_range = data['allowed_humidity_temperature_range']
        Light_Senfsitive = data['Light_Senfsitive']
        light_conditions = data['light_conditions']
        Api = data['Api']
        Oel = data['Oel']
        Oel_value = data['Oel_value']
        Valid_MSDS = data['Valid_MSDS']
        Source_Country_Raw_Material = data['Source_Country_Raw_Material']
        Type_Raw_Material = data['Type_Raw_Material']
        Presentation_washing_method = data['Presentation_washing_method']
        Producr_Batch_Weight = data['Producr_Batch_Weight']
        Producr_Batch_Number = data['Producr_Batch_Number']
        Production_Anticipation = data['Production_Anticipation']
        Tablet_or_Capsule = data['Tablet_or_Capsule']
        Kind_of_coat = data['Kind_of_coat']
        Description = data['Description']
        Specification_capsule_content = data['Specification_capsule_content']
        Granule_Production_Method = data['Granule_Production_Method']
        Granulator_Type = data['Granulator_Type']
        Moisture_Percentage_Granule = data['Moisture_Percentage_Granule']
        Required_Granulator_Tank = data['Required_Granulator_Tank']
        Glue_Making_Tank_Required = data['Glue_Making_Tank_Required']
        Temperature_Granulation = data['Temperature_Granulation']
        Mill_Mesh_Size = data['Mill_Mesh_Size']
        Fbd = data['Fbd']
        Mesh_for_API_Sieving = data['Mesh_for_API_Sieving']
        Mesh_Size_Required_Excipients_Sieving = data['Mesh_Size_Required_Excipients_Sieving']
        Required_Blender = data['Required_Blender']
        Required_Blender_Shape = data['Required_Blender_Shape']
        Press_Size = data['Press_Size']
        Press_Shape = data['Press_Shape']
        Punch_Specifications = data['Punch_Specifications']
        Hardness_Range_Tablet_Press = data['Hardness_Range_Tablet_Press']
        Diameter_Tablet_Press = data['Diameter_Tablet_Press']
        Thickness_Tablet_Press = data['Thickness_Tablet_Press']
        Tablet_Weight_Range = data['Tablet_Weight_Range']
        Capsule_Size = data['Capsule_Size']
        Empty_Shell_Weight = data['Empty_Shell_Weight']
        Range_Granule_Weight_Capsule = data['Range_Granule_Weight_Capsule']
        Storage_Temperature = data['Storage_Temperature']
        Humidity_Temperature = data['Humidity_Temperature']
        Containers = data['Containers']
        Press = data['Press']
        Capsule_Filling = data['Capsule_Filling']
        Coat = data['Coat']
        toC = data['toC']
        Container = data['Container']
        Material_Container = data['Material_Container']
        Container_Size = data['Container_Size'] 
        Container_Height = data['Container_Height']
        Opening_Diameter = data['Opening_Diameter']
        Cap_Model = data['Cap_Model']
        Number_Tablet_Capsules_perContainer = data['Number_Tablet_Capsules_perContainer']
        Cotton_SilicaGel = data['Cotton_SilicaGel']
        Number_SilicaGel = data['Number_SilicaGel']
        Blister_Type = data['Blister_Type']
        Pvc_Type = data['Pvc_Type']
        Pvc_Other = data['Pvc_Other']
        Blister_Dimensions = data['Blister_Dimensions']
        Aluminum_Foil_Width = data['Aluminum_Foil_Width']
        Pvc_Width = data['Pvc_Width']
        Number_Tablets_Blister = data['Number_Tablets_Blister']
        Number_Blister_Box = data['Number_Blister_Box']
        #Final_Product_Packaging_Contains = data['Final_Product_Packaging_Contains']
        cartNumber = data['cartNumber']
        leaflet = data['leaflet']
        ttac = data['ttac']
        finalContains_other = data['finalContains_other']
        Diameter = data['Diameter']
        Thickness = data['Thickness']
        Weight = data['Weight']
        Hardness = data['Hardness']
        Friability = data['Friability']
        Abrasion = data['Abrasion']
        Disintegration_Time = data['Disintegration_Time']
        Assay = data['Assay']
        qcTest = data['qcTest']
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
        representative = data['representative']
        authorised = data['authorised']
        context = data
       # raw_template = open(path.join(BASE_DIR , 'templates/jcc_pdf.html'))
       # rendered_template = Template(raw_template.read())
       # rendered_template = rendered_template.render(Context(context))
       # raw_template.close()
       # options={'page-size':'A4', 'dpi':400}
       # pdf_file = pdfkit.from_string(
       # rendered_template,
       # False,
       # options=options)
        file_name = 'contract.pdf'
        email = EmailMessage(
            'Contract submission',
            'Below contract is submitted. Please review and respond if possible.',
            'info.aanico@gmail.com',
            ['info.aanico@gmail.com', 'info.aanidarman@gmail.com'],
        )
        email.attach(file_name, pdf_file, 'application/pdf')
        email.send()
        return redirect('index')
    return render(request, 'Aanisite/contract.html')        
      