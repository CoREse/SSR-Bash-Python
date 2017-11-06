# -*- coding:utf-8 -*-  
import json

f = file("/usr/local/shadowsocksr/mudb.json");

json = json.load(f);

print "用户名\t端口\t下载流量\t上传流量\t总已用流量\t流量限制"

for x in json:
  #Convert Unit To MB
  transfer_enable_int = int(x[u"transfer_enable"])/1024/1024;
  d_int = int(x[u"d"])/1024/1024;
  u_int = int(x[u"u"])/1024/1024;
  a_int = int(x[u"d"])+int(x[u"u"]);
  a_int = a_int/1024/1024;
  transfer_unit = "MB"
  d_unit = "MB"
  u_unit = "MB"
  a_unit = "MB"

  #Convert Unit To GB For Those Number Which Exceeds 1024MB
  if(transfer_enable_int > 1024):
  	transfer_enable_int = transfer_enable_int/1024
  	transfer_unit = "GB"
  if(d_int > 1024):
  	d_int = d_int/1024
  	d_unit = "GB"
  if(u_int > 1024):
  	u_int = u_int/1024
  	u_unit = "GB"
  if(a_int > 1024):
  	a_int = a_int/1024
  	a_unit = "GB"

  #Print In Format
  print "%s\t%s\t%d%s\t\t%d%s\t\t%d%s\t\t%d%s" %(x[u"user"],x[u"port"],d_int,d_unit,u_int,u_unit,a_int,a_unit,transfer_enable_int,transfer_unit)

f.close();

