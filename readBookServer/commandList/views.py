#coding:utf-8
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import StreamingHttpResponse
import time
import requests
import json

# Create your views here.
@csrf_exempt
def rankList(request):
	if request.method == 'GET':
		return JsonResponse({"code":300,"description":"Please use postMothed"})
	else:
		rankList = []
		rankList.append({
			'name':'原创风云榜·新书',
			'path':'/rank/yuepiao',
			})
		rankList.append({
			'name':'24小时热销榜',
			'path':'/rank/hotsales',
			})
		rankList.append({
			'name':'新锐会员周点击榜',
			'path':'/rank/newvipclick',
			})
		rankList.append({
			'name':'推荐票榜',
			'path':'/rank/recom',
			})
		rankList.append({
			'name':'收藏榜',
			'path':'/rank/collect',
			})
		rankList.append({
			'name':'完本榜',
			'path':'/rank/fin',
			})
		rankList.append({
			'name':'签约作家新书榜',
			'path':'/rank/signnewbook',
			})
		rankList.append({
			'name':'公众作家新书榜',
			'path':'/rank/pubnewbook',
			})
		typeList = []
		typeList.append({
			'name':'全部分类',
			'chn':'-1',
			})
		typeList.append({
			'name':'玄幻',
			'chn':'21',
			})
		typeList.append({
			'name':'奇幻',
			'chn':'1',
			})
		typeList.append({
			'name':'武侠',
			'chn':'2',
			})
		typeList.append({
			'name':'仙侠',
			'chn':'22',
			})
		typeList.append({
			'name':'都市',
			'chn':'4',
			})
		typeList.append({
			'name':'现实',
			'chn':'15',
			})
		typeList.append({
			'name':'军事',
			'chn':'6',
			})
		typeList.append({
			'name':'历史',
			'chn':'5',
			})
		typeList.append({
			'name':'游戏',
			'chn':'7',
			})
		typeList.append({
			'name':'体育',
			'chn':'8',
			})
		typeList.append({
			'name':'科幻',
			'chn':'9',
			})
		typeList.append({
			'name':'灵异',
			'chn':'10',
			})
		typeList.append({
			'name':'二次元',
			'chn':'12',
			})
		titleRegex = r'''<div class="book-mid-info">.*?<h4><a href="//book.qidian.com/info/[\s\S]*?>(.*?)</a>'''
		coverRegex = r'<a href="//book.qidian.com/info/.*?" target="_blank" data-eid="qd_C39" data-bid=".*?"><img src="//([\s\S]*?)"></a>';
		introRegex = r'<p class="intro">(.*?)</p>';
		lastRegex = r'<p class="update"><a href=".*?" target="_blank" data-eid="qd_C43" data-bid=".*?" data-cid=".*?">(.*?)</a><em>&#183;</em><span>.*?</span>';
		lastDateRegex = r'<p class="update"><a href=".*?" target="_blank" data-eid="qd_C43" data-bid=".*?" data-cid=".*?">.*?</a><em>&#183;</em><span>(.*?)</span>';
		authorRegex = r'<img src=".*?"><a class="name" href=".*?" target="_blank" data-eid="qd_C41">([\s\S]*?)</a><em>';
		typeRegex = r'<div class="book-mid-info">.*?data-eid="qd_C42">(.*?)</a><em>|</em><span>$';
		linkRegex = r'<div class="book-img-box">.*?<a href="//(.*?)" target="_blank" data-eid="qd_C39" data-bid=".*?"><img src="//.*?"></a>.*?</div>';

		regex = {
	    "titleRegex":titleRegex,
	    "coverRegex":coverRegex,
	    "introRegex":introRegex,
	    "lastRegex":lastRegex,
	    "lastDateRegex":lastDateRegex,
	    "authorRegex":authorRegex,
	    "typeRegex":typeRegex,
	    "linkRegex":linkRegex,
	    }
		return JsonResponse({'code':100,'rankList':rankList,'typeList':typeList,'doMain':"www.qidian.com","regex":regex})






