from django.db import models

# Create your models here.
# 데이터베이스에 직접 접근하는 것이 아니라 ORM 기능을 통해서 접근
# 모델은 class로 만든다.

class Bookmark(models.Model):
    # 필드 : 데이터베이스에 어떤 컬럼, 어떤 형태, 어떤 제약조건
    # 필드목적2 : 프론트에서 어떤 form tag와 어떤 제약조건을 설정
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    # print 함수를 사용해서 객체를 출력할 때 출력될 내용을 반환하는 함수
    # 장고가 이걸 응용해서 화면에 객체를 html로 출력할 때 내용을 반환하는 함수
    def __str__(self):
        return self.site_name+ " : "+self.url

    class Meta:
        # 해당 모델에 대한 옵션 값
        # 정렬, 출력될 모델 이름
        ordering = ['site_name']

    # Todo : get_absolute_url
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('bookmark:detail', args=[str(self.id)])
