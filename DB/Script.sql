create table tipo_usuario(
idTipoUsuario SERIAL primary key,
descricaoTipoUsuario varchar(255)
);

create table usuario(
idUsuario SERIAL primary key,
nomeUsuario varchar(255),
idade int,
genero varchar(50),
email varchar(255),
senha varchar(30),
idTipoUsuario bigint,
constraint fk_tipousuario foreign key (idTipoUsuario) references tipo_usuario(idTipoUsuario)
);

CREATE TABLE servico
(idServico SERIAL PRIMARY KEY,
descricaoServico varchar (50),
precoServico numeric (15,2),
tempoServico time
);

CREATE TABLE agendamento(
idAgendamento SERIAL PRIMARY KEY ,
idCliente bigint,
idFuncionario bigint,
datahora timestamp,
idservico bigint,
statusagendamento varchar(50),
constraint fk_servico foreign key (idservico) references servico(idServico),
constraint fk_Funcionario foreign key (idFuncionario) references usuario(idUsuario),
constraint fk_Cliente foreign key (idCliente) references usuario(idUsuario)
);



