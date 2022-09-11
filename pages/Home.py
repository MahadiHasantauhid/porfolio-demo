import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import base64
dash.register_page(__name__ , path='/', order=0)
imagefile = 'assets/mypic.jpg'
encoded_image = base64.b64encode(open(imagefile, 'rb').read())
layout = html.Div([
    dbc.Row([
        dbc.Col([
            dcc.Markdown('# MD MAHADI HASAN',style={'text-align':'center', 'color': 'green'}),
            dcc.Markdown('### Electrical And Automation Engineer',style={'text-align':'center'})
        ]),
        #dbc.Col([
        #    html.Img(id='image', src='data:image/png;base64,{}'.format(encoded_image.decode()),
        #             style={'float': 'right','width': '50%','align': 'right'})

        #],width= 4)


    ]),# Selecting Image for the resume

    dbc.Row([
        dbc.Col([
            dcc.Markdown('# Summary',style={'text-align':'center','color': 'orange','background-color':'#33475b'}),
            html.Hr(),
            dcc.Markdown('I am a Proficient Electrical Engineer Capable of Demonstration Profound knowledge involving\n' 
                    'project planning, cost control, resource utilization and risk management. Highly skilled in\n' 
                    'the management of design engineering for large scale construction project.\n' 
                    'A recognized team player with ability to manage cross-functional project teams during\n'
                    'project development cycle and demonstrates the ability to build robust relationship with\n' 
                     'stakeholders and contractors to achieve project Deliverables and Milestones.\n',
                         style={'text-align':'center','white-space':'pre'})
        ])
    ]),
    dcc.Markdown('# Software Skills',style={'text-align':'center','color': 'orange','background-color':'#33475b'}),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''
            * Siemens TIA Portal
            * Allen Bradley Rslogix-500
            * ISPsoft Delta
            * Ignition Maker Edition
            
            ''')

        ],width=3),
        dbc.Col([
            dcc.Markdown('''
            * MySQL
            * Python
            * ETAP
            * EasyPower
            
            ''')
        ],width=3),
        dbc.Col([
            dcc.Markdown('''
            * Wonderware Aveva
            * WinCC
            * Revit
            * KepServerEX
        
            
            ''')
        ],width=3),
        dbc.Col([
            dcc.Markdown('''
            * Electrical CAD
            * Jupyter Notebook
            * Data Analysis 
            * Web app
        
        ''')
        ],width=3)


    ]),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('# Job Experience',style={'text-align': 'center','color': 'orange','background-color':'#33475b'}),


        ])
    ]),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('Hankuk Engineering Consultants',style={'color': 'orange','text-align': 'center','background-color':'#33475b'}),
            dcc.Markdown('Mid Level Electrical Engineer', style={'font-weight': 'bold'}),
            dcc.Markdown('02/2018 - 06/2020')
        ]),
        dbc.Col([
            dcc.Markdown('Performed Duties',style={'color': 'orange','text-align': 'center','background-color':'#33475b'}),
            html.Ul([
                html.Li('Medium and Low Voltage Cable Sizing, Circuit Breaker Selection (HV/LV), Transformer Selection'
                        '& Sizing, Reactive Power Compensation Calculation, VFD & Soft Starter Selection.'),
                html.Li('Single Line Design using CAD tools and Specifying Specification as per international Guideline'
                        'in order to establish design criteria at FEED stage.'),
                html.Li('TN-S Industrial Grounding System implementation and Performed Validation of Step and Touch '
                        'Voltage using Software Solutions.'),
                html.Li('Deployed Power System Relay Protection Design in accordance to IEEE guideline for Motor, '
                        'Transformer, Busbar.'),
                html.Li('Cable Sizing and Selection, Effective Ground-fault Calculation for validation of Cable sizes.'),
                html.Li('Power System Analysis including Load Flow Analysis, Short Circuit Analysis, Harmonic Analysis,'
                        ' and Motor starting Analysis.'),
                html.Li('Preliminary I/O Schedule, Field Instrumentation Selection, P&ID approval and PLC Programming '
                        'Using Siemens TIA Portal.'),
                html.Li('Attended FAT in China For Equipment such as Motor,Rotary kiln.'),
                html.Li('Fixed Design Criteria at FEED stage for Proper Construction Supervision as per Scope of work.'),
                html.Li('SCADA & HMI Design implementation and Supervision, Network Architecture, Topology & '
                        'Protocol Selection, Specifying requirements.'),
                html.Li('Design Engineering problems, fault finding using Simulation and Providing technical solution '
                        'according to International Guidelines at FEED stage.'),
                html.Li('Particiapated in Installation Supervision of Electrical Equipment such as Switchgear, Flow Meter,'
                        ' Submersible Pump.'),
                html.Li('Lighting Design of the Plant Facility both indoor and outdoor using Revit Model inside '
                        'Dialux Evo Environment as per NFPA, BNBC, and NESC Guideline.'),
                html.Li('Troubleshooting and fault finding using Siemens TIA portal.'),
                html.Li('Helped Model Switchgear Panel 3D Modelling for Design and Installation case review.'),
                html.Li('Issued RFI, NCR as a part of regular supervision task and also prepared field report regarding '
                        'construction issues.')

            ])
        ])
    ])

])