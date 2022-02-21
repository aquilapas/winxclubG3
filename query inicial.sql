create database teste;

use teste;

create table Clients(
id int primary key not null, 
nome varchar(200),
email varchar(200),
data_cadastro datetime,
telefone varchar(50)
)

create table Transaction_In(
id int primary key not null, 
cliente_id int, 
valor float, 
data datetime
)

create table Transaction_Out(
id int primary key not null, 
cliente_id int, 
valor float, 
data datetime
)

/*drop table Clients;
drop table Transaction_In;
drop table Transaction_Out;*/

select * from Clients;
select * from Transaction_Out;

--ANALISANDO TABELA TRANSACTION_OUT
--seleciona somente clientes que tem transacoes out
select Clients.nome,Transaction_Out.cliente_id,Transaction_Out.valor, Transaction_Out.data 
from Transaction_Out
inner join Clients on Clients.id = Transaction_Out.cliente_id
order by Transaction_Out.cliente_id

--seleciona por id
select * from Transaction_Out
where cliente_id = 44 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 73--fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 74 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 153 --não fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 205 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 298 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 387 --não fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 389 --não fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 393 --não fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 442 --não fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 449 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 454 --não fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 495 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 522 --não fraudado 
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 523 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 529 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 530 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 533 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 534 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 570 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 586 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 643 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 651 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 660 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 671 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 680 --não fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 685 --não fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 689 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 690 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 671 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 694 --não fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 695 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 702 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 715 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 718 --não fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 719 --não fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 724 --não fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 727 --não fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 730 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 731 --não fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 732 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 737 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 741 --fraudado
order by data

--seleciona por id
select * from Transaction_Out
where cliente_id = 827 --fraudado
order by data

--ANALISANDO TABELA TRANSACTION_IN
--seleciona somente clientes que tem transacoes in
select Clients.nome,Transaction_In.cliente_id,Transaction_In.valor, Transaction_In.data 
from Transaction_In
inner join Clients on Clients.id = Transaction_In.cliente_id
order by Transaction_In.cliente_id

--seleciona por id
select * from Transaction_In
where cliente_id = 76 --fraudado
order by data

--seleciona por id
select * from Transaction_In
where cliente_id = 211 --não fraudado
order by data

--seleciona por id
select * from Transaction_In
where cliente_id = 335 --não fraudado
order by data

--seleciona por id
select * from Transaction_In
where cliente_id = 369 --não fraudado
order by data

--seleciona por id
select * from Transaction_In
where cliente_id = 387 --não fraudado
order by data

--seleciona por id
select * from Transaction_In
where cliente_id = 389 --não fraudado
order by data

--seleciona por id
select * from Transaction_In
where cliente_id = 449 --não fraudado
order by data

--seleciona por id
select * from Transaction_In
where cliente_id = 907 --fraudado
order by data
