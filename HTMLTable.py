

def newTable(data):
    data = data.splitlines()
    data = [d.strip() for d in data]
    data = [f"<tr><td>{d}</tr>" for d in data if d.strip() != ""]
    data = "<table border=1>" + "".join(data) + "</table>"
    data = data.replace(",", "</td><td>")
    with open("table.html", "w", encoding="utf-8") as file:
        file.write(data)

