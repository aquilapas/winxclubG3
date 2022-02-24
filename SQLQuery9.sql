--Código SQL para identificar fraudadores
create view transaction_total as
    select * from (
        select * from transaction_in 
        union all 
        select * from transaction_out
    ) dum; 

create view transaction_final as
    select transaction_total.id, transaction_total.cliente_id, clientes.nome, clientes.telefone, transaction_total.valor, transaction_total.data
    from transaction_total
    inner join clientes on clientes.id = transaction_total.cliente_id; 

create view transaction_time as
    select transaction_final.id, transaction_final.cliente_id, transaction_final.nome, transaction_final.telefone, transaction_final.valor, transaction_final.data,
        datediff(second, lag(data) over (order by cliente_id), data) as time_difference
    from transaction_final; 


select count(id) as transactions__menorque_2min, cliente_id, nome, telefone
into transactions_menor_que_2min
from transaction_time
where (time_difference < 120 and time_difference > 0)
group by cliente_id, nome, telefone
order by count(id) desc; 

select * from clientes;
select * from transaction_in;
select * from transaction_out;
select * from transactions_menor_que_2min;
select * from valores_movimentados;

select sum(abs(valor)) as valores_movimentados, tt.cliente_id 
into valores_movimentados from transaction_total tt join transactions_test teste 
on tt.id = teste.transactions__menorque_2min group by tt.cliente_id;

alter table transactions_menor_que_2min add valor float not null default 0;

update transactions_menor_que_2min 
set transactions_menor_que_2min.valor = valores_movimentados.valores_movimentados 
from transactions_menor_que_2min inner join valores_movimentados
on transactions_menor_que_2min.cliente_id = valores_movimentados.cliente_id;
