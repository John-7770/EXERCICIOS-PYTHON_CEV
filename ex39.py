print("bem vindo ao alistamemto militar 2019".title())

anos = int(input("em que ano voce nasceu: ".title()))
anos = str(anos - 2019)
anos = anos.replace("-", " ")
anos = int(anos)

print("voce esta com {} anos ".title().format(anos))

if anos == 18:
    print("voce precisa se alistar no exercito brasileiro ".title() + "\033[0;31;mIMEDIATAMENTE")
elif anos < 18:
    print("daqui a {} ano voce tera aque se alistar no exercito brasileiro ".title().format(18-17))
elif anos > 18:
    print("voce nao precisa se alistar pois voce ja passou da  epoca".title())