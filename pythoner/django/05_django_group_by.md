# Django Group By
> https://stackoverflow.com/questions/629551/how-to-query-as-group-by-in-django  

```python
If you mean to do aggregation you can use the aggregation features of the ORM:

from django.db.models import Count
Members.objects.values('designation').annotate(dcount=Count('designation'))
This results in a query similar to

SELECT designation, COUNT(designation) AS dcount
FROM members GROUP BY designation
and the output would be of the form

[{'designation': 'Salesman', 'dcount': 2}, 
 {'designation': 'Manager', 'dcount': 2}]
```
