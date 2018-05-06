import psycopg2
from django.shortcuts import render
from django.http import JsonResponse

def all_names(request):
    with psycopg2.connect(host="127.0.0.1",
                          user="postgres",
                          password="postgres",
                          dbname="local_elections") as conn:
        c = conn.cursor()
        c.execute(
            """
            select id, filer_name from committees_list
            """
        )
        res = c.fetchall()
        # res_clean = res[0][0]
        print(res)
        return JsonResponse({
            "msg": res
        })

def total_contributions(request, cid):
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
            """, {"id": cid}
        )
        res = c.fetchall()
        if res:
            res_clean = res[0][0]
            print(res_clean)
            return JsonResponse({
                "msg": res_clean,
            })

def total_expenditures(request, cid):
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
            where t.committee_id = %(id)s and td.transaction_type = 'Expenditure'
            group by t.committee_id;
            """, {"id": cid}
        )
        res = c.fetchall()
        if res:
            res_clean = res[0][0]
            print(res_clean)
            return JsonResponse({
                "msg": res_clean,
            })
        # catch case where we don't have a result with a HTTP 404

def contribution_count(request, cid):
    with psycopg2.connect(host="127.0.0.1",
                          user="postgres",
                          password="postgres",
                          dbname="local_elections") as conn:
        c = conn.cursor()
        c.execute(
            """
            select t.contributor_payee, sum(t.amount) from transactions t
            left join transaction_details td using(transaction_id)
            where t.committee_id = %(id)s and td.transaction_type = 'Contribution'
			group by contributor_payee
			order by sum(t.amount) desc limit 5
            """,{"id": cid}
        )
        res = c.fetchall()
        if res:
            res_clean = res[0][0]
            print(res_clean)
            return JsonResponse({
                "msg": res_clean,
            })
def spending_categories(request, cid):
    test = 16423
    with psycopg2.connect(host="127.0.0.1",
                          user="postgres",
                          password="postgres",
                          dbname="local_elections") as conn:
        c = conn.cursor()
        c.execute(
            """
            select td.purpose, sum(t.amount) from transactions t
            left join transaction_details td using(transaction_id)
            where t.committee_id = %(id)s and td.transaction_type = 'Expenditure'
			group by purpose
			order by sum(t.amount) desc
            """,{"id": cid}
        )
        res = c.fetchall()
        if res:
            res_clean = res[0][0]
            print(res_clean)
            return JsonResponse({
                "msg": res_clean,
            })
