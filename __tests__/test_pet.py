# 1 - Bibliotecas
import json
import pytest
import requests

# 2 - Classe opcional no python
 
# 2.1 - atributos e variaveis
pet_id = 173218101   #codigo do animal
pet_name = "zoze"    # nome do animal
pet_category_id = 1  #Codigo da categoria do animal
pet_category_name = "dog"  #titulo da cateroria
pet_tag_id = 1   #codigo do rotulo
pet_tag_name = "vacinado"   # titulo do rotulo
pet_status = "available"  #status do animal
url = 'https://petstore.swagger.io/v2/pet' 
headers = { 'Content-Type': 'application/json' }



# 2.2 - funções e metodos

def test_post_pet():
  #configura
  pet=open('./fixtures/json/pet1.json')   #abrir o arquivo
  data=json.loads(pet.read())
    
  #executa
  response = requests.post(
      url=url,
      headers=headers,
      data=json.dumps(data),
      timeout=5
  )

  #valida
  response_body = response.json()
  assert response.status_code == 200
  assert response_body['id'] == pet_id
  assert response_body['name'] == pet_name
  assert response_body['category']['name'] == pet_category_name
  assert response_body['tags'][0]['name'] == pet_tag_name


