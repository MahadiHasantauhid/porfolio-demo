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
            dcc.Markdown('''I am a Proficient Electrical Engineer Capable of Demonstration Profound knowledge involving
                    project planning, cost control, resource utilization and risk management. Highly skilled in
                    the management of design engineering for large scale construction project. 
                    A recognized team player with  ability to manage cross-functional project teams during'
                    project development cycle and demonstrates the ability to build robust relationship with' 
                     stakeholders and contractors to achieve project Deliverables and Milestones.''',
                         style={'text-align':'center','white-space':'normal','text-align':'justify','text-justify': 'inter-word'})
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

                html.Li('Designed Single Line Diagram using CAD tools and fixed Specification as per international Guideline'
                        ' in order to establish design criteria at FEED stage.'),
                html.Li('Implemented TN-S Industrial Grounding System and Performed Validation of Step and Touch '
                        'Voltage using Software Solutions.'),
                html.Li('Deployed Power System Relay Protection Design in accordance to IEEE guideline for Motor, '
                        ' Transformer, Busbar.'),
                html.Li('Performed Cable Sizing and Selection studies Considering thermal damage, Effective Ground-fault as per IEEE guideline'),
                html.Li('Performed Power System Analysis including Load Flow Analysis, Short Circuit Analysis, Harmonic Analysis,'
                        ' and Motor starting Analysis.'),
                html.Li('Prepared Preliminary I/O Schedule,Selected appropriate Field Instrumentation,Approved P&ID and Simulated PLC Programming '
                        ' Using Siemens TIA Portal.'),
                html.Li('Attended FAT in China For Equipment like Submersible Pump, Motor,Rotary kiln.'),
                html.Li('Fixed Design Criteria at FEED stage for Proper Construction Supervision as per Scope of work.'),
                html.Li('Reviewed SCADA & HMI Design , Network Architecture, and Topology  '
                        ' And also Specified Hardware requirements accordingly.'),
                html.Li('Provided solution using Software Simulation'' according to International Guidelines at FEED stage.'
                        ),
                html.Li('Particiapated in Installation Supervision of Electrical Equipment such as Switchgear, Flow Meter,'
                        ' Submersible Pump.'),
                html.Li('Lighting Design of the Plant Facility both indoor and outdoor using Revit Model inside '
                        'Dialux Evo Environment as per NFPA, BNBC, and NESC Guideline.'),
                html.Li('Troubleshooting and fault finding using Siemens TIA portal.'),
                html.Li('Reviewed Design and Installation case by preparing Switchgear Panel 3D Model.'),
                html.Li('Issued RFI, NCR as a part of regular supervision task and also prepared field report regarding '
                        'construction issues.')

            ])
        ])
    ])

])