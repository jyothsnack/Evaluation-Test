# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import locale
from django.shortcuts import render
from analysis.models import StockName, StockPrices

locale.setlocale(locale.LC_ALL, '')

# Create your views here.
def stocks(request):
	'''Home Page'''
	stock_names = StockName.objects.all()
	print stock_names, 'stock_names'
	return render(request, 'stocks.html',{'stockNames':stock_names})

def stock_details(request, stock_name):
	'''view stock details'''
	stock_prices = []
	top_five = []
	stck_name = StockName.objects.filter(name=stock_name)[0]
	prev_close = None
	for stock in StockPrices.objects.filter(stock_id=stck_name).order_by('stock_date'):
		if prev_close:
			stock_percent = ((stock.stock_close - prev_close)/stock.stock_close) * 100
			stock_percent = "%.2f" % stock_percent
		else:
			stock_percent = ''
		stock_prices.append({'stock_date':stock.stock_date.date(),
							 'stock_open':stock.stock_open,
							 'stock_close':stock.stock_close,
							 'stock_percent':stock_percent})
		prev_close = stock.stock_close
	for top in StockPrices.objects.filter(stock_id=stck_name).order_by('-stock_volume')[:5]:
		top_five.append({'stock_date':top.stock_date.date(),
						 'stock_volume':locale.format('%d', top.stock_volume, 1)})

	return render(request, 'stockDetails.html', {'stockDetails':stock_prices,
												 'stockName':stock_name,
												 'topFive':top_five})



