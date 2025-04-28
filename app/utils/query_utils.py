def insert_users(nome_usuario,idade,genero,email,senha,id_tipo_usuario):
    return """ insert into usuario(nomeUsuario,idade,genero,email,senha,idTipoUsuario) values ('{}',{},'{}','{}','{}',{}) """.format(nome_usuario,idade,genero,email,senha,id_tipo_usuario)

