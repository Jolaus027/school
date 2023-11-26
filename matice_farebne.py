from matice import matica1, pocet_matic
import tkinter

pocet_stvorcov = pocet_matic



canvas = tkinter.Canvas(width=1920,height=1080)
canvas.pack()


for i in range(1,pocet_matic+1):

    canvas.create_line(0, 500/pocet_matic*i,500, 500/pocet_matic*i)
    canvas.create_line(500/pocet_matic*i, 0, 500/pocet_matic*i, 500)


for p in range(pocet_matic):

    for g in range(pocet_matic):

        

        

        if g == 0 and p == 0:

            canvas.create_text(240//pocet_matic, 300//pocet_matic, text={(str(matica1[p][g])).replace("{", "").replace("}", "").replace("'", "")}, font=("Helvetica", 300//pocet_matic), fill="blue")

        else:

            canvas.create_text((g*505+240)//pocet_matic, (p*505+300)//pocet_matic, text={(str(matica1[p][g])).replace("{", "").replace("}", "").replace("'", "")}, font=("Helvetica", 300//pocet_matic), fill="blue")


tkinter.mainloop()