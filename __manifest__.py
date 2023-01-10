
{
    'name': "School",

    'summary': """
    School
    """,

    'description': """
        School
    """,

    'author': "Farhan",
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': [],

    # always loaded
    'data': [
        #security
        "security/ir.model.access.csv",

        #views
        "views/student.xml",
        
        #menus
        "views/menu.xml",


    ],
    # only loaded in demonstration mode
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "AGPL-3"
}