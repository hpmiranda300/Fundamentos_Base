-- Conferir se gravou
SELECT * FROM clients WHERE id = 1;
SELECT * FROM transactions WHERE cliente_id = 1;
-- Ver extrato
CALL proc_ver_extrato(1);