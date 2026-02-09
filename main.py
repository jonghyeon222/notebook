from tkinter import *
from tkinter.filedialog import *      # 파일 열기/저장 대화상자를 별도로 가져온다

def new_file():                    # 텍스트창을 아무것도 안 쓰인 상태로
    text_area.delete(1.0, END)     # 텍스트창 1행 부터 끝(END)까지 다 지운다

def save_file():                   # 현재 쓰여진 내용을 파일로 저장하기
    f = asksaveasfile(mode="w", defaultextension=".txt",   # askaveasfile: 사용자가 저장 경로와 이름을 정할 수 있는 탐색기 창을 연다
                      filetypes=[('Text File', '.txt')])   # defaultextension: 확장자 생략 시 기본값
    text_save = str(text_area.get(1.0, END))   # 텍스트창 1행 부터 끝(END)까지 내용들을 문자열로 가져온다
    f.write(text_save)              # 추출한 문자열을 실제 파일에 쓴다.
    f.close()                       # 파일을 안전하게 닫는다.

def maker():                        # 누가 만들었는지 보여주는 창을 별도로 띄운다
    help_view = Toplevel(window)    # 별도의 메시지창 띄우기용
    help_view.geometry("300x50")
    help_view.title("만든이")
    lb = Label(help_view, text="신종현이 만든 메모장입니다.")
    lb.pack()


window = Tk()
window.title("Notebook")
window.geometry("400x400")
window.resizable(False, False)

menu = Menu(window)                    # 최상위 메뉴바

menu_1 = Menu(menu, tearoff=0)         # 하위 메뉴(tearoff=1: 메뉴 바가 본체에서 떨어져 나와 화면을 떠다님)
menu_1.add_command(label="새파일", command=new_file)
menu_1.add_command(label="저장", command=save_file)
menu_1.add_separator()
menu_1.add_command(label="종료", command=window.destroy)
menu.add_cascade(label="파일", menu=menu_1)

menu_2 = Menu(menu, tearoff=0)
menu_2.add_command(label="만든이", command=maker)
menu.add_cascade(label="만든이", menu=menu_2)

text_area = Text(window)                # 텍스트 입력창

window.grid_rowconfigure(0, weight=1)     # 첫번째 행과 첫번째 열에 가중치를 몰빵
window.grid_columnconfigure(0, weight=1)  # weight=1: 남는 공간이 생기면 0번 행과 0번 열이 전부 다 차지

text_area.grid(sticky = N+S+E+W)         # 텍스트 입력창으로 가득 채운다(.grid(): 위젯을 격자 판 위에 배치)

window.config(menu=menu)               # 생성한 메뉴를 창에다 추가한다
window.mainloop()
