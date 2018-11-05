#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psycopg2
class report(object):
	"""docstring for report"""
	def __init__(self):

		self.db = psycopg2.connect("dbname=news")
		self.cursor= self.db.cursor()
	
	def reportShow(self,title,query,style):
		
		self.cursor.execute(query)
		data=self.cursor.fetchall()
		result=[]
		#print the title
		print title
		for item in data:
			print (style.format(item[0],item[1]))
		print("\n")

def reportInfo():
	repo=report()

	title="What are the most popular three articles of all time?"
	query="select title,count(log.id) as num from articles join log on articles.slug= SUBSTRING(log.path, 10,LENGTH(log.path))\
	 group by title order by num desc limit 3"
	style='● {0} __ {1} log_count'
	repo.reportShow(title,query,style)


	#show most popular
	title="Who are the most popular article authors of all time?"
	query="""select
	 authors.name,num 
	 from 
	   authors 
	   join
	   (select author,count(log.id) as num from articles join log on articles.slug= SUBSTRING(log.path, 10,LENGTH(log.path))
	   group by author order by num desc limit 4) as popular_authors
	  on authors.id=popular_authors.author
	  order by num desc
	  limit 4"""
	repo.reportShow(title,query,style)

	#show which days did more than 1% of requests lead to errors
	title="On which days did more than 1% of requests lead to errors?"
	style='● {0:%b %d, %Y}__ {1}% errors'
	query="""
        select
            all_logs_date.date,
            ROUND(error_logs.log_count * 100.0 / all_logs_date.log_count, 2) AS pers
        from 
        (
            select DATE(time) AS date, COUNT(id) AS log_count
            from log
            where status LIKE '404%'
            group by date
        ) AS error_logs 

        join 
        (
            select DATE(time) AS date, COUNT(id) AS log_count
            from log
            group by date
        ) AS all_logs_date ON all_logs_date.date = error_logs.date

        where (error_logs.log_count * 100.0 / all_logs_date.log_count) > 1.00
        order by pers DESC
        limit 1
    """


	repo.reportShow(title,query,style)
	
reportInfo()






		
