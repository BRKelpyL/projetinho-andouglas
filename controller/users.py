#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def incluir(nome, matricula, password):
    try:
        db.cur.execute("""
                    INSERT into streamservice.users (name, matricula, password)
                    VALUES ('%s','%s','%s')
                    """ % (nome, matricula, password))
        db.con.commit()
    except:
        db.con.rollback()
        return False

#função para inserir registro no banco de dados
def selecionar():
    query = "SELECT * FROM streamservice.users"
    db.cur.execute(query)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

def deletar(matricula):
    try:
        query = "DELETE FROM streamservice.users WHERE matricula = %s"
        db.cur.execute(query, (matricula,))
        db.con.commit()
    except:
        db.con.rollback()
        return False