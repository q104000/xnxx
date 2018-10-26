# -*- coding: utf-8 -*-
import requests,re,time
def main(url,name,shi):
	headers = {
	'Origin': 'https://www.xnxx.com',
	'Referer': url,
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
	res = requests.get(url)
	url_z = re.findall('html5player.setVideoHLS\(\'(.*?)\'\)',res.text)[0]#匹配总m3u8
	url_a = re.findall('(.*?)hls.m3u8',url_z)							  #提出前缀
	url_n = re.findall('\"\n(.*?)\n',requests.get(url_z,headers=headers).text) #匹配分m3u8
	ts_url = url_a[0]+url_n[hd(url_n)]
	res2 = requests.get(ts_url,headers=headers).text
	jindu = re.findall(',\n(.*?)\n',res2)
	jindu_over = int(re.search('p(\d*?)\.ts',jindu[-1]).group(1))
	for i in jindu:
		bai = int(re.search('p(\d*?)\.ts',i).group(1)) / jindu_over
		print (str(bai*100)[:4] + '%')
		res3 = requests.get(url_a[0]+i,headers=headers)
		with open (name,'ab') as ts:
			ts.write(res3.content)
		time.sleep(int(shi))
	input_name()
def hd(url_list):
	over = [int(re.search('-(\d*?)p',i).group(1)) for i in url_list]
	ret = sorted(over,reverse=True)
	return over.index(ret[0])
def input_name():
	print ('XNXX下载工具')
	rui = input('请输入视频网页url 文件名 时间:').split()
	main(rui[0],rui[1],rui[2])
if __name__ == '__main__':
	input_name()
# if __name__ == '__main__':
# 	main('https://www.xnxx.com/video-kjjuxc7/_..._rina_ishihara_adn-046','like.mp4')
# #https://www.xnxx.com/video-kjjuxc7/_..._rina_ishihara_adn-046
