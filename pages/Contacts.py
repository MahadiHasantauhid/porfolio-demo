import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=3)
green_text={'color':'green'}
layout = html.Div(
    dbc.Row([
        dbc.Col([
            dcc.Markdown('# MD MAHADI HASAN',className='mt-3',style={'text-align':'center', 'color': 'green'}),
            dcc.Markdown('### Electrical And Automation Engineer',className='mb-5'),
            dcc.Markdown('### Personal Info',style={'color': 'orange','text-align': 'center','background-color':'#33475b'}),
            dcc.Markdown('Address', style={'font-weight': 'bold'}),
            dcc.Markdown('Basundhara R/A, Dhaka-1229'),
            dcc.Markdown('Contact Number', style={'font-weight': 'bold'}),
            dcc.Markdown('+8801684573043 (Whatsapp,Viber)'),
            dcc.Markdown('Email Address', style={'font-weight': 'bold'}),
            dcc.Markdown('mahadihasan@hotmail.com'),
            dcc.Markdown('Linkedin', style={'font-weight': 'bold'}),
            dcc.Markdown('[www.linkedin.com/in/md-hasan-769a3425](linkedin.com/in/md-hasan-769a3425)',link_target='_blank'),
            dcc.Markdown('Youtube', style={'font-weight': 'bold'}),
            dcc.Markdown('[www.youtube.com/mahadihasan](https://www.youtube.com/channel/UCPkIivttGmrdQhslBcANOcA)',link_target='_blank'),
            dcc.Markdown('Professional Affiliation', style={'font-weight': 'bold'}),
            dcc.Markdown('IEEE Professional Member'),
            dcc.Markdown('IEEE Smart Grid Community Member')




        ],width={'size':6,'offset':2})



    ],justify='center'


    )

)