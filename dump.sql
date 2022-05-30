CREATE TABLE `recicla`.`venda` ( 
    `id` INT NULL AUTO_INCREMENT , 
    `comprador` VARCHAR(80) NULL , 
    `descricao` TEXT NOT NULL , 
    `preco_unitario` DECIMAL NULL , 
    `quantidade` INT NULL , 
    `endereco` TEXT NULL , 
    `fornecedor` VARCHAR(80) NULL , 
    PRIMARY KEY (`id`)
) ENGINE = InnoDB;

--
-- Estrutura para tabela `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nome` varchar(80) DEFAULT NULL,
  `email_do_usuario` varchar(80) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices de tabela `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;
COMMIT;