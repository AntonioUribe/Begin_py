from persona import Persona
from conexion import Conexion
from logger_base import logger

class PersonaDao:
    '''
    DAO (DATE ACCES OBJECT)
    CRUD: CREATE-READ-UPDATE-DELETE entidad persona
    
    '''
    __SELECCIONAR = 'SELECT * FROM persona ORDER BY persona'
    __INSERTAR = 'INSERT INTO persona(nombre, apellido,email) VALUES(%s,%s,%s)'
    __ACTUALIZAR = 'UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona= %s'
    __ELIMINAR = 'DELETE FROM persona WHERE id_persona= %s'
    
    @classmethod
    def seleccionar(cls):
        cursor = Conexion.obtenerCursor()
        logger.debug(cursor.mogrify(cls.__SELECCIONAR))
        cursor.execute(cls.__SELECCIONAR)
        registros = cursor.fetchall()
        personas=[]
        for registro in registros:
            persona=Persona(registro[0],registro[1],registro[2],registro[3])
            personas.append(persona)
        Conexion.cerrar()
        return personas
    @classmethod
    def insertar(cls,persona):
        try:
            conexion=Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Persona a insertar: {persona}')
            valores = (persona.get_nombre(),persona.get_apellido(), persona.get_email())
            cursor.execute(cls.__INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            conexion.rollback()
            logger.error(f'Excepcion al insertar persona {e}')
        finally:
            Conexion.cerrar()
            
            
    @classmethod
    def actualizar(cls,persona):
        try:
            conexion=Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Persona a actualizar: {persona}')
            valores = (persona.get_nombre(),persona.get_apellido(), persona.get_email(), persona.get_id_persona())
            cursor.execute(cls.__ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            conexion.rollback()
            logger.error(f'Excepcion al insertar persona {e}')
        finally:
            Conexion.cerrar()
            
            
    @classmethod
    def eliminar(cls, persona):
        try:
            conexion=Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'Persona a eliminar: {persona}')
            valores = (persona.get_id_persona(),)
            cursor.execute(cls.__ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            conexion.rollback()
            logger.error(f'Excepcion al eliminar persona: {e}')
        finally:
            Conexion.cerrar()
    
    
    
if __name__=='__main__':
    #personas = PersonaDao.seleccionar()
    #for persona in personas:
    #   logger.debug(persona)
    #   logger.debug(persona.get_id_persona())
    
    #insertamos un nuevo registro
    #persona = Persona(nombre = 'Pedro', apellido = 'Najera', email = 'pnajera@mail.com') 
    #registros_insertados = PersonaDao.insertar(persona)
    
    #logger.debug(f'Personas insertados: {registros_insertados}')
    
    #Actualizar un registro
    #persona= Persona(24,'Antonio','Uribe','salazarantoniosa@gmail.com')
    #registros_actualizar = PersonaDao.actualizar(persona)
    #logger.debug(f'Personas actualizadas: {registros_actualizar}')
    
    #Eliminar
    persona2 = Persona(id_persona=16)
    personas_eliminadas = PersonaDao.eliminar(persona2)
    logger.debug(f'Personas eliminadas: {personas_eliminadas}')