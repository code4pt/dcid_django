INSERT INTO `parliament_person`(`id_num`, `name`, `email`) VALUES (1111,"alice wonderland","alice@wonderland.com");
INSERT INTO `parliament_person` VALUES (2222,"bob builder","bob@builder.com");
INSERT INTO `parliament_person` VALUES (3333,"clair de lune boudair","clair@boudair.com");
INSERT INTO `parliament_person` VALUES (4444,"dionisus draconius","dionisus@draconius.com");
INSERT INTO `parliament_person` VALUES (5555,"someone anonymous","someone@anonymous.com");

INSERT INTO `parliament_tag`(`name`, `desc`) VALUES ("cm-cascais", "sem descrição");
INSERT INTO `parliament_tag` VALUES ("cm-lisboa", "sem descrição");
INSERT INTO `parliament_tag` VALUES ("cm-oeiras", "sem descrição");
INSERT INTO `parliament_tag` VALUES ("cm-porto", "sem descrição");
INSERT INTO `parliament_tag` VALUES ("parque", "sem descrição");
INSERT INTO `parliament_tag` VALUES ("reparação", "sem descrição");
INSERT INTO `parliament_tag` VALUES ("nova-construção", "sem descrição");
INSERT INTO `parliament_tag` VALUES ("iniciativa", "sem descrição");

INSERT INTO `parliament_proposal`(`id_num`, `author_id`, `title`, `problem`, `solution`, `benefits`, `upvotes`, `downvotes`, `views`, `timestamp`) VALUES (1,2222,"Adoptar o 'dcid' em todas as Câmaras Municipais","Várias câmaras municipais já começaram a implementar Orçamentos Participativos. Infelizmente, cada câmara gasta tempo e dinheiro público a desenvolver o seu próprio site de votação online (reinventando a roda).", "Proponho que todas as Câmaras Municipais com OPs usem o 'dcid' como plataforma de suporte.","Poupa-se dinheiro público; Criam-se sinergias pois todas as CMs trabalham para mnelhorar a mesma plataforma; Os cidadãos habituam-se a utilizar uma só plataforma; Incentiva-se a participação democrática dos munícipes e cidadãos em geral.",968,17,8624,"2013-03-10 14:13:12");
INSERT INTO `parliament_proposal` VALUES (2,1111,"Terminar o parque da Quinta de Rana","A requalificação do parque começou mas não chegou a ser terminada. A parte mais interessante da nora e aqueduto está vedada, há alguns anos.","Requalificar essa zona, de certeza que a Câmara já tem o plano é só implementá-lo.","O Parque deixa de ter aspecto de obras; Os cidadãos podem usar o parque para evitarem a estrada da Rebelva (que não tem passeios).",50,1,10,"2012-09-04 14:14:12");
INSERT INTO `parliament_proposal` VALUES (3,1111,"Diminuir tráfego na Rotunda do Marquês","O trânsito é caótico a quase toda a hora. Os peões têm muita dificuldade em atravessar a estrada, além de que cheira muito a combustível.","Plantavam-se trepadeiras!","Mais agradável para os peões.",523,496,500,"2012-09-04 14:15:12");
INSERT INTO `parliament_proposal` VALUES (4,4444,"A ponte Dona Maria devia ser um jardim","É ferro a mais.","Plantavam-se trepadeiras!","Era inovador e bonito",1,624,200,"2012-09-04 14:16:12");

INSERT INTO `parliament_tag_tagged_proposals`(`tag_id`, `proposal_id`) VALUES ("iniciativa", 1);
INSERT INTO `parliament_tag_tagged_proposals` VALUES ("cm-cascais", 2);
INSERT INTO `parliament_tag_tagged_proposals` VALUES ("parque", 2);
INSERT INTO `parliament_tag_tagged_proposals` VALUES ("cm-lisboa", 3);
INSERT INTO `parliament_tag_tagged_proposals` VALUES ("nova-construção", 3);
INSERT INTO `parliament_tag_tagged_proposals` VALUES ("cm-porto", 4);
INSERT INTO `parliament_tag_tagged_proposals` VALUES ("iniciativa", 4);
INSERT INTO `parliament_tag_tagged_proposals` VALUES ("nova-construção", 4);
