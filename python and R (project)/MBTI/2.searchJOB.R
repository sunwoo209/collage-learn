#install.packages("xlsx")
#install.packages("XLConnect")
Sys.setenv(JAVA_HOME='C:\\Program Files\\Java\\jre1.8.0_251')
library(rJava)
library(XLConnect)
library(xlsx)
library(XML)
library(RCurl)
library(ggmap)
library(ggplot2)


register_google(key="AIzaSyASrdCrbTwgCxRs9IrsPwuNdUjdEB0pw0o")

api<-"http://openapi.work.go.kr/opi/opi/opia/wantedApi.do"
api_key<-"WNK9J6KXM0IC1BP7CETGQ2VR1HJ"


#항목간의 관계는 and 이며, 항목내의 다중선택은 or 관계

num0fRows<-100  #한페이지에 표현할 데이터 행의 수
pageNo<- 1
callTp<-"L" # L:목록 D:상세 
returnType<-"XML" #xml지정
startPage<-1
display<-1000  #출력건
occupation<-"024"  #직종코드[A|B] ex) 컴퓨터 프로그래밍
career<-"N" #N 신입 E경력 z관계없음
region<-"11000|41000" #지역 [A|B]
#salTP<-"Y"  #Y:연봉 , M:월급, H:시급, D:일급
#termContractMmcnt<- #근무기간 1 3 6 12// 1~3개월 3~6 6~12 12


 
url<-paste(api,
           "?authKey=", api_key,
           "&numOfRows=", num0fRows,
           "&pageNo=", pageNo, 
           "&callTp=", callTp,
           "&returnType=",returnType,
           "&startPage=",startPage,
           "&display=",display,
           "&occupation=",occupation,
           "&career=",career,
           "&region=",region,
           sep="")
url
xmlFile<-xmlParse(url) #xml파일
df<-xmlToDataFrame(getNodeSet(xmlFile,"//wanted")) #돔트리에서 태그반환 
df<-subset(df, select = -c(infoSvc, wantedMobileInfoUrl, smodifyDtm, strtnmCd))
#기본값에 불필요한 정보(중복url,도로명주소<api상오류>,최종수정일)를 제거하는 과정

addr1<-(df$basicAddr)#df에 있는 basicAddr을 추출 (+지도활용)
company1<-(df$company) #df에 있는 basicAddr을 추출(+지도활용)
title1<-(df$title) #df에 있는 basicAddr을 추출 (워드 클라우드)
 
names(df)<-c("구인인증번호","회사명","채용제목","임금형태","급여","최소임금액","최대임금액","지역","근무형태","최소학력","최대학력","경력","등록일자","마감일자","채용정보URL","근무지 우편주소","기본주소","상세주소","고용형태","직종코드","우대조건");

#엑셀파일로 추출
write.csv(df,"맞춤형 채용정보.csv",row.names = TRUE) 
#고용형태코드 
#10 기간의 정함이 없는 근로계약
#11 기간의 정함이 없는 근로계약 (시간(선택)제)
#20 기간의 정함이 있는 근로계약
#21 기간의 정함이 있는 근로계약 (시간(선택)제))

#우대조건
#13 청년층

#지도로 한눈에 보기
gc<-geocode(enc2utf8(addr1))
gc
df<-data.frame(name=company1,lon=gc$lon,lat=gc$lat)

cen<-c((max(df$lon)+min(df$lon))/2,
       (max(df$lat)+min(df$lat))/2)
cen

map<-get_googlemap(center=cen,
                   maptype="roadmap",
                   zoom =10 ,
                   marker=gc)
ggmap(map,extent="device")

gmap<-ggmap(map)


#워드 클라우드
# 채용공고 제목을 기반

#title1
#nouns<-nouns(iconv(title1,"utf-8"))
#nouns.all<-unlist(nouns,use.names = F)
#nouns.all2<-nouns.all[nchar(nouns.all)>=2]
#nouns.all2
#nouns.freq<-table(nouns.all2)
#nouns.df<-data.frame(nouns.freq,stringsAsFactors = F)
#nouns.df.sort<-nouns.df[order(-nouns.df$Freq),]
#nouns.df.sort
#wordcloud(nouns.df.sort[,1],
#          freq=nouns.df.sort[,2],
#          min.freq=1,
#          scale=c(3,0.7),
#          rot.per=0.25,
#          random.order=F,
#          random.color=T,
#          colors=rainbow(10))

