#  -*- coding: UTF-8 -*
import pandas as pd

class LatexUtils():
    def __init__(self):
        pass

    # pandasのDataFrameを入力とし，表を出力する
    def create_table(self, df, caption="Title", position="p", label=None, align="center", lcr="c", tl=""):
        s = "\\begin{{table}}[{}]\n".format(position)           # ページ全体における表の位置の指定
        s += " \\caption{{{}}}\n".format(caption)               # 注釈(タイトル)の追加
        if label != None: s += "  \\label{}\n".format(label)    # ラベルの付与
        s += "  \\begin{{{}}}\n".format(align)                  # positionで指定された場所内での表の位置を指定
        s += "\t\\begin{{tabular}}{{{}}}\n".format(lcr*len(df)) # left/center/rightでセル内の要素の位置を指定
        s += "\t\t{}\t&\t".format(tl)                           # 左上に何か加えるならtlに
        s += "\t&\t".join(df.columns)                           # カラム名を追加
        s += " \\\\\n"
        for i in range(len(df)):                                # 表の要素の追加
            s += "\t\t{}\t&\t".format(df.index[i])
            s += "\t&\t".join(map(str, df.iloc[i]))
            s += " \\\\\n"
        s += "\t\\end{tabular}\n"
        s += "  \\end{center}\n"
        s += "\\end{table}"
        return s

if __name__ == "__main__":
    df = pd.DataFrame([["day1","day2","day1","day2","day1","day2"],
              ["A","B","A","B","C","C"],
              [100,150,200,150,100,50],
              [120,160,100,180,110,80]] ).T
    df.columns = ["day_no","class","score1","score2"]
    lu = LatexUtils()
    s = lu.create_table(df)
    print(s)
