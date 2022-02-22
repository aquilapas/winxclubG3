CREATE VIEW transaction_total
AS
    select * from (
        SELECT * FROM transaction_in 
        UNION ALL 
        SELECT * FROM transaction_out
            ) dum

select * from transaction_total
order by cliente_id, data;

CREATE VIEW transaction_final
as
    SELECT transaction_total.id, transaction_total.cliente_id, transaction_total.valor, transaction_total.data
    FROM transaction_total
    INNER JOIN clients ON clients.id = transaction_total.cliente_id


CREATE VIEW transaction_time
as
    select transaction_final.id, transaction_final.cliente_id, transaction_final.valor, transaction_final.data,
        datediff(second, lag(data) over (order by data), data) as time_difference
    from transaction_final

select * from transaction_time
where time_difference < 120
