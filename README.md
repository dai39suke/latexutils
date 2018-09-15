## latexutils

### Install
---
```
pip install latexutils
```

### Usage
---
Input: DataFrame(pandas object), options ...
Output: Raw text for making table at latex

### Example
---
```
lu = LatexUtils()
s = lu.create_table(df)
s
```
``` output
\begin{table}[p]
 \caption{Title}
  \begin{center}
	\begin{tabular}{ccc}
			&	A	&	B	&	C \\
		0	&	1	&	2	&	3 \\
		1	&	4	&	5	&	6 \\
		2	&	7	&	8	&	9 \\
	\end{tabular}
  \end{center}
\end{table}
```
