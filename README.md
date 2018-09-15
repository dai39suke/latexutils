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

Options:
- `caption`: \\caption contents
- `position`: table position on the whole page
- `label`: \\label contents
- `align`: table position in the assigned region by `position`
- `lcr`: elements position left/center/right
- `tl`: upper left cell
- `digit`: round to the specified number of decimal places 

### Example
---
- default version
```
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
df.columns = ["A", "B", "C"]
df.index = ["First", "Second", "Third"]
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
		First	&	1	&	2	&	3 \\
		Second	&	4	&	5	&	6 \\
		Third	&	7	&	8	&	9 \\
	\end{tabular}
  \end{center}
\end{table}
```
- option added version
```
df = pd.DataFrame([
    [1.111, 2.222, 3.333],
    [4.444, 5.555, 6.666],
    [7.777, 8.888, 9.999]])
df.columns = ["A", "B", "C"]
df.index = ["First", "Second", "Third"]
lu = LatexUtils()
s = lu.create_table(df, caption="Sample", position="h", label="tb:sample", align="left", lcr="l", tl="Times", digit=2)
s
```
``` output
\begin{table}[h]
 \caption{Sample}
  \labeltb:sample
  \begin{left}
	\begin{tabular}{lll}
		Times	&	A	&	B	&	C \\
		First	&	1.11	&	2.22	&	3.33 \\
		Second	&	4.44	&	5.56	&	6.67 \\
		Third	&	7.78	&	8.89	&	10.0 \\
	\end{tabular}
  \end{center}
\end{table}
```
