<div align="center">
  <h1>Serviço de Inferência de Preços de Hotéis com Django, XGBoost e AWS </h1>
</div>

<div align="center">
  <p>Equipe 5</p>
</div>

***

<a name="ancora"></a>
## 📖 Sumário
- [1 - Objetivo](#ancora1)
  - [1.1 - Tecnologias Utilizadas](#ancora1-1)
- [2 - Desenvolvimento do Projeto](#ancora2)
  - [2.1 - Treinamento do Modelo](#ancora2-1)
  - [2.2 - Desenvolvimento do Serviço Django](#ancora2-2)
  - [2.3 - Deploy no Elastic Beanstalk](#ancora2-3)
- [3 - Acesso à Aplicação](#ancora3)
- [4 - Estrutura de Pastas do Projeto](#ancora4)
- [5 - Arquitetura AWS](#ancora5)
- [6 - Dificuldades conhecidas](#ancora6)
- [7 - Licença](#ancora7)

***

<a id="ancora1"></a>
# 1 - Objetivo

Este projeto tem como objetivo construir um serviço em Python utilizando o framework Django, que realiza inferências de preços de hotéis com base em informações contidas em um modelo XGBoost treinado no Amazon SageMaker. O serviço é implantado no AWS Elastic Beanstalk e oferece um endpoint para a realização de previsões de faixa de preços para reservas de hotéis.
***

<a id="ancora1-1"></a>
- ## 1.1 - Tecnologias Utilizadas

  <div style="display: inline-block" align="center">
    <img align="center" alt="Python" height="30" src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" />
    <img align="center" alt="Django" height="30" src="https://piptocode.github.io/_images/logo-django.png" />
    <img align="center" alt="Git" height="28" width="42" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg">
    <img align="center" alt="AWS-Js" height="28" width="42" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Amazon_Web_Services_Logo.svg/1024px-Amazon_Web_Services_Logo.svg.png" />
    <img align="center" alt="Sagemaker" height="28" width="42" src="https://d2q66yyjeovezo.cloudfront.net/icon/0c8d8b2a870bf0792528dc54c41799f1-eff89633572cc66bc69c8bed5885bc73.svg" />
    <img align="center" alt="EB" height="28" width="42" src="https://d2q66yyjeovezo.cloudfront.net/icon/d43b67a293d39d11b046bd1813c804cb-4bc0ce71c93950e1ad695b25a4f1d4b5.svg" />
    <img align="center" alt="S3" height="28" width="42" src="https://d2q66yyjeovezo.cloudfront.net/icon/c0828e0381730befd1f7a025057c74fb-43acc0496e64afba82dbc9ab774dc622.svg" />
  </div>

<a id="ancora2"></a>
# 2 - Desenvolvimento do Projeto

<a id="ancora2-1"></a>
- ## 2.1 - Treinamento do Modelo
  O modelo foi construido através do Amazon SageMaker com a utilização do algoritmo XGBoost, treinado com base no [dataset Hotel Reservations](https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset) e seguindo as seguintes etapas:

  1. Tratamento da base de dados;
  2. Configurações do SageMaker;
  3. Tuning;
  4. Construção do modelo;
  5. Testes e Deploy.

  O algoritmo XGBoost foi escolhido devido ao seu alto índice de assertividade com problemas de classificação em relação aos outros algoritmos aprendidos durante os estudos da sprint 5. 
  Ao realizar o teste com o modelo construído obtivemos os seguintes resultados:
   
   <div align="center">
    <p>Figura 1 - Informações do Modelo</p>
    <img src = "https://user-images.githubusercontent.com/47997616/261663787-864db099-9496-426e-a476-bcc59d4b1d49.png">
  </div>

<a id="ancora2-2"></a>
- ## 2.2 Desenvolvimento do Serviço Django
  Foi desenvolvido um serviço em Python utilizando o framework Django. O serviço é responsável por receber e tratar as informações recebidas em um endpoint POST em "/api/v1/predict" e consultar o modelo treinado no SageMaker para a realização de previsões. O JSON fornecido na requisição contém informações relevantes sobre a reserva.
  Exemplo de JSON no corpo da requisição:

  ```
  {
      "no_of_adults": 3,
      "no_of_children": 3,
      "type_of_meal_plan": "example"
      ...
  }
  ```
  A resposta segue o formato:

  ```
  {
    "result": 1
  }
  ```

  O projeto utiliza variáveis de ambiente para configurar as variáveis responsáveis por realizarem o acesso ao modelo de previsões. Assim permitindo uma maior flexibilidade e possibilidades de configurações desses valores de acordo com diferentes ambientes (desenvolvimento, teste, produção) sem a necessidade de alterar o código-fonte, além de ser uma imporetante prática de segurança.

<a id="ancora2-3"></a>
- ## 2.3 Deploy no Elastic Beanstalk
  Um ambiente Docker foi configurado para o AWS Elastic Beanstalk, garantindo a portabilidade do serviço.

<a id="ancora3"></a>
# 3 - Acesso à Aplicação 

### **[Link](http://equipe05-sprint05.us-east-1.elasticbeanstalk.com/api/v1/predictions/)**



<a id="ancora4"></a>
# 4 - Estrutura de Pastas do Projeto
- **hotelReservation**

  - **hotelReservation**
    - `asgi.py`
    - `settings.py`
    - `urls.py`
    - `wsgi.py`
  - **predictions**
    - `.env`
    - `admin.py`
    - `apps.py`
    - `middleware.py`
    - `models.py`
    - `tests.py`
    - `utils.py`
    - `views.py`

  - `db.sqlite3`
  - `Dockerfile`
  - `Dockerrun.aws.json`
  - `rquirements.txt`


***

<a id="ancora5"></a>
# 5 - Arquitetura AWS

<div align="center">
  <p>Figura 2 - Arquitetura do Projeto na AWS</p>
  <img src = "https://github.com/Sais01/MicrosoftLearn/assets/47997616/54092b63-4078-4b45-942b-5bae91fd2225">
</div>

***

<a id="ancora6"></a>
# 6 - Dificuldades conhecidas

Não houve dificuldades significantes no desenvolvimento desta atividade.


<a id="ancora7"></a>
# 7 - Licença

Este projeto está licenciado sob a Licença MIT - consulte o [Link](https://mit-license.org/) para obter mais detalhes.
