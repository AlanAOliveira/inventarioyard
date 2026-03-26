import gradio as gr
import pandas as pd
import datetime

data = pd.DataFrame({'x': [x for x in range(30)],
                     'y': [2 ** x for x in range(30)]})

# Current date and time header
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Display the data with Gradio
with gr.Blocks(css='footer {visibility: hidden}') as gradio_app:
    with gr.Row():
        with gr.Column(scale=3):
            gr.Markdown(f'# Inventario YARD!\n\n**{now}**')
            gr.ScatterPlot(value=data, height=400, width=700,
                           container=False, x='x', y='y',
                           y_title='Fun with data', x_title='Apps')

if __name__ == '__main__':
    gradio_app.launch()
