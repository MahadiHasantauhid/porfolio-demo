import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=1)

layout = html.Div([
    dbc.Row([
        dbc.Col([
            dcc.Markdown('# MD MAHADI HASAN', className='mt-3', style={'text-align': 'center','color': 'green'}),
            dcc.Markdown('### Electrical And Automation Engineer', className='mb-5', style={'text-align': 'center'}),

        ])

    ]),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('BETS Consulting Services Limited',style={'color': 'orange','text-align': 'center','background-color':'#33475b'}),
            dcc.Markdown('Electrical Engineer', style={'font-weight': 'bold'}),
            dcc.Markdown('05/2016 - 02/2018')
        ]),
        dbc.Col([
            dcc.Markdown('Performed Duties',style={'color': 'orange','text-align': 'center','background-color':'#33475b'}),
            html.Ul([
                html.Li('Electrical Power Distribution System Design and Specifying using Computer aided design '
                        'tools(CAD).'),
                html.Li('Performed required Power System Studies and helped establishing design criteria at preliminary'
                        ' design stage.'),
                html.Li('Worked with Engineering team to Power System component Selection and Sizing of Transformer, '
                        'Circuit Breaker,Cables, Reactive Compensation as per Project requirement using '
                        'Standard Guideline.'),
                html.Li('Enforced International Electrical Guideline including IEEE, IEC, NEMA, UL, NFPA, and ISA '
                        'at FEED stage.'),
                html.Li('Prepared FAT (Factory Acceptance Test) checklist based on Guideline documents for Equipment'
                        ' (Pump, Motor) under test.'),
                html.Li('Conducted Environmental Impact Assessment(EIA) studies which include Air, Water quality '
                        'Monitoring and Data Analysis.'),
                html.Li('Participated in Monitoring and Supervision services of Environmental Compliance for '
                        'Power plants.'),
                html.Li('Helped writing reports including Inception Report, Monthly Progress Report.')
            ])
        ])
    ]),
    html.Hr(),
    dbc.Row([
        dbc.Col([
           dcc.Markdown('### Project Completed', style={'text-align': 'center','color': 'orange','background-color':'#33475b'})
        ])
    ]),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            html.Ul([
                html.Li('Consultancy Services for Design review,Construction Supervision of Dasherkandi Sewage'
                        'Treatment 500 MLD under EPC Turnkey Contract Management'),
                #html.Li('Employer: Dhaka WASA, Consultant Partners: Hankuk Engineering Consultant,Shah Technical'
                 #       'Consultants,BETS Consulting Services Limited, Sodev Technical Consultants Pvt.ltd')
            ])



        ])
    ]),
    #html.Hr(),
    dbc.Row([
        dbc.Col([
            html.Ul([
                html.Li('Feasiblity Study, Plan, Design, Preparation of BOQ, Work Supervision Etc. of Water supply system '
                        'of 37 District Towns Water Supply Projects.')
                #html.Li('Employer: DPHE, Consultant: BETS Consulting Services Limited')
                ])

        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Ul([
                 html.Li('Detail feasibility study of Constructing Common Utility Tunnel in '
                         'Dhaka South City Corporation'),
                 #html.Li('Employer:Dhaka South City Corporation, Consultant: BETS Consulting Services Limited')
            ])

        ])
    ]),

    dbc.Row([
        dbc.Col([
            html.Ul([
                html.Li('Environmental Monitoring Consultancy-Investment Promotion and Financing Facility (IPFF)'
                        ' under World Bank.'),
                #html.Li('Employer:World Bank, Consultant: BETS Consulting Services Limited')
                ])

        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Ul([
                html.Li('Environmental Impact Assessment (EIA) study of Small scale LNG floating storage'
                        ' and Re-gasification Unit (FSRU) Moored at KAFCO/CUFL Jetty on the Bank of'
                        ' Karnaphuli river Chittagong'),
                #html.Li('Employer:Karnaphuli Gas Transmission Company,'
                #        'Consultant: BETS Consulting Services Limited')

            ])

        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Ul([
                html.Li('Environmental Impact Assessment (EIA) for the Proposed Offshore LNG Floating Storage'
                        ' and Re-gasification Unit (FSRU) moored at STL (Submerged Turret Loading) Project'
                        ' at Maheshkhali under Cox’s Bazar '),
                #html.Li('Employer:Summit LNG Terminal Co. (Pvt.) Ltd,Consultant: BETS Consulting Services Limited')

            ])

        ])
    ]),
dbc.Row([
        dbc.Col([
            html.Ul([
                html.Li('Data Analysis Projects Consists of Sea Level Predictor, Time Series Visualizer,'
                        'Medical Data Visualizer, DemographicData Visualizer, Mean Variance-Standard Deviation Calculator.'),
                #html.Li('Employer:Summit LNG Terminal Co. (Pvt.) Ltd,Consultant: BETS Consulting Services Limited')

            ])

        ])
    ])


])