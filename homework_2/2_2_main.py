from pylatexhw import generate_latex_table_figure_wrapped

sample_rows = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

if __name__ == '__main__':
    latex_str = generate_latex_table_figure_wrapped(sample_rows, 'sample_img.jpg')

    with open('./artifacts/2_2.tex', 'w') as f:
        f.write(latex_str)
