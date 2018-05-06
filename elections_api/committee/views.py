import psycopg2
from django.shortcuts import render
from django.http import JsonResponse


def total_contributions(request):
    test = 16423
    with psycopg2.connect(host="127.0.0.1", 
                          user="postgres", 
                          password="postgres",
                          dbname="local_elections") as conn:
        c = conn.cursor()
        c.execute(
            """
            select sum(t.amount) from transactions t
            left join transaction_details td using(transaction_id)
            where t.committee_id = %(id)s and td.transaction_type = 'Contribution'
            group by t.committee_id;
            """, {"id": test}
        )
        if res:
            res = c.fetchall()[0][0]
            print(res)
            return JsonResponse({
                "msg": res,
            })
        # catch case where we don't have a result with a HTTP 404
    
