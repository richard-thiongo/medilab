from db import Database
import functions

# Here we do the CRUD operations for the laboratories table

class LabService:
    def __init__(self):
        self.db = Database()

    def createLab(self, lab_name, permit_id, email, phone, password ):
        query = "INSERT INTO laboratories (lab_name, permit_id, email, phone , password) VALUES (%s, %s, %s, %s, %s)"

        try:
            cursor = self.db.get_cursor()
            data = (lab_name, permit_id, email, phone, password)
            cursor.execute(query, data)
            self.db.commit()
            return True
        except Exception as e:
            # print(e)
            return False
        finally:
            self.db.close()


    def labLogin(self, email, password):
        query = "SELECT * FROM laboratories WHERE email = %s"
        try:
            cursor = self.db.get_cursor()
            data = (email)
            cursor.execute(query, data)
            if cursor.rowcount == 0:
                return False
            else:
                result = cursor.fetchone()
                if functions.hash_verify(password, result["password"]):
                    return result
                else:
                    return False
        except Exception as e:
            # print(e)
            return False
        finally:
            self.db.close()


    def labProfile(self, lab_id):
        query = "SELECT * FROM laboratories WHERE lab_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (lab_id)
            cursor.execute(query, data)
            if cursor.rowcount == 0:
                return False
            else:
                lab = cursor.fetchone()
                return lab
        except Exception as e:
            # print(e)
            return False
        finally:
            self.db.close()
            

    def updateLab(self, lab_id, lab_name, permit_id, email, phone, password):
        query = "UPDATE laboratories SET lab_name = %s, permit_id = %s, email = %s, phone = %s, password = %s WHERE lab_id = %s"
        try:
            cursor = self.db.get_cursor()
            data = (lab_name, permit_id, email, phone, password, lab_id)
            cursor.execute(query, data)
            self.db.commit()
            if cursor.rowcount == 0:
                return False
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.db.close()
            
        