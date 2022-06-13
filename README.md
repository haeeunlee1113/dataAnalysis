# dataAnalysis

archive python codes that made for analysing broad data from public data api.

* data source
\https://www.data.go.kr/


* Data sample(Countries-GDP-Data.csv) which is used on anlaysis has some formal problem.
** First, Every decimal points are written with ',' not '.'. So pandas considers their data format as string not float.
** So I should convert them to normal float format.
** cv_analysis.py has this part.

* Libary
- seaborn
- pandas
- matplotlib
