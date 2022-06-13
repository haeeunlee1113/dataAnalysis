# dataAnalysis

archive python codes that made for analysing broad data from public data api.

* data source
\https://www.data.go.kr/



+ Libary
  * seaborn
  *  pandas
  *  matplotlib

+ Data sample(Countries-GDP-Data.csv) which is used on anlaysis has  formal problem.<br/>
  Every decimal points are written with ',' not '.'. <br/>
  So pandas considers their data format as string not float.<br/>
  I should convert them to normal float format.<br/>
  *cv_analysis.py has this part.*
