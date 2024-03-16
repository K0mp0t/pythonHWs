from typing import List


def wrap_latex(latex: str) -> str:
    return f'\\documentclass{{article}}\n\\usepackage{{graphicx}}\\begin{{document}}\n{latex}\n\\end{{document}}'


def generate_latex_table_from_rows(rows: List[List[str]]) -> str:
    assert all(len(row) == len(rows[0]) for row in rows)

    rows_strs = ' \\\\\\hline\n'.join([' & '.join(row) for row in rows])

    return f'\\begin{{table}}\\begin{{tabular}}{{{"|".join(["c"] * len(rows[0]))}}}\n{rows_strs}\n\\end{{tabular}}\\end{{table}}\n'


def generate_latex_figure(fig_path: str) -> str:
    return f'\\begin{{figure}}\n\\includegraphics[scale=0.5]{{{fig_path}}}\n\\end{{figure}}\n'


def generate_latex_table_wrapped(rows: List[List[str]]) -> str:
    return wrap_latex(generate_latex_table_from_rows(rows))


def generate_latex_table_figure_wrapped(rows: List[List[str]], fig_path: str) -> str:
    return wrap_latex(generate_latex_table_from_rows(rows) + generate_latex_figure(fig_path))
