# 53º Encontro do PUG-PE (14/06)

Local:  Accenture Armazém 12 

Horário:  14 de Junho de 2018 às 18:30 

## Palestras

### Introdução a Microsserviços com Python
#### Guilherme Caminha
O padrão arquitetural de Microsserviços é um estilo arquitetural que está crescendo em popularidade, dada sua flexibilidade e resiliência. Em conjunto com tecnologias como Kubernetes, está se tornando cada vez mais fácil criar aplicações utilizando arquiteturas baseadas em Microsserviços como nunca antes.
Nesta palestra vamos explorar a criação de microsserviços utilizando Python, e vamos construir uma aplicação prova de conceito para demonstrar a viabilidade desta estratégia. 

### Domando a irreversibilidade com Feature Flags
#### Hugo Rafael Bessa de Andrade
Feature Flags não são mais novidade: O time de desenvolvimento do Flickr já fala disso desde 2009. Mas muitos times não estão tirando benefício dessa incrível ferramenta para melhorar a maneira como eles constroem software.

Usar feature flags é sobre ter a possibilidade de ativar e desativar funcionalidades sem tocar no código. Isso pode ajudar o seu time de desenvolvimento, não só melhorar o tempo de resposta a desastres, como também aumenta a paz de espírito dos desenvolvedores. Além disso, é possível conseguir uma melhor 
sincronização do código (os desenvolvedores podem ter acesso a funcionalidades incompletas sem que isso prejudique o seu trabalho, já que a funcionalidade vai estar desligada) e um melhor fluxo de lançamento de novas funcionalidade, principalmente em aplicações com uma grande quantidade de usuários.

Junto com essas grandes vantagens, feature flags trazem algumas preocupações: existem várias estratégias de implementação e inúmeras nova coisas a se preocupar quando estiver lançando novas funcionalidades. Desde a escolha das melhores ferramentas para te ajudar a armazenar e recuperar suas flags à manutenção da consistência da aplicação com todas as combinações ligado/desligado de todas as flags.

Nessa talk, eu vou mostrar alguns dos benefícios e desafios que você vai encontrar ao usar feature flags, e como extrair o máximo de valor sem perder qualidade de código e a consitência da aplicação. 


### Deploy de Aplicações (Django e WSGI) em Ambiente Serverless (AWS Lambda)
#### Nielson Santana
O gerenciamento de servidores, escalabilidade, alta disponibilidade e tolerância a falhas, constitui um grande desafio para desenvolvedores/DevOps. Já imaginou não precisar mais se preocupar com estes problemas? Essa é a proposta das plataformas Serverless (AWS Lambda, Google Functions, Azure Functions, Apache OpenWhisk).  Outra vantagem é que só precisará pagar pelos recursos(CPU e GB RAM) que usar. Serverless é uma "nova" plataforma gerenciada para o deploy de aplicações baseadas em eventos no qual o usuário não precisa se preocupar com servidores. Nessa apresentação, irei falar sobre minha experiência no deploy de uma aplicação em django na plataforma Serverless da Amazon (AWS Lambda) e algumas boas práticas.
