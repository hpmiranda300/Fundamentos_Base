CREATE OR REPLACE PROCEDURE proc_ver_extrato (IN p_id_cliente INTEGER) LANGUAGE plpgsql AS $$
DECLARE
    saldo_atual INTEGER;
    transacao RECORD;
    contador INTEGER := 0;  
BEGIN    
	--Obtenção do Saldo Atual
	-- Se o cliente não existir, gera erro automaticamente (NO_DATA_FOUND)
    -- Se houver mais de um registro, também gera erro (TOO_MANY_ROWS)
    SELECT saldo INTO STRICT saldo_atual
    FROM clients
    WHERE id = p_id_cliente;

	IF NOT FOUND THEN
    	RAISE EXCEPTION 'Cliente com ID % não foi encontrado.', p_id_cliente;
	END IF;
	
	--Exibição do Saldo Atual   
    RAISE NOTICE 'Saldo atual do cliente: %', saldo_atual;
	
	--Obtenção das Últimas 10 Transações	
    RAISE NOTICE 'Últimas 10 transações do cliente:';
	
	FOR transacao IN
        SELECT *
        FROM transactions
        WHERE cliente_id = p_id_cliente
        ORDER BY realizada_em DESC, id DESC
        LIMIT 10
    LOOP
        contador := contador + 1;
        RAISE NOTICE 'ID: %, Tipo: %, Descrição: %, Valor: %, Data: %', transacao.id, transacao.tipo, transacao.descricao, transacao.valor, transacao.realizada_em;
        EXIT WHEN contador >= 10;
    END LOOP;
END;
$$;

--CALL proc_ver_extrato (1)