from sagemaker.serializers import CSVSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import Formatter, Validator
from rest_framework import status
from decouple import config
import sagemaker
import boto3

# Create your views here.

@api_view(['POST'])
def predictions(request):
    if request.method == 'POST':

        # pega a requisição do usuário
        data = request.data

        # instanciar a classe Formatter
        formatter = Formatter(data)
        
        # instanciar a classe Validator
        validator = Validator(data)

        # verifica a data de chegada
        if not validator.validate_data():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        # pegar as credenciais do arquivo dentro da pasta .env no arquivo .env
        config.search_path = './env'

        ACCESS_KEY_ID = config('ACCESS_KEY_ID')
        SECRET_ACCESS_KEY = config('SECRET_ACCESS_KEY')
        REGION_NAME = config('REGION_NAME')
        ENDPOINT = config('ENDPOINT')

        # criar uma sessão com o AWS Sagemaker
        boto_session = boto3.Session(aws_access_key_id = ACCESS_KEY_ID,
                             aws_secret_access_key = SECRET_ACCESS_KEY,
                             region_name = REGION_NAME)
        
        session = sagemaker.Session(boto_session = boto_session)
        
        endpoint = ENDPOINT
        previsor = sagemaker.predictor.Predictor(endpoint_name = endpoint, sagemaker_session = session)

        previsor.serializer = CSVSerializer() # definir o tipo de serialização dos dados de entrada

        X_exp = formatter.map_categorical_values() # mapear os valores categóricos
        previsao = previsor.predict(X_exp)
    
        previsao = previsao.decode('utf-8') # decodificar o resultado da previsão

        previsao = float(previsao) # converter o resultado da previsão para float
        previsao = int(previsao) # converter o resultado da previsão para int

        response = {'result': previsao + 1}

        # retorna o resultado da previsão e o status da requisição
        return Response(response, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND) # caso o método não seja POST
