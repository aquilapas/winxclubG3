--Código SQL para identificar fraudadores    
create view transaction_total as
    select * from (
        select * from transaction_in 
        union all 
        select * from transaction_out
    ) dum; 

create view transaction_final as
    select transaction_total.id, transaction_total.cliente_id, clients.nome, clients.telefone, transaction_total.valor, transaction_total.data
    from transaction_total
    inner join clients on clients.id = transaction_total.cliente_id; 

create view transaction_time as
    select transaction_final.id, transaction_final.cliente_id, transaction_final.nome, transaction_final.telefone, transaction_final.valor, transaction_final.data,
        datediff(second, lag(data) over (order by cliente_id), data) as time_difference
    from transaction_final; 

select count(id) as transactions__menorque_2min, cliente_id, nome, telefone
from transaction_time
where (time_difference < 120 and time_difference > 0)
group by cliente_id, nome, telefone
order by count(id) desc; 
