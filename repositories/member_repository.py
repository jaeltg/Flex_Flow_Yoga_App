from db.run_sql import run_sql

from models.member import Member

def save(member):
    sql = """
        INSERT INTO members (name, 
                             date_of_birth, 
                             memb_number,
                             memb_type, 
                             address, 
                             contact_number, 
                             active) 
            VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *
        """
    values = [member.name, 
              member.date_of_birth, 
              member.memb_number, 
              member.memb_type, 
              member.address, 
              member.contact_number,
              member.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member

    
def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row['name'], 
                        row['date_of_birth'],
                        row['memb_number'],
                        row['memb_type'], 
                        row['address'], 
                        row['contact_number'], 
                        row['active'],   
                        row['id'])
        members.append(member)
    return members
   


