class Mensaje:
    def __init__(self, remitente, destinatario, asunto, contenido):
        self._remitente = remitente
        self._destinatario = destinatario
        self._asunto = asunto
        self._contenido = contenido

    @property
    def remitente(self):
        return self._remitente

    @property
    def destinatario(self):
        return self._destinatario

    @property
    def asunto(self):
        return self._asunto

    @property
    def contenido(self):
        return self._contenido

    def __str__(self):
        return f"De: {self.remitente}, Para: {self.destinatario}, Asunto: {self.asunto}"


class Carpeta:
    def __init__(self, nombre):
        self._nombre = nombre
        self._mensajes = []

    @property
    def nombre(self):
        return self._nombre

    def agregar_mensaje(self, mensaje):
        self._mensajes.append(mensaje)

    def listar_mensajes(self):
        return self._mensajes


class Usuario:
    def __init__(self, nombre, email):
        self._nombre = nombre
        self._email = email
        self._carpetas = {"bandeja de entrada": Carpeta("bandeja de entrada"), "enviados": Carpeta("enviados")}

    @property
    def nombre(self):
        return self._nombre

    @property
    def email(self):
        return self._email

    def recibir_mensaje(self, mensaje):
        self._carpetas["bandeja de entrada"].agregar_mensaje(mensaje)

    def enviar_mensaje(self, servidor, destinatario_email, asunto, contenido):
        mensaje = Mensaje(self.email, destinatario_email, asunto, contenido)
        servidor.enviar_mensaje(mensaje)
        self._carpetas["enviados"].agregar_mensaje(mensaje)

    def listar_mensajes(self, carpeta_nombre="bandeja de entrada"):
        if carpeta_nombre in self._carpetas:
            return self._carpetas[carpeta_nombre].listar_mensajes()
        else:
            return []


class ServidorCorreo:
    def __init__(self):
        self._usuarios = {}

    def agregar_usuario(self, usuario):
        self._usuarios[usuario.email] = usuario

    def enviar_mensaje(self, mensaje):
        destinatario = self._usuarios.get(mensaje.destinatario)
        if destinatario:
            destinatario.recibir_mensaje(mensaje)
        else:
            print(f"Error: Usuario destinatario {mensaje.destinatario} no encontrado.")


# Ejemplo de uso
if __name__ == "__main__":
    servidor = ServidorCorreo()

    usuario1 = Usuario("Alice", "alice@example.com")
    usuario2 = Usuario("Bob", "bob@example.com")

    servidor.agregar_usuario(usuario1)
    servidor.agregar_usuario(usuario2)

    usuario1.enviar_mensaje(servidor, "bob@example.com", "Hola", "Hola Bob, ¿cómo estás?")
    mensajes_bob = usuario2.listar_mensajes()

    for msg in mensajes_bob:
        print(msg)
