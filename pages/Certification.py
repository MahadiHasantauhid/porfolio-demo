import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=2)
layout = html.Div([
    dbc.Row([

        dbc.Col([
            #dcc.Markdown('# MD MAHADI HASAN',className='mt-3',style={'text-align':'center', 'color': 'green'}),
            #dcc.Markdown('### Electrical And Automation Engineer',className='mb-5',style={'text-align':'center'}),

        ])
    ]


    ),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('### Education', style={'text-align':'center','color': 'orange','background-color':'#33475b'})
        ])
    ]),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('Brac University.Dhaka', style={'font-weight': 'bold'}),
            dcc.Markdown('11/2014')
        ]),
        dbc.Col([
            dcc.Markdown('Electronics and Communication Engineering', style={'font-weight': 'bold'}),

        ])

    ]),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('### Publication', style={'text-align':'center','color': 'orange','background-color':'#33475b'})
        ])

    ]),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('[Brac University](https://www.bracu.ac.bd/)',link_target='_blank'),
            dcc.Markdown('15/2012')
        ]),
        dbc.Col([
            dcc.Markdown('[Designing of an office appliance system using temperature sensor & micro controller for '
                         'efficient use of electricity](http://hdl.handle.net/10361/2378)',link_target='_blank')
        ])
    ]),

    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('### Professional Certification',style={'text-align':'center','color': 'orange','background-color':'#33475b'}),
        ])
    ]),
    html.Hr(),
    dbc.Row([
        dbc.Col([

           # dcc.Markdown('Issued Authority'),
            dcc.Markdown('[RealPars](https://realpars.com/)',link_target='_blank')



        ]),
        dbc.Col([
             dcc.Markdown('[PLC Programming Made Easy -(Level 4)](https://learn.realpars.com/certificates/toay21xtfd)',
                         link_target='_blank'),
            dcc.Markdown()
        ])

    ]),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('[RealPars](https://realpars.com/)',link_target='_blank'),
            #dcc.Markdown('Issued Authority')


        ]),
        dbc.Col([
             dcc.Markdown('[PLCNext Ladder Logic Programming](https://learn.realpars.com/certificates/sggnjp8gub)',
                         link_target='_blank'),
            dcc.Markdown()
        ])

    ]),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('[RealPars](https://realpars.com/)',link_target='_blank'),
            #dcc.Markdown('Issued Authority')


        ]),
        dbc.Col([
             dcc.Markdown('[Allen Bradley PLC Programming-Advanced Course](https://learn.realpars.com/certificates/dxvzorbrbc)',
                         link_target='_blank'),
            dcc.Markdown()
        ])

    ]),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('[RealPars](https://realpars.com/)',link_target='_blank'),
           # dcc.Markdown('Issued Authority')


        ]),
        dbc.Col([
             dcc.Markdown('[PLC Program Made Easy-Level 3](https://learn.realpars.com/certificates/cqsoq48vru)',
                         link_target='_blank'),

        ])

    ]),dbc.Row([
        dbc.Col([
            dcc.Markdown('[RealPars](https://realpars.com/)',link_target='_blank'),
           # dcc.Markdown('Issued Authority')


        ]),
        dbc.Col([
             dcc.Markdown('[Configure a Profibus-DP Network](https://learn.realpars.com/certificates/qnueolalmi)',
                         link_target='_blank'),

        ])

    ]),dbc.Row([
        dbc.Col([
            dcc.Markdown('[RealPars](https://realpars.com/)',link_target='_blank'),
            #dcc.Markdown('Issued Authority')


        ]),
        dbc.Col([
             dcc.Markdown('[PROFINET Made Easy-Configure a Profinet Device](https://learn.realpars.com/certificates/p9cf9n0zso)',
                         link_target='_blank'),

        ])

    ]),dbc.Row([
        dbc.Col([
            dcc.Markdown('[RealPars](https://realpars.com/)',link_target='_blank'),
            #dcc.Markdown('Issued Authority')


        ]),
        dbc.Col([
             dcc.Markdown('[WinCC-Program Siemens HMIs By Building Real World Applications ](https://learn.realpars.com/certificates/w8m2epjfli)',
                         link_target='_blank'),

        ])

    ]),dbc.Row([
        dbc.Col([
            dcc.Markdown('[Scantime Automation & Training](https://www.scantime.co.uk/)',link_target='_blank'),
            #dcc.Markdown('Issued Authority')


        ]),
        dbc.Col([
             dcc.Markdown('[Siemens TIA Portal Programming ](https://www.scantime.co.uk/)',
                         link_target='_blank'),

        ])

    ]),dbc.Row([
        dbc.Col([
            dcc.Markdown('[FreeCodeCamp](https://www.freecodecamp.org/)',link_target='_blank'),
            #dcc.Markdown('Issued Authority')


        ]),
        dbc.Col([
             dcc.Markdown('[Data Analysis with Python](https://www.freecodecamp.org/certification/fccf32756cb-4f07-4c39-9614-f3fe235f8875/data-analysis-with-python-v7)',
                         link_target='_blank'),

        ])

    ]),










])

