# Django Model Q 或
> https://docs.djangoproject.com/en/2.0/topics/db/queries/  

```
https://stackoverflow.com/questions/6567831/how-to-perform-or-condition-in-django-queryset

from django.db.models import Q
User.objects.filter(Q(income__gte=5000) | Q(income__isnull=True))
```

```
http://simeonfranklin.com/blog/2011/jun/14/best-way-or-list-django-orm-q-objects/

A co-worker asked me today about the best way to OR together a list of Q objects in the Django ORM. Usually you have a specific number of conditions and you can use Q objects and the bitwise OR operator to logical OR the query conditions together. The Q object is necessary because multiple arguments or successive calls to .filter are ANDed. But what if you have an arbitrary number of Q conditions?

One suggestion is to use the undocumented .add method of the Q object in a loop to add multiple query conditions together. I thought this might be a good use case for reduce and the operator module:



# Normal Usage with the | operator
from django.db.models import Q
qs = MyModel.objects.filter(Q(cond1=1) | Q(cond2="Y"))

#but given a list of Q conditions
from operator import __or__ as OR
lst = [Q(...), Q(...), Q(...)]
qs = MyModel.objects.filter(reduce(OR, lst))
Is this the most Pythonic approach?
```

```
https://micropyramid.com/blog/querying-with-django-q-objects/

Dynamic querying with Q objects:
    This is an interesting feature as we can use the operator module to create dynamic queries. 

    import operator
    from django.db.models import Q
    from your_app.models import your_model_object

    q_list = [Q(question__startswith='Who'), Q(question__startswith='What')]
    your_model_object.objects.filter(reduce(operator.or_, q_list))
    We are performing the or operation using operator.or_

    To use and operations simply execute:

    your_model_object.objects.filter(reduce(operator.and_, q_list))
    Q objects not only simplify complex queries, they are very handy for dynamic filtering.

    To Know more about our Django CRM(Customer Relationship Management) Open Source Package. Check Code
```
