#!/usr/bin/python
# -*- coding: utf-8 -*-

# Code to Scrap out all the links from the website https://www.india.gov.in/topics/travel-tourism/approved-agents

#Code starts
import re
import scrapy
import xlrd 

class bot(scrapy.Spider):

    name = 'bot'
    allowed_domains = ["india.gov.in/topics/travel-tourism/approved-agents"]
    start_urls = ["https://www.india.gov.in/topics/travel-tourism/approved-agents"]
    
    def parse(self, response):
		links=response.css('h3 a::attr(href)').extract();dd=dict()
		for x in range(len(links)):
			dd[x]=links[x]
		
		yield dd
  
