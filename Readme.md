O projeto se chama Core e é um projeto para gerenciamento de clientes e seus carros. A motivação por trás de um sistema de gestão de clientes e seus carros está na busca pela eficiência e na melhoria da experiência do cliente. O sistema visa simplificar o acompanhamento de algumas informações referentes aos clientes e seus bens automotivos, visando garantir a segurança e confiabilidade desses veículos, resultando em clientes mais satisfeitos e fidelizados. Ao mesmo tempo, otimiza a gestão de recursos e aumenta a eficiência operacional.

Primeiro foi definida a rota, que mapeia para o ViewSet. A View busca o cliente no banco de dados e, em seguida, é utilizado o models para definir o queryset. Depois, o serializer é utilizado quando se deseja retornar models como uma resposta para o cliente que está fazendo a solicitação.

Foi definida a classe Cliente, que representa as informações de cada cliente através dos atributos: nome, idade e endereço.

Depois foi definida a classe Carro, que captura as informações de cada carro, através dos atributos: dono, apelido, ano, modelo, placa e cor.

Posteriormente, foi adicionado um atributo ForeignKey para estabelecer o relacionamento entre as classes, pois cada cliente pode ter mais de um carro.