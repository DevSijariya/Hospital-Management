{
    'name': "Hospital_Management",
    'version': '18.0',
    'depends': ['base'],
    'author': "Codetrade",
    'category': 'Management',
    'description': """
        This is the custom Hospital Management model contain Data About the Doctors and the Patients 
    """,
    # data files always loaded at installation
    # xml file and security file are imported in data
    'data': [
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/medicines_view.xml',
        'wizard/patient_wizard.xml',
        'security/ir.model.access.csv',
    ],

    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'license':'LGPL-3',
    'installable':True,
    'application':True,
}
