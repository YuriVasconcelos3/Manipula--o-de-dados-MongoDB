arquivo = open ("main.py", "r")
pagina = open("python.html", "w")
pagina.write("""
<html lang=\"pt-BR\">
<head>
<title> Eltrônics</title>
</head>
<body>
<p> 
""")
pagina.write(arquivo)