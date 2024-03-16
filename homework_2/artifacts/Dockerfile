FROM python:3.8

RUN apt-get update && apt-get install texlive-latex-recommended -y
RUN pip install -i https://test.pypi.org/simple/ pylatexhw
RUN mkdir /pylatexhw

COPY sample_img.jpg /pylatexhw
COPY 2_2_main.py /pylatexhw

WORKDIR /pylatexhw

RUN python3 2_2_main.py
RUN pdflatex artifacts/2_2.tex
