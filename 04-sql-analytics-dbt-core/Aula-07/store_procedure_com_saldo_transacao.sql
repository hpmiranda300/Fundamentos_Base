--proc_realizar_transacao(tipo, descricao, valor, cliente_id) 
--                       ('d', 'Compra de carro', 80000, 1)
CREATE
OR REPLACE PROCEDURE proc_realizar_transacao (
	IN p_tipo CHAR(1),
	IN p_descricao VARCHAR(10),
	IN p_valor INTEGER,
	IN p_cliente_id INTEGER
) LANGUAGE plpgsql AS $$
DECLARE
    saldo_atual INTEGER;
    limite_cliente INTEGER;
	saldo_apos_transacao INTEGER;
BEGIN
	-- Corpo da procedure...
	-- Obtém o saldo atual e o limite do cliente	
	SELECT saldo, limite INTO saldo_atual, limite_cliente
	FROM clients
	WHERE id = p_cliente_id;
	
	RAISE NOTICE 'Saldo atual do cliente: %', saldo_atual;
	RAISE NOTICE 'Limite atual do cliente: %', limite_cliente;	
	
	-- Verifica se a transação é válida com base no saldo e no limite
	IF p_tipo = 'd' AND saldo_atual - p_valor < - limite_cliente THEN
		RAISE EXCEPTION 'Limite inferior ao necessario para realizar a transação.';
		RAISE EXCEPTION 'Dados da transação. Tipo: %, Descrição: %, Valor: %', p_tipo, p_descricao, p_valor;
	END IF;
	
	-- Atualiza o saldo do cliente
	--Nesta parte, o saldo do cliente é atualizado com base no tipo de transação.
	--Se for um débito ('d'), o valor é subtraído do saldo atual; caso contrário, é adicionado.
	UPDATE clients
	SET saldo = saldo + CASE WHEN p_tipo = 'd' THEN -p_valor ELSE p_valor END
	WHERE id = p_cliente_id;

    -- Insere uma nova transação
	--Por fim, uma nova transação é inserida na tabela transactions com os detalhes fornecidos.
	INSERT INTO transactions (tipo, descricao, valor, cliente_id)
	VALUES (p_tipo, p_descricao, p_valor, p_cliente_id);	
	
	SELECT saldo INTO saldo_apos_transacao
	FROM clients
	WHERE id = p_cliente_id;
	
	RAISE NOTICE 'Saldo cliente apos transacao: %', saldo_apos_transacao;
END;
$$;

--CALL proc_realizar_transacao('d', 'carro', 80000, 1);
--CALL proc_realizar_transacao('c', 'bonus', 70000, 1);
--CALL proc_realizar_transacao('d', 'carro', 80000, 1);
--CALL proc_realizar_transacao('c', 'bonus', 15000, 1);
--SELECT * FROM clients
--select * from transactions