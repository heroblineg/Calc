import tkinter as tk

# ボタンがクリックされたときの処理
def button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# メインウィンドウの作成
root = tk.Tk()
root.title("YKalc")

# アイコンを設定 (yk.pngファイルがリポジトリのルートディレクトリにあることを確認)
icon = tk.PhotoImage(file="yk.png")
root.iconphoto(True, icon)

# グリッドの行と列のサイズ変更を設定
root.rowconfigure(0, weight=1)
for i in range(1, 5):
    root.rowconfigure(i, weight=1)
    root.columnconfigure(i-1, weight=1)

# エントリーウィジェット（表示部分）の作成
entry = tk.Entry(root, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# ボタンのラベルリスト
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# ボタンの作成と配置
row_val = 1
col_val = 0
for button in buttons:
    b = tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18))
    b.grid(row=row_val, column=col_val, sticky="nsew")
    b.bind("<Button-1>", button_click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# メインループの開始
root.mainloop()