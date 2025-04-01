# app 에서 사용할 form 을 모은 모듈.

# form 의 역할: 1. form 을 쉽게 그릴 수 있게 도와줌. 2. 유효성 검사를 할 수 있게 해 줌.
# 우리가 사용자로부터 받아야 하는 데이터는 model 이다. 즉, model 과 똑같이 생긴(data 형식이 똑같은) form 이 있으면 된다.
# form 을 만들건데, model 을 참조해서 만들어야 되겠다 => ModelForm.

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # Meta class 에 Article model 정의.
    class Meta:
        model = Article  # Meta 야, 내가 쓰는 model 은 Article 이야....
        fields = '__all__'  # Form 에서 사용자에게 입력받을 필드를 정의. 
        # fields = ['title', 'content']  # 원래 이렇게 해 주는 게 안전하고 좋은데, 일단은 다 받기.
